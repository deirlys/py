######################################################################
# Author:       Una Ibrahimpasic
# MatNr:        1431650
#
# Description:  Calculator for the mean error
#               Mean error is calculated with
#               (E(x[n]-y[n]))/n
######################################################################

from error_calculator import ErrorCalculator


class MeanCalculator(ErrorCalculator):
    def __init__(self, data=list()):
        super().__init__(data)

    def calc_error(self, y):
        super().calc_error(y)
        return (sum(y) - sum(self.data)) / len(y)
