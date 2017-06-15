######################################################################
# Version 1
# Author:       Patrick Kasper
# MatNr:        0730294
# Version 2
# Author:       Una Ibrahimpasic
# MatNr:        1431650
# Version 2:    Extended with Linear Regression
#               uses s0010_re.dat, for different results change the
#               data variable and put in array or list
#
# Short script to call the infobm functionality
######################################################################
import infobm

import numpy as np
from rms_error import RootMeanSquareCalculator
from ma_error import MeanAbsoluteCalculator
from ms_error import MeanSquareCalculator
from msd_error import MeanSignedDeviationCalculator

from m_error import MeanCalculator

from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    # assignment one
    # code
    info_bm = infobm.InfoBm("ptbdb")
    path = "s0010_re.dat"

    info_bm.read_data(path)
    bpm = info_bm.calculate_bpm(1000, 10000)

    # From notebook
    # https://github.com/pkasper/info2-bm/tree/master/tutor_sessions
    data = bpm
    # define window size
    _window_size = 200
    # define forecast
    forecast = 10
    window_data = data[:-forecast]
    windows = []
    for i in range(len(window_data) - _window_size + 1):
        windows.append(data[i: i + _window_size])
    fc = list(range(len(window_data) - _window_size + 1))
    for i in range(len(window_data) - _window_size + 1):
        fc[i] = data[i + _window_size + forecast - 1]
    # Using pandas for simplicity purpose (no need to go into detail)
    df = pd.DataFrame.from_dict({"X": windows, "y": fc})
    # 80% training data
    split = int(len(df) * 0.8)
    # split data into train and
    train = df[:split]
    # test data
    test = df[split:]
    reg = linear_model.LinearRegression(normalize=True)
    reg.fit(list(train['X']), list(train['y']))
    predict = reg.predict(list(test['X']))
    test['prediction'] = predict  # ignore warning
    # Plot all the datas
    plt.plot(train['y'], '-b', label='data')
    plt.plot(test['y'], '-c', label='test')
    plt.plot(test['prediction'], '--r', label='prediction')
    plt.legend(loc='best')
    plt.savefig('predict.png', bbox_inches='tight')
    plt.show()
    # Calculate the errors with the written classes
    rms = RootMeanSquareCalculator(data=test['y'])
    ma = MeanAbsoluteCalculator(data=test['y'])
    ms = MeanSquareCalculator(data=test['y'])
    msd = MeanSignedDeviationCalculator(data=test['y'])
    bias = MeanCalculator(data=test['y'])
    # Print out the errors
    # Rounding 5 digits after comma
    rms_val = round(rms.calc_error(predict), 5)
    ma_val = round(ma.calc_error(predict), 5)
    ms_val = round(ms.calc_error(predict), 5)
    msd_val = round(msd.calc_error(predict), 5)
    bias_val = round(bias.calc_error(predict), 5)
    print(rms_val)
    print(ma_val)
    print(ms_val)
    print(msd_val)
    print(bias_val)
    # Plot the errors
    # Example taken from
    # https://pythonspot.com/en/matplotlib-bar-chart/
    objects = ('MA', 'MS', 'MSD', 'RMS', 'BIAS')
    y_pos = np.arange(len(objects))
    performance = [ma_val, ms_val, msd_val, rms_val, bias_val]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Error')
    plt.title('Error calculated')
    plt.savefig('error.png', bbox_inches='tight')
    plt.show()
