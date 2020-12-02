import unittest
import datetime
from src.preprocess import *


class TestPreprocess(unittest.TestCase):
    def test_find_time_of_day(self):
        example = pd.DataFrame([datetime.datetime.strptime('18-30-00', '%H-%M-%S')])
        example_time_of_day = find_time_of_day(x=example.iloc[0,0])
        self.assertEquals(example_time_of_day, 'evening')
