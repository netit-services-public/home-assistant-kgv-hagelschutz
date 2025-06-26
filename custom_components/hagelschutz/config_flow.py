
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .const import DOMAIN, CONF_DEVICE_ID, CONF_HWTYPE_ID, DEFAULT_NAME

class HagelschutzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME, default=DEFAULT_NAME): str,
                vol.Required(CONF_DEVICE_ID): str,
                vol.Optional(CONF_HWTYPE_ID, default=188): int,
            }),
            errors=errors
        )
