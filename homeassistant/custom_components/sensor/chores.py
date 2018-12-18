from homeassistant.helpers.entity import Entity
import datetime


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([ToiletUp(), ToiletDown(), Vacuum(), Bath()])


class ToiletUp(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = "Unknown"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Upstairs Toilet"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        weekNumber = datetime.date.today().isocalendar()[1]
        self._state = ['Ben','Jacob','David','Dylan'][weekNumber % 4]

class ToiletDown(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = "Unknown"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Downstairs Toilet"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        weekNumber = datetime.date.today().isocalendar()[1]
        self._state =  ['Dylan','Ben', 'Jacob', 'David'][weekNumber % 4]


class Bath(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = "Unknown"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Bath"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        weekNumber = datetime.date.today().isocalendar()[1]
        self._state =  ['Jacob','David','Dylan','Ben'][weekNumber % 4]


class Vacuum(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = "Unknown"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Vacuum Cleaning"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        weekNumber = datetime.date.today().isocalendar()[1]
        self._state = ['David','Dylan','Ben', 'jacob'][weekNumber % 4]
