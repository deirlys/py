######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: Main Class of the infobm package
#
# Version 2:
# Author: Una Ibrahimpasic
# Author: Dragan Babic
# Author: Edina Bojic
#
# Description: Adjusted the version by Patrick Kasper, now there is a
# different parser support, removed old one due to incompatibility.
# Added a classify function
######################################################################

from infotsd import tsdparser
from scipy.linalg import norm


class InfoTsd:
    """
    Main class for the infobm package. Provides abstracted
     functionality to read data files and calculate bpm
    """
    _parsers = {"tsd": tsdparser.TsdParser}

    def __init__(self, _parser="tsd"):
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
        Instructs the parser to read the data file. On success fetches
        the data SignalData Object and
        stores it in the data property
        :param _filename: path to the data fue
        :return: -
        """
        self._parser.data_file = _filename
        read_success = self._parser.read()

        if read_success:
            self._data = self._parser.data
        else:
            raise IOError("File could not be read")

    def classify(self):
        real_label = []
        calc_label = []
        coder = self._parser.coder
        # Dynamic K, based on weeks. Nobody likes magic numbers
        for test in range(0, coder.encoded_weeks()):
            test_set = self._data[test]
            for training in range(0, coder.encoded_weeks()):
                if training is not test:
                    # Exclude the test set for the training
                    training_set = self._data[training]
                    for real_sign in range(0,
                                           coder.encoded_signs(test)):
                        real_label.append(
                            coder.decode(test, real_sign)[0] + " - " +
                            coder.decode(test, real_sign)[1])
                        lowest_norm = 1000
                        looks_like = 0
                        for sign in range(0, coder.encoded_signs(
                                training)):
                            # Cover all the signs
                            work_test = test_set[real_sign]
                            work_training = training_set[sign]
                            # Slicing
                            if len(work_test) > len(work_training):
                                work_test = work_test[
                                            :len(work_training)]
                            if len(work_training) > len(work_test):
                                work_training = work_training[
                                                :len(work_test)]
                            # Calculating Frobenius form and
                            # getting the one closest only
                            result_set = work_test - work_training
                            if norm(result_set) < lowest_norm:
                                lowest_norm = norm(result_set)
                                looks_like = sign
                        calc_label.append(
                            coder.decode(training, looks_like)[
                                0] + " - " +
                            coder.decode(training, looks_like)[1])

        return real_label, calc_label
