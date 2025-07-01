
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_DEVICE_ID
from .const import DOMAIN


class HagelschutzConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Hagelschutz", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_DEVICE_ID): str,
                vol.Optional("hwtype_id", default=188): int,
            }),
            errors=errors,
        )
