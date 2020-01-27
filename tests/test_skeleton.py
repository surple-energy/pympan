# -*- coding: utf-8 -*-

import pytest
from pympan.skeleton import check_digit

__author__ = "David Parr"
__copyright__ = "David Parr"
__license__ = "mit"

def test_check_digit():
    assert check_digit("210004056876") == 5
    assert check_digit("219998966488") == 2
    assert check_digit("219999121347") == 4
    assert check_digit("219999131116") == 2
    assert check_digit("219999138049") == 5
    assert check_digit("219999141655") == 7
    assert check_digit("219999142127") == 3
    assert check_digit("219999150607") == 7
    assert check_digit("219999153889") == 5

    
