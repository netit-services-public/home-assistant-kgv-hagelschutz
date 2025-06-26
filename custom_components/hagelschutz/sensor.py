
import logging
import requests
import voluptuous as vol
from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN, CONF_DEVICE_ID, CONF_HWTYPE_ID, DEFAULT_NAME

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=120)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_DEVICE_ID): cv.string,
    vol.Optional(CONF_HWTYPE_ID, default=188): vol.Coerce(int),
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    device_id = config[CONF_DEVICE_ID]
    hwtype_id = config[CONF_HWTYPE_ID]
    name = config[CONF_NAME]
    add_entities([HagelschutzSensor(name, device_id, hwtype_id)], True)

class HagelschutzSensor(Entity):
    def __init__(self, name, device_id, hwtype_id):
        self._name = name
        self._device_id = device_id
        self._hwtype_id = hwtype_id
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        url = f"https://meteo.netitservices.com/api/v0/devices/{self._device_id}/poll?hwtypeId={self._hwtype_id}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            self._state = data.get("hailState")
        except Exception as e:
            _LOGGER.error("Fehler beim Abrufen des Hagelsignals: %s", e)
            self._state = "unavailable"
