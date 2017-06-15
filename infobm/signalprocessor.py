######################################################################
# Author: Patrick Kasper
# MatNr: 0730294
# Description: A collection of functions for general use
######################################################################

import numpy as np


def detect_heartbeat(_sensor_data, _channel_name, _min_interval):
    """
    Detect heartbeats using a specified sensor. Ensures a minimal distance between beats
    :param _sensor_data: SensorData object
    :param _channel_name: Channel to use for heartbeat detection
    :param _min_interval: Minimal distance between 2 beats
    :return: List of indices for the detected heartbeats
    """
    signal = np.array(_sensor_data.get_sensor(_channel_name))
    heartbeats = []
    signal_mean = signal.mean()
    signal_std = signal.std()

    threshold = signal_mean + (2 * signal_std)
    above_threshold = False
    for index, entry in enumerate(signal):
        if (entry > threshold) and not above_threshold:
            heartbeats.append(index)
            above_threshold = True
        elif (entry < threshold) and above_threshold:
            above_threshold = False

    heartbeats_fixed = list()

    last_beat = -_min_interval
    for beat in heartbeats:
        if beat - last_beat >= _min_interval:
            heartbeats_fixed.append(beat)
            last_beat = beat

    return heartbeats_fixed


def fit_polynomial(_data, _degree):
    """
    Fits a polynomial based on the passed data and the specified degree
    :param _data: list of data values
    :param _degree: degree of the polynomial to fit
    :return: the polynomial and its evaluation for each index in the data.
    """
    if not isinstance(_data, (list, np.array)):
        raise TypeError("Invalid parameter _data. Expected {exp}, got {got}".format(exp=(list, np.array),
                                                                                    got=type(_data)))

    if not isinstance(_degree, int):
        raise TypeError("Invalid parameter _data. Expected {exp}, got {got}".format(exp=type(int),
                                                                                    got=type(_data)))
    if _degree < 1:
        raise TypeError("Invalid parameter _data. Has to be > 0")

    poly = np.poly1d(np.polyfit(np.arange(len(_data)), _data, _degree))

    return poly, poly(np.arange(len(_data)))
