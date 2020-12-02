import pandas as pd


def find_time_of_day(x):
    """
    Helper function that takes the timestamp of a dataframe and provides the time of day.
    (6-12) --> morning
    (12-16) --> afternoon
    (16-20) --> evening
    (20-24) --> night
    (0-6) --> sleep_time
    :param x: Cell of a dataframe
    :return: time of day
    """
    if not isinstance(x, pd.Timestamp):
        raise ValueError('entry must be timestamp')
    hour = x.hour
    if 6 <= hour <= 12:
        time_of_day = 'morning'
    elif 12 < hour <= 16:
        time_of_day = 'afternoon'
    elif 16 < hour <= 20:
        time_of_day = 'evening'
    elif 20 < hour <= 24:
        time_of_day = 'night'
    elif 0 <= hour < 6:
        time_of_day = 'sleep_time'

    return time_of_day
