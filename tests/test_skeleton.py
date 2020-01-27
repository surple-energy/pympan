# -*- coding: utf-8 -*-

import pytest
from pympan.skeleton import calculate_check_digit, compare_check_digit

__author__ = "David Parr"
__copyright__ = "David Parr"
__license__ = "mit"

@pytest.fixture(name="full_mpans")
def fixture_full_mpans(request):
    """
    2100040568765	K06D00347
    2199989664882	208280757
    2199991213474	211047941
    2199991311162	211048796
    2199991380495	210201010
    2199991416557	E12Z040308
    2199991421273	E12Z092282
    2199991506077	211048777
    2199991538895	211049032
    """
    return "2110479412199991213474"

def test_calculate_check_digit():
    assert calculate_check_digit("210004056876") == 5
    assert calculate_check_digit("219998966488") == 2
    assert calculate_check_digit("219999121347") == 4
    assert calculate_check_digit("219999131116") == 2
    assert calculate_check_digit("219999138049") == 5
    assert calculate_check_digit("219999141655") == 7
    assert calculate_check_digit("219999142127") == 3
    assert calculate_check_digit("219999150607") == 7
    assert calculate_check_digit("219999153889") == 5

def test_compare_check_digit():
    assert compare_check_digit("2100040568765") == True
    assert compare_check_digit("2199989664882") == True
    assert compare_check_digit("2199991213474") == True
    assert compare_check_digit("2199991311162") == True
    assert compare_check_digit("2199991380495") == True
    assert compare_check_digit("2199991416557") == True
    assert compare_check_digit("2199991421273") == True
    assert compare_check_digit("2199991506077") == True
    assert compare_check_digit("2199991538895") == True
    assert compare_check_digit("2199991538894") == False

    
