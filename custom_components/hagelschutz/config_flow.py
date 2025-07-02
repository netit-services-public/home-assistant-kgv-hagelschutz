from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class HagelschutzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            device_id = user_input.get("device_id", "")
            hwtype_id = user_input.get("hwtype_id", 188)

            # Validierung der device_id: exakt 12 alphanumerische Zeichen
            if not isinstance(device_id, str) or len(device_id) != 12 or not device_id.isalnum():
                errors["device_id"] = "invalid_device_id"
            else:
                return self.async_create_entry(title="Hagelschutz", data={
                    "device_id": device_id,
                    "hwtype_id": hwtype_id
                })

        # Schema mit Validierungslogik
        schema = vol.Schema({
            vol.Required("device_id"): str,
            vol.Optional("hwtype_id", default=188): int,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors
        )