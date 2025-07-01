
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import HomeAssistantType
from datetime import timedelta
import logging
import aiohttp

from .const import DOMAIN, API_BASE_URL, DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry, async_add_entities):
    device_id = entry.data.get("device_id")
    hwtype_id = entry.data.get("hwtype_id", 188)

    coordinator = HailCoordinator(hass, device_id, hwtype_id)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([HagelschutzSensor(coordinator)])


class HailCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistantType, device_id: str, hwtype_id: int):
        super().__init__(
            hass,
            _LOGGER,
            name="Hagelschutz Coordinator",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.device_id = device_id
        self.hwtype_id = hwtype_id

    async def _async_update_data(self):
        url = f"{API_BASE_URL}/devices/{self.device_id}/poll?hwtypeId={self.hwtype_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()


class HagelschutzSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Hagelschutz"
        self._attr_unique_id = f"{coordinator.device_id}_hail"
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def native_value(self):
        return self.coordinator.data.get("hailState", "unbekannt")
