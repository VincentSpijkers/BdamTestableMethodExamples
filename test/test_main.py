import unittest
from datetime import datetime

import main
from not_a_date_exception import NotADateException


class TestMain(unittest.TestCase):

    def test_format_YMD_to_DMY_WithYMDDateTime_toBeDMYDate(self):
        #arrange
        ymd_date = datetime(2021, 5, 16)

        #act
        converted_date = main.format_YMD_to_DMY(ymd_date)
        expected_value = "16-05-2021"

        #assert
        self.assertEqual(str(converted_date), expected_value)

    def test_format_YMD_to_DMY_WithWrongValue_NotADateException(self):
        # arrange
        wrong_date = "__TestDate__"

        # assert
        self.assertRaises(NotADateException, main.format_YMD_to_DMY, wrong_date)

    def test_convert_string_to_date_WithStringValue_toBeDateTimeObject(self):
        # arrange
        string_date = "16-5-2021"

        # act
        converted_date = main.convert_string_to_date(string_date)

        # assert
        self.assertIsInstance(converted_date, datetime)
