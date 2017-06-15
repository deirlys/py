######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: The data class encapsulating biomedical signal cdata
######################################################################


class SensorData:
    """
    A class to store signal data. Should only be instantiated by the concrete parsers
    """
    def __init__(self, _data=None):
        """
        Constructor
        :param _data: Data to be stored
        """
        self._sensors = dict()
        if _data is not None:
            self.sensors = _data

    @property
    def sensors(self):
        """
        :return: Full data as dict
        """
        return self._sensors

    @sensors.setter
    def sensors(self, _sensor_dict):
        if not isinstance(_sensor_dict, dict):
            raise TypeError("Incorrect datatype. Expected {expected}, got {got}".format(expected=dict,
                                                                                        got=type(_sensor_dict)))
        self._sensors = _sensor_dict

    def get_sensor(self, _name):
        """
        Fetches the data for a specific sensor
        :param _name: Name of the sensor to fetch
        :return: list of sensor values
        """
        if _name not in self._sensors:
            raise ValueError("Sensor not found in data")
        return self._sensors[_name]

    def get_sensor_names(self):
        """
        Fetches the names of all available sensors
        :return: sorted list of sensor names
        """
        return sorted(list(self._sensors.keys()))
