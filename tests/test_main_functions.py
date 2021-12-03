import pytest
from unittest import TestCase
from utils import read_json, filter_exclusives, set_profits


@pytest.mark.parametrize("test_case_file, len_non_priority", [
    ("tests/test_cases/all_exclusives.json", 0),
    ("tests/test_cases/main_case.json", 4),
    ("tests/test_cases/more_shops_and_orders.json", 4),
    ("tests/test_cases/no_exclusives.json", 5)
])
def test_filter_exclusives_non_priority(test_case_file, len_non_priority):
    """
    Tests the non priority motoboys list is correctly set
    """
    test_case = read_json(test_case_file)
    non_priority = filter_exclusives(test_case["motoboys"], test_case["shops"])
    assert len(non_priority) == len_non_priority

@pytest.mark.parametrize("test_case_file", [
    "tests/test_cases/all_exclusives.json",
    "tests/test_cases/main_case.json",
    "tests/test_cases/more_shops_and_orders.json",
    "tests/test_cases/no_exclusives.json"
])
def test_filter_exclusives_shops_priorities(test_case_file):
    """
    Tests the shops priorities lists are correctly set
    """
    test_case = read_json(test_case_file)
    filter_exclusives(test_case["motoboys"], test_case["shops"])
    TestCase().assertDictEqual(test_case["shops"], test_case["shops_priorities"])

@pytest.mark.parametrize("test_case_file", [
    "tests/test_cases/all_exclusives.json",
    "tests/test_cases/main_case.json",
    "tests/test_cases/more_shops_and_orders.json",
    "tests/test_cases/no_exclusives.json"
])
def test_set_profits(test_case_file):
    """
    Test the profits are calculated and set correctly
    """
    test_case = read_json(test_case_file)
    non_priority = filter_exclusives(test_case["motoboys"], test_case["shops"])
    set_profits(test_case["motoboys"], test_case["shops"], non_priority)
    TestCase().assertDictEqual(test_case["motoboys"], test_case["motoboys_profits"])
