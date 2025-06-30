from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.entity import EntityDescription
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import aiohttp
import async_timeout
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = HailDataCoordinator(hass, entry.data["device_id"])
    await coordinator.async_config_entry_first_refresh()
    async_add_entities([HailSensor(coordinator)], True)

class HailDataCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, device_id: str):
        super().__init__(
            hass,
            _LOGGER,
            name="hagelschutz",
            update_interval=hass.config.time_zone.utcoffset(None) or timedelta(minutes=2),
        )
        self.device_id = device_id

    async def _async_update_data(self):
        url = f"https://meteo.netitservices.com/api/v0/devices/{self.device_id}/poll?hwtypeId=188"
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        data = await response.json()
                        return data
        except Exception as err:
            raise UpdateFailed(f"Fehler beim Abrufen der Daten: {err}") from err

class HailSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "Hagelalarm"
        self._attr_unique_id = f"hagelschutz_{coordinator.device_id}"

    @property
    def native_value(self):
        return self.coordinator.data.get("hailState")