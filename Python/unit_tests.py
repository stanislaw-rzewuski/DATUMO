import unittest
from unittest.mock import mock_open, patch
from datetime import datetime
from helpers_module import sort_pair, read_numbers_from_file, write_numbers_to_file, find_pairs, get_time_stamp, Style


class TestFunctions(unittest.TestCase):

    # Test for sort_pair function
    def test_sort_pair(self):
        self.assertEqual(sort_pair([5, 3]), [3, 5])
        self.assertEqual(sort_pair([1, 2]), [1, 2])
        self.assertEqual(sort_pair([-1, 0]), [-1, 0])

    # Test for read_numbers_from_file function
    @patch("builtins.open", new_callable=mock_open, read_data="1;2;3")
    def test_read_numbers_from_file_semicolon(self, mock_file):
        result = read_numbers_from_file("dummy_path")
        self.assertEqual(result, [1, 2, 3])

    @patch("builtins.open", new_callable=mock_open, read_data="4,5,6")
    def test_read_numbers_from_file_comma(self, mock_file):
        result = read_numbers_from_file("dummy_path")
        self.assertEqual(result, [4, 5, 6])

    @patch("builtins.open", new_callable=mock_open, read_data="4,5,A")
    def test_read_numbers_from_file_value_error(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file("dummy_path")

    # Test for file not found in read_numbers_from_file
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_numbers_from_file_not_found(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file("dummy_path")

    # Test for file not found in read_numbers_from_file
    @patch("builtins.open", side_effect=ValueError)
    def test_read_numbers_from_file_not_found(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file([0,11,9])

    # Test for file that is empty
    @patch("builtins.open")
    def test_read_numbers_from_file_empty_file(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file(".\\TestData\\TESTInput_2_emptyFile.csv")

    # Test for file that is having float instead of integer
    @patch("builtins.open")
    def test_read_numbers_from_file_empty_file(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file(".\\TestData\\TESTInput_2_float.csv")

    # Test for file that is having single comma
    @patch("builtins.open")
    def test_read_numbers_from_file_empty_file(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file(".\\TestData\\TESTInput_2_singleComma.csv")

    # Test for file that is having single semicolon
    @patch("builtins.open")
    def test_read_numbers_from_file_empty_file(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file(".\\TestData\\TESTInput_2_singleSemicolon.csv")

    # Test for file that is having single string
    @patch("builtins.open")
    def test_read_numbers_from_file_empty_file(self, mock_file):
        with self.assertRaises(SystemExit):
            read_numbers_from_file(".\\TestData\\TESTInput_2_string.csv")

    # Test for write_numbers_to_file function
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_write_numbers_to_file(self, mock_makedirs, mock_file):
        result = write_numbers_to_file("dummy_path/output.txt", [1, 2, 3])
        mock_file.assert_called_with("dummy_path/output.txt", 'w')
        self.assertTrue(result)

    # Test for directory creation in write_numbers_to_file
    @patch("os.path.exists", return_value=False)
    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_write_numbers_to_file_directory_creation(self, mock_file, mock_makedirs, mock_exists):
        write_numbers_to_file("dummy_dir/output.txt", [1, 2, 3])
        mock_makedirs.assert_called_once_with("dummy_dir")

    # Test for find_pairs function
    def test_find_pairs(self):
        result, leftovers = find_pairs([10, 2, 5], 12)
        self.assertEqual(result, [[2, 10]])
        self.assertEqual(leftovers, [5])

        result, leftovers = find_pairs([10, -10, 2, -20], 0)
        self.assertEqual(result, [[-10, 10]])
        self.assertEqual(leftovers, [2, -20])

        result, leftovers = find_pairs([1, 2, 3], 10)
        self.assertEqual(result, [])
        self.assertEqual(leftovers, [1, 2, 3])

    # Test for get_time_stamp function
    @patch("helpers_module.datetime")
    def test_get_time_stamp(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, 0, 123456)
        self.assertEqual(get_time_stamp(), "2024.01.01__12-00-00-123")


if __name__ == '__main__':
    unittest.main()
