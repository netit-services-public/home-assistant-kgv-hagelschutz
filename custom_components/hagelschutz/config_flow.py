import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_DEVICE_ID
from .const import DOMAIN, DEFAULT_HWTYPE_ID

class HagelschutzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_DEVICE_ID], data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_DEVICE_ID): str,
            vol.Optional("hwtype_id", default=DEFAULT_HWTYPE_ID): int,
        })

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
