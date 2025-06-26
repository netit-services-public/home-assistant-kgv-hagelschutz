from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, config_entry, async_add_entities):
    device_id = config_entry.data["device_id"]
    hwtype_id = config_entry.data.get("hwtype_id", "188")
    async_add_entities([HagelSensor(device_id, hwtype_id)], True)

class HagelSensor(Entity):
    def __init__(self, device_id, hwtype_id):
        self._device_id = device_id
        self._hwtype_id = hwtype_id
        self._state = None

    @property
    def name(self):
        return "Hagelalarm"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        import aiohttp
        url = f"https://meteo.netitservices.com/api/v0/devices/{self._device_id}/poll?hwtypeId={self._hwtype_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                self._state = data.get("hailState", None)
