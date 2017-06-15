######################################################################
# Version 1
# Author: Patrick Kasper
# MatNr: 0730294
# Version 2
# Author: Una Ibrahimpasic
# MatNr: 1431056
# Version 2: Containing a type check
#
#
# Interface class for calculating errors
######################################################################


import abc
import numpy as np
import pandas as pd


class ErrorCalculator(metaclass=abc.ABCMeta):
    """A class built to calculate errors on data series.
    This is an abstract class and thus, concrete implementations of the 
    error calculation methods have to be defined in the child classes.

    IMPORTANT: The predefined lengthcheck was changed. Both this and the
               old version will be accepted for submissions!

    Args:
      data (list): The series of true/test data. Can be of np.array(). 
                   This is the series of values you want to test against.

    Attributes:
      _data (str): The stored list of of true/test data. Only to be set
                   via the properties.
    """

    def __init__(self, data=list()):
        if self.__class__ is ErrorCalculator:
            raise NotImplementedError(
                "Instantiated base class. Use a derivative!")
        self._data = data

    @property
    def data(self):
        """
        Property to access the true/test data. Can either be set in the class constructor
        or via this property. 
        """
        type_check(self._data)
        return self._data

    @data.setter
    def data(self, data):
        type_check(data)
        self._data = data

    @abc.abstractmethod
    def calc_error(self, y):
        """
        This method calculates the error of series y on the stored test data.
        Args:
          y: The series to test with (against the values in self._data)

        Returns:
          The return value. The calculated error of series y on self_data
        """
        type_check(y)
        if self._data is None:
            raise ValueError("Data is not set")
        if len(y) != len(self._data):
            raise ValueError("Series are not of identical length")


def type_check(data):
    # Only work with types that are tested
    # Currently those are: Tuple, numpy array, list, and panda series
    if not isinstance(data, list) \
            and not isinstance(data, np.ndarray) \
            and not isinstance(data, tuple) \
            and not isinstance(data, pd.Series):
        raise TypeError(
            "Invalid parameter data. Expected: "
            "tuple/numpy.ndarray/array/series, got: {got}".format(
                got=type(data)))
