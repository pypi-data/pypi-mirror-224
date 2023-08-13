import aiohttp
import pytest
from aioresponses import aioresponses, CallbackResult
from pyliblorawan.helpers.exceptions import CannotConnect, InvalidAuth
from pyliblorawan.models import Device
from pyliblorawan.network_servers.ttn import TTN


@pytest.fixture
def ttn_uplink() -> dict:
    return {"uplink_message": {"frm_payload": "/gDt", "f_port": 123}}


def callback_get_devices(url: str, **kwargs) -> CallbackResult:
    assert kwargs["headers"]["Authorization"] == "Bearer TEST-API-KEY"
    assert kwargs["headers"]["Accept"] == "application/json"
    assert kwargs["headers"]["User-Agent"] == "pyLibLoRaWAN"

    return CallbackResult(
        payload={
            "end_devices": [
                {
                    "ids": {
                        "device_id": "TEST-DEVICE",
                        "application_ids": {"application_id": "TEST-APPLICATION"},
                        "dev_eui": "FEEDABCD00000002",
                        "join_eui": "FEEDABCD00000001",
                    },
                    "created_at": "2023-07-24T23:35:49.598651Z",
                    "updated_at": "2023-07-24T23:35:49.598651Z",
                }
            ]
        }
    )


def test_constructor():
    ttn = TTN("TEST-API-KEY", "TEST-APPLICATION", "http://TEST.URL")

    assert ttn._application == "TEST-APPLICATION"
    assert ttn._url == "http://TEST.URL/"
    assert ttn._headers == {
        "Accept": "application/json",
        "Authorization": "Bearer TEST-API-KEY",
        "User-Agent": "pyLibLoRaWAN",
    }

    ttn = TTN("TEST-API-KEY", "TEST-APPLICATION", "http://TEST.URL/")
    assert ttn._url == "http://TEST.URL/"


def test_normalize_uplink(ttn_uplink):
    ttn = TTN("TEST-API-KEY", "TEST-APPLICATION", "http://TEST.URL")
    uplink = ttn.normalize_uplink(ttn_uplink)

    assert uplink.f_port == 123
    assert uplink.payload == bytes.fromhex("FE00ED")


@pytest.mark.asyncio
async def test_list_device_euis():
    ttn = TTN("TEST-API-KEY", "TEST-APPLICATION", "http://TEST.URL")
    session = aiohttp.ClientSession()

    with aioresponses() as m:
        m.get(
            "http://TEST.URL/api/v3/applications/TEST-APPLICATION/devices",
            callback=callback_get_devices,
        )
        devices = await ttn.list_device_euis(session)
        assert devices == [Device("FEEDABCD00000002", "TEST-DEVICE")]

    await session.close()


@pytest.mark.asyncio
async def test_list_device_euis_unauthorized():
    ttn = TTN("TEST-API-KEY", "TEST-APPLICATION", "http://TEST.URL")
    session = aiohttp.ClientSession()

    with aioresponses() as m:
        m.get(
            "http://TEST.URL/api/v3/applications/TEST-APPLICATION/devices",
            status=401,
        )
        with pytest.raises(InvalidAuth):
            _ = await ttn.list_device_euis(session)

    await session.close()


@pytest.mark.asyncio
async def test_list_device_euis_unknown():
    ttn = TTN("TEST-API-KEY", "TEST-APPLICATION", "http://TEST.URL")
    session = aiohttp.ClientSession()

    with aioresponses() as m:
        m.get(
            "http://TEST.URL/api/v3/applications/TEST-APPLICATION/devices",
            status=400,
        )
        with pytest.raises(CannotConnect) as e:
            _ = await ttn.list_device_euis(session)
        assert str(e.value) == "400"

    await session.close()
