import logging
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
import requests

_LOGGER = logging.getLogger(__name__)

CONF_DEVICE_ID = "device_id"
CONF_HWTYPE_ID = "hwtype_id"
DEFAULT_NAME = "Hagelalarm"
DEFAULT_HWTYPE_ID = 188

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_DEVICE_ID): cv.string,
    vol.Optional(CONF_HWTYPE_ID, default=DEFAULT_HWTYPE_ID): cv.positive_int,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config[CONF_NAME]
    device_id = config[CONF_DEVICE_ID]
    hwtype_id = config[CONF_HWTYPE_ID]
    add_entities([HagelAlarmSensor(name, device_id, hwtype_id)], True)

class HagelAlarmSensor(Entity):
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
            self._state = response.json().get("hailState")
        except Exception as e:
            _LOGGER.error("Fehler beim Abrufen des Hagelalarms: %s", e)
            self._state = "unavailable"
