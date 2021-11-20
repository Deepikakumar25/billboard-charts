import datetime
import unittest
import billboard
from nose.tools import raises


class DateTest(unittest.TestCase):
    def testDateRounding(self):
        """Checks that the Billboard website is rounding dates correctly: it should
        round up to the nearest date on which a chart was published.

        We used to check that requesting the Hot 100 chart for 1958-01-01 would
        return the first Hot 100 chart (1958-08-04), but the test was flaky.
        """
        chart = billboard.ChartData("hot-100", date="2019-12-31")
        self.assertEqual(chart.date, "2020-01-04")

    def testDatetimeDate(self):
        """Checks that ChartData correctly handles datetime objects as the
        date parameter.
        """
        chart = billboard.ChartData("hot-100", datetime.date(2016, 7, 9))
        self.assertEqual(len(chart), 100)
        self.assertEqual(chart.date, "2016-07-09")

    @raises(ValueError)
    def testUnsupportedDateFormat(self):
        """Checks that using an unsupported date format raises an exception."""
        billboard.ChartData("hot-100", date="07-30-1996")

    @raises(ValueError)
    def testEmptyStringDate(self):
        """
        Checks that passing an empty string as the date raises an exception.
        """
        billboard.ChartData("hot-100", date="")

    @raises(ValueError)
    def testInvalidDate(self):
        """Checks that passing a correctly formatted but invalid date raises an exception."""
        billboard.ChartData("hot-100", date="2018-99-99")
