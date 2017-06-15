######################################################################
# Author:       Una Ibrahimpasic
# MatNr:        1431650
#
# Description:  Calculator for the mean square error
#               Mean Square is calculated with
#               E ((y - x)^2) / len
######################################################################

from error_calculator import ErrorCalculator


class MeanSquareCalculator(ErrorCalculator):
    def __init__(self, data=list()):
        super().__init__(data)

    def calc_error(self, y):
        super().calc_error(y)
        error = 0.0
        index = 0
        for i in self.data:
            error += (i - y[index]) ** 2
            index += 1
        return error / len(y)
