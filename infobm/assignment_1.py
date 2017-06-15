######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: Short script to call the infobm functionality
######################################################################

import infobm

if __name__ == "__main__":
    info_bm = infobm.InfoBm("ptbdb")
    path = "s0010_re.dat"

    info_bm.read_data(path)
    bpm = info_bm.calculate_bpm(1000, 10000)
