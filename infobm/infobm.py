######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: Main Class of the infobm package
######################################################################

from infobm import ptbdbparser
from infobm.signalprocessor import *


class InfoBm:
    """
    Main class for the infobm package. Provides abstracted functionality to read data files and calculate bpm
    """
    _parsers = {"ptbdb": ptbdbparser.PtbdbParser}

    def __init__(self, _parser="ptbdb"):
        """
        Constructor
        :param _parser: The concrete parser to use. Defaults to ptbdb
        """
        if _parser not in self._parsers.keys():
            raise ValueError("Incorrect parser type specified")
        self._parser = self._parsers[_parser]()
        self._data = None

    def read_data(self, _filename):
        """
        Instructs the parser to read the data file. On success fetches the data SignalData Object and 
        stores it in the data property
        :param _filename: path to the data fue
        :return: -
        """
        self._parser.data_file = _filename
        read_success = self._parser.read_file()

        if read_success:
            self._data = self._parser.data
        else:
            raise IOError("File could not be read")

    def calculate_bpm(self, _signal_rate, _window_size, _sensor=None, _min_distance=100):
        """
        Calculates the bpm for the stored signal data
        :param _signal_rate: signal rate in frames per second
        :param _window_size: size of the rolling window
        :param _sensor: name of the sensor to use. Defaults to none which asks the parser
        :param _min_distance: minimum distance between two heartbeats
        :return: list of bpm for every window. aligns left (first value is the mean bpm based on the first window) 
        """
        if self._data is None:
            raise IOError("No data loaded.")

        if not isinstance(_min_distance, int):
            raise TypeError("Invalid parameter _min_distance. Expected: {exp}, got: {got}".format(exp=type(int),
                                                                                                  got=type(_min_distance)))
        if _sensor is None:
            _sensor = self._parser.get_heartbeat_sensor()
        if _sensor not in self._data.get_sensor_names():
            raise ValueError("Sensor not found in data")
        beats = detect_heartbeat(self._data, _sensor, _min_distance)
        windows = [(i, i+_window_size) for i in range(len(self._data.get_sensor(_sensor)) - _window_size + 1)]

        bpm_ratio = 60 * (_signal_rate / _window_size)

        bpm = [len([b for b in beats if x[0] < b < x[1]]) * bpm_ratio for x in windows]
        return bpm
