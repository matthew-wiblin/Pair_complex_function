from lib.complex_function import *
import pytest

def test_user_over_sixteen():
    date_of_birth = "1950-02-10"
    assert validate_age(date_of_birth) == "Access has been granted"

def test_user_under_sixteen():
    date_of_birth = "2010-02-10"
    assert validate_age(date_of_birth) == "Access has been denied, your age is 14 and the required age is 16"

def test_wrong_format_of_date():
    with pytest.raises(Exception) as e:
        validate_age("12-05-1988")
    error_message = str(e.value)
    assert error_message == "Date in wrong format, please answer in YYYY-MM-DD format"
