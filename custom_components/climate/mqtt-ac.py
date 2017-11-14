import logging

import requests
import voluptuous as vol

from homeassistant.components.climate import(
    ClimateDevice, PLATFORM_SCHEMA, ATTR_TEMPERATURE, STATE_COOL, STATE_DRY, 
    STATE_FAN_ONLY)

from homeassistant.const import (
        CONF_NAME, STATE_ON, STATE_OFF, STATE_UNKNOWN)

from homeassistant.components.mqtt import (
        CONF_COMMAND_TOPIC, CONF_QOS, CONF_RETAIN, CONF_STATE_TOPIC)

import homeassistant.helpers.config_validation as cv

REQUIREMENTS = ['MQTT']

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = 'MQTT Thermostat'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_TEMP_COMMAND_TOPIC) : mqtt.valid_publish_topic,
    vol.Optional(CONF_FAN_COMMAND_TOPIC) : mqtt.valid_publish_topic,

})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup MQTT AirCon thermostat."""
    
    name = config.get(CONF_NAME)


class MqttThermostat(ClimateDevice):
    """Representation of an MQTT Thermostat."""

    def __init__(self, climate):

