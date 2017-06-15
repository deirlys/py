######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: The abstract parser class
######################################################################

import abc
import os


class InputParser(metaclass=abc.ABCMeta):
    """
    An abstract class defining the interface for concrete parsers.
    I reads an input file and creates a SensorData object with its contents
    """
    def __init__(self):
        self._data_file = None,
        self._data = None

    @property
    def data(self):
        """
        :return: The read data as a SignalData Object
        """
        if self._data is None:
            raise ValueError("Data is not set. Maybe the data file has yet to be read.")
        return self._data

    @property
    def data_file(self):
        """
        :return: current path to the data file
        """
        return self._data_file

    @data_file.setter
    def data_file(self, _path):
        if not os.path.isfile(_path):
            raise ValueError("Given filepath does not exist")

        self._data_file = _path

    @abc.abstractmethod
    def read_file(self):
        """
        Subclasses are meant to override this method to implement their specific parsers
        """
        raise NotImplementedError()
