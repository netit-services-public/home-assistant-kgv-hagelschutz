"""Initialisierung der Hagelschutz-Integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN


# Optional, falls YAML-Setup erlaubt werden soll (nicht zwingend notwendig)
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True


# Setzt die Integration bei Konfiguration über die UI auf
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Wichtig: async_forward_entry_setup MUSS in einem Task ausgeführt werden!
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True


# Entfernt die Integration (inkl. Sensor) korrekt
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
