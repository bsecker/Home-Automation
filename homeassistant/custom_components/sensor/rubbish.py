# from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import datetime

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([RubbishSensor()])


class RubbishSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._name = "Unknown"

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'rubbish'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._name

    # @property
    # def unit_of_measurement(self):
    #     """Return the unit of measurement."""
    #     return TEMP_CELSIUS

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        weekNumber = datetime.date.today().isocalendar()[1]
        self._name =  ['Dylan','Ben', 'Jacob', 'David'][weekNumber % 4]
        