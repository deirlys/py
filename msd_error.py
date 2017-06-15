######################################################################
# Author:       Una Ibrahimpasic
# MatNr:        1431650
#
# Description:  Calculator for the Mean Signed Deviation
#               Root Mean Square is calculated with
#               E (y - x)/n)
######################################################################

from error_calculator import ErrorCalculator


class MeanSignedDeviationCalculator(ErrorCalculator):
    def __init__(self, data=list()):
        super().__init__(data)

    def calc_error(self, y):
        super().calc_error(y)
        error = 0.0
        index = 0
        for i in self.data:
            error += ((y[index] - i)/(index + 1))
            index += 1
        return error
