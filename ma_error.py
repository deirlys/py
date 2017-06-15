######################################################################
# Author:       Una Ibrahimpasic
# MatNr:        1431650
#
# Description:  Calculator for the mean absolute error
#               Mean Absolute is calculated with
#               E (abs(y - x)) / len
######################################################################

from error_calculator import ErrorCalculator


class MeanAbsoluteCalculator(ErrorCalculator):
    def __init__(self, data=list()):
        super().__init__(data)

    def calc_error(self, y):
        super().calc_error(y)
        error = 0.0
        index = 0
        for i in self.data:
            error += abs(y[index] - i)
            index += 1
        return error / len(y)
