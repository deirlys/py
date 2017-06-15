######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: The concrete parser for ptbdb data
######################################################################

from collections import defaultdict
import struct

from infobm.inputparser import InputParser
from infobm.sensordata import SensorData

#  List of sensors in the data
SENSORS = ["i", "ii", "iii", "avr", "avl", "avf", "v1", "v2", "v3", "v4", "v5", "v6"]

#  The best sensor to use when detecting heartbeats
HEARTBEAT_SENSOR = "i"


class PtbdbParser(InputParser):
    """
    Concrete class implementing a parser for the ptb database
    """
    def __init__(self):
        super().__init__()

    def read_file(self):
        """
        Reads the file according to the Ptbdb specifications.
        """
        sensor_dict = defaultdict(list)

        with open(self._data_file, "rb") as data_file:
            while True:
                try:
                    current_frame = {key: struct.unpack("h", data_file.read(2))[0] for key in SENSORS}
                except:  # Very broad exception but we dont really care why the package fails
                    break
                [sensor_dict[key].append(value) for key, value in current_frame.items()]
        self._data = SensorData(sensor_dict)
        return True

    @staticmethod
    def get_heartbeat_sensor():
        """
        :return: the preferred sensor for heartbeat detection
        """
        return HEARTBEAT_SENSOR
