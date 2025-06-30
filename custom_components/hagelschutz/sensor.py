from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import CONF_DEVICE_ID
from .const import DOMAIN, DEFAULT_HWTYPE_ID, DEFAULT_SCAN_INTERVAL, API_URL_TEMPLATE
import aiohttp
import asyncio
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    device_id = entry.data[CONF_DEVICE_ID]
    hwtype_id = entry.data.get("hwtype_id", DEFAULT_HWTYPE_ID)

    coordinator = HailCoordinator(hass, device_id, hwtype_id)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([HagelschutzSensor(coordinator)], True)

class HailCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, device_id, hwtype_id):
        super().__init__(
            hass,
            _LOGGER,
            name="Hagelschutz",
            update_interval=asyncio.timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.device_id = device_id
        self.hwtype_id = hwtype_id

    async def _async_update_data(self):
        url = API_URL_TEMPLATE.format(device_id=self.device_id, hwtype_id=self.hwtype_id)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    data = await response.json()
                    return data.get("hailState", "unknown")
            except Exception as e:
                raise UpdateFailed(f"Fehler beim Abrufen: {e}")

class HagelschutzSensor(Entity):
    def __init__(self, coordinator: HailCoordinator):
        self.coordinator = coordinator

    @property
    def name(self):
        return "Hagelalarm"

    @property
    def state(self):
        return self.coordinator.data

    @property
    def unique_id(self):
        return f"hagelschutz_{self.coordinator.device_id}"

    async def async_update(self):
        await self.coordinator.async_request_refresh()
