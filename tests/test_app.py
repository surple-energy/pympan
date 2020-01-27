# -*- coding: utf-8 -*-

import pytest
from pympan.app import parse_top_line, parse_bottom_line, calculate_check_digit, compare_check_digit

__author__ = "David Parr"
__copyright__ = "David Parr"
__license__ = "mit"

@pytest.fixture(name="left_letter")
def fixture_left_letter():
    return "S"

@pytest.fixture(name="top_line")
def fixture_top_line():
    return "01801100"

@pytest.fixture(name="bottom_line")
def fixture_bottom_line():
    return "2199992801200"
  

def test_parse_top_line(top_line):
    top_line = parse_top_line(top_line)
    assert isinstance(top_line, dict)
    assert top_line["profile_class"] =="01"
    assert top_line["profile"] == "Domestic unrestricted"
    assert top_line["meter_time_switch_code"] == "801"
    assert top_line["line_loss_factor"] == "100"

def test_parse_bottom_line(bottom_line):
    bottom_line = parse_bottom_line(bottom_line)
    assert isinstance(bottom_line, dict)
    assert bottom_line["distributor_id"] == "21"
    assert bottom_line["distributor"] == "Western Power Distribution"
    assert bottom_line["unique_identifier"] == "219999280120"
    assert bottom_line["calculate_check_digit"] == "0"

def test_calculate_check_digit():
    assert calculate_check_digit("219999280120") == 0

def test_compare_check_digit(bottom_line):
    assert compare_check_digit(bottom_line)
    assert not compare_check_digit("2199992801201")

