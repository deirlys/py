######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: The abstract parser class
#
# Version 2:
# Author: Una Ibrahimpasic
# Author: Dragan Babic
# Author: Edina Bojic
#
# Description: Adjusted the version by Patrick Kasper with a different
# data type, and added a coder for encoding and decoding names
######################################################################

import abc
import os
from infotsd.coder import Coder


class InputParser(metaclass=abc.ABCMeta):
    """
    An abstract class defining the interface for concrete parsers.
    I reads an input file and creates a SensorData object with its
     contents
    """

    def __init__(self):
        self._data = {}
        self._coder = Coder()
        self._data_file = None,
        self._data_dir = None,
        self._is_dir = False,
        self._data = None

    @property
    def coder(self):
        return self._coder

    @property
    def data(self):
        """
        :return: The read data as a SignalData Object
        """
        if self._data is None:
            raise ValueError(
                "Data is not set. Maybe the data file has yet "
                "to be read.")
        return self._data

    @property
    def data_file(self):
        """
        :return: current path to the data file
        """
        return self._data_file

    @data_file.setter
    def data_file(self, _path):
        if os.path.isfile(_path):
            self._data_file = _path
            self._is_dir = False
        elif os.path.isdir(_path):
            self._data_dir = _path
            self._is_dir = True
        else:
            raise ValueError("Given filepath does not exist")

    @property
    def is_dir(self):
        return self._is_dir

    @abc.abstractmethod
    def read(self):
        """
        Subclasses are meant to override this method to implement their
        specific parsers
        """
        raise NotImplementedError()
