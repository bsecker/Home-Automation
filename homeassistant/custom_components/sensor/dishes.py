# from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import datetime

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([DishesSensor()])


class DishesSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._name = "Uknown"
        self.OFFSET = -1

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Whos on Dishes?'

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
        names = ["Jacob", "Ben", "Dylan", "David"]
        today = datetime.datetime.now()
        day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + self.OFFSET
        name = names[day_of_year % len(names)]
        
        self._name = name