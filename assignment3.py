######################################################################
# Author: Una Ibrahimpasic
# Author: Dragan Babic
# Author: Edina Bojic
# Reads out a path, and classifies and tests data inside
######################################################################


import infotsd

info_tsd = infotsd.InfoTsd("tsd")
path = "Datas"
info_tsd.read_data(path)
print("Data read")
result_tuple = info_tsd.classify()
print("Data classified")
for index in range(0, len(result_tuple[0])):
    print(str(result_tuple[0][index]) + " identifies as " + str(
        result_tuple[1][index]))
