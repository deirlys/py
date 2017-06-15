######################################################################
# Author:       Una Ibrahimpasic
# MatNr:        1431650
#
# Description:  Calculator for the root mean square error
#               Root Mean Square is calculated with
#               sqrt(E ((y - x)^2) / len)
######################################################################

from error_calculator import ErrorCalculator
import math


class RootMeanSquareCalculator(ErrorCalculator):
    def __init__(self, data=list()):
        super().__init__(data)

    def calc_error(self, y):
        super().calc_error(y)
        error = 0.0
        index = 0
        for i in self.data:
            error += (i - y[index]) ** 2
            index += 1
        return math.sqrt(error / len(self.data))
