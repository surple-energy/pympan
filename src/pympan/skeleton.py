# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = pympan.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging

from pympan import __version__

__author__ = "David Parr"
__copyright__ = "David Parr"
__license__ = "mit"

def calculate_check_digit(mpan_unique: str) -> int:
    """Check MPAN digit.

    The final digit in the MPAN is the check digit, and validates the previous 12 (the core) using a modulus 11 test. The check digit is calculated thus:

    0. Multiply the first digit by 3
    0. Multiply the second digit by the next prime number (5)
    0. Repeat this for each digit (missing 11 out on the list of prime numbers for the purposes of this algorithm)
    0. Add up all these products
    0. The check digit is the sum modulo 11 modulo 10.

    Args:
      mpan -- The first 12 digits of the MPAN number, excluding the check digit.
    """
    check_digit = sum(prime * int(digit) for prime, digit in \
            zip([3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43], mpan_unique)) % 11 % 10

    return check_digit

def compare_check_digit(mpan_core: str) -> bool:
    """
    compare_check_digit [summary]
    
    :param mpan_core: [description]
    :type mpan_core: str
    :return: [description]
    :rtype: bool
    """

    n = len(mpan_core)

    if n != 13:
      print("`mpan_core` is not 13")

    else:
      check_digit = calculate_check_digit(mpan_core[0:12])
      if check_digit == int(mpan_core[12]):
        print("check digit checks out")
        check_response = True
      else:
        print("check your digits")
        check_response = False
    return check_response