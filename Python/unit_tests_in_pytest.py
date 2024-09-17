import pytest
from datetime import datetime
from helpers_module import sort_pair, read_numbers_from_file, write_numbers_to_file, find_pairs, get_time_stamp


# Test for sort_pair function
def test_sort_pair():
    assert sort_pair([5, 3]) == [3, 5]
    assert sort_pair([1, 2]) == [1, 2]
    assert sort_pair([-1, 0]) == [-1, 0]


# Test for read_numbers_from_file function with semicolon delimiter
def test_read_numbers_from_file_semicolon_data(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("1;2;3")

    monkeypatch.setattr("builtins.open", mock_open)
    result = read_numbers_from_file("dummy_path")
    assert result == [1, 2, 3]


# Test for read_numbers_from_file function with comma delimiter
def test_read_numbers_from_file_comma(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("4,5,6")

    monkeypatch.setattr("builtins.open", mock_open)
    result = read_numbers_from_file("dummy_path")
    assert result == [4, 5, 6]


# Test for file not found in read_numbers_from_file
def test_read_numbers_from_file_not_found(monkeypatch):
    def mock_open(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for ValueError in read_numbers_from_file
def test_read_numbers_from_file_ValueError(monkeypatch):
    def mock_open(*args, **kwargs):
        raise ValueError

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for empty file
def test_read_numbers_from_file_empty_file(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for file with float numbers
def test_read_numbers_from_file_file_with_float_number(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("1.1,2.2")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for file with a single comma
def test_read_numbers_from_file_file_with_single_comma(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO(",")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for file with a single semicolon
def test_read_numbers_from_file_file_with_single_semicolon(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO(";")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for file with a single string
def test_read_numbers_from_file_file_with_string(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("some_string")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(SystemExit):
        read_numbers_from_file("dummy_path")


# Test for write_numbers_to_file function
def test_write_numbers_to_file(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO()

    monkeypatch.setattr("builtins.open", mock_open)
    mock_makedirs = lambda x: None  # Mock directory creation
    monkeypatch.setattr("os.makedirs", mock_makedirs)

    result = write_numbers_to_file("dummy_path/output.txt", [1, 2, 3])
    assert result is True



# Test for find_pairs function
def test_find_pairs():
    result, leftovers = find_pairs([10, 2, 5], 12)
    assert result == [[2, 10]]
    assert leftovers == [5]

    result, leftovers = find_pairs([10, -10, 2, -20], 0)
    assert result == [[-10, 10]]
    assert leftovers == [2, -20]

    result, leftovers = find_pairs([1, 2, 3], 10)
    assert result == []
    assert leftovers == [1, 2, 3]


# Test for get_time_stamp function
def test_get_time_stamp(monkeypatch):
    class MockDatetime:
        @staticmethod
        def now():
            return datetime(2024, 1, 1, 12, 0, 0, 123456)

    monkeypatch.setattr("helpers_module.datetime", MockDatetime)
    assert get_time_stamp() == "2024.01.01__12-00-00-123"
