######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: The concrete parser for ptbdb data
#
# Version 2:
# Author: Una Ibrahimpasic
# Author: Dragan Babic
# Author: Edina Bojic
#
# Description: Adjusted the version by Patrick Kasper, reading folders
# instead of just files, and validates the files. Only accepts folders
# containing tctodd
######################################################################

import os
import pandas as pd
from infotsd.inputparser import InputParser


class TsdParser(InputParser):
    """
    Concrete class implementing a parser for the ptb database
    """

    def __init__(self):
        super().__init__()
        self._data = {}

    @staticmethod
    def read_file(origin, folder, file):
        path = os.path.join(origin, folder, file)
        csv = pd.read_csv(path, header=None, sep="\t")
        if not csv.shape[1] == 22:
            raise ValueError("CSV file {file} has {rows} /22 rows" \
                             .format(file=repr(path),
                                     rows=repr(csv.shape[1])))
        return csv

    @staticmethod
    def read_folder(self, origin, folder):
        folder_dic = {}
        for root, dirs, files in os.walk(os.path.join(origin, folder),
                                         topdown=False):
            for name in files:
                day = self._coder.encode(folder, name)[1]
                folder_dic[day] = TsdParser.read_file(origin, folder,
                                                      name)
        return folder_dic

    def read(self):
        if not self._is_dir:
            raise ValueError("We have a file, but expect a directory")
        for root, dirs, files in os.walk(self._data_dir, topdown=False):
            for name in dirs:
                # lets check all the directories and make sure it
                # #contains data
                if "tctodd" in name:
                    self._data[self._coder.encode_week(
                        name)] = self.read_folder(self, root, name)
        return True
