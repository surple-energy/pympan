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


from pympan import __version__

__author__ = "David Parr"
__copyright__ = "David Parr"
__license__ = "mit"

PROFILE_CLASSES = {
    "00":	"Half-hourly supply (import and export)",
    "01":	"Domestic unrestricted",
    "02":	"Domestic Economy meter of two or more rates",
    "03":	"Non-domestic unrestricted",
    "04":	"Non-domestic Economy 7",
    "05":	"Non-domestic, with maximum demand (MD) recording capability and with load factor (LF) less than or equal to 20%",
    "06":	"Non-domestic, with MD recording capability and with LF less than or equal to 30% and greater than 20%",
    "07":	"Non-domestic, with MD recording capability and with LF less than or equal to 40% and greater than 30%",
    "08":	"Non-domestic, with MD recording capability and with LF greater than 40% (also all non-half-hourly export MSIDs)"
}

METER_TIME_SWITCH_CODES = {
    ("001", "399"): "DNO specific",
    ("400", "499"): "Reserved",
    ("500", "509"): "Codes for related Metering Systems – common across the Industry",
    ("510", "799"): "Codes for related Metering Systems – DNO specific",
    ("800", "999"): "Codes common across the Industry"
}

DISTRIBUTOR_IDS = {
    "10":	"UK Power Networks",
    "11":	"Western Power Distribution",
    "12":	"UK Power Networks",
    "13":	"SP Energy Networks",
    "14":	"Western Power Distribution",
    "15":	"Northern Powergrid",
    "16":	"Electricity North West",
    "17":	"Scottish & Southern Electricity Networks",
    "18":	"SP Energy Networks",
    "19":	"UK Power Networks",
    "20":	"Scottish & Southern Electricity Networks",
    "21":	"Western Power Distribution",
    "22":	"Western Power Distribution",
    "23":	"Northern Powergrid"
}

def parse_top_line(top_line: str) -> dict:
    meter_time_switch_code = top_line[2:5]

    for low, high in METER_TIME_SWITCH_CODES.keys():
      if int(low) <= int(meter_time_switch_code) <= int(high):
          meter_time_switch = METER_TIME_SWITCH_CODES[(low, high)]

    top_line_parsed = {
        "profile_class": top_line[0:2],
        "profile": PROFILE_CLASSES[top_line[0:2]],
        "meter_time_switch_code": meter_time_switch_code,
        "meter_time_switch": meter_time_switch,
        "line_loss_factor": top_line[5:8]
    }
    return top_line_parsed

def parse_bottom_line(bottom_line: str) -> dict:
    bottom_line_parsed = {
        "distributor_id": bottom_line[0:2],
        "distributor": DISTRIBUTOR_IDS[bottom_line[0:2]],
        "unique_identifier": bottom_line[0:12],
        "calculate_check_digit": bottom_line[12],
    }
    return bottom_line_parsed

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
    check_digit = calculate_check_digit(mpan_core[0:12])
    if check_digit == int(mpan_core[12]):
        print("check digit checks out")
        check_response = True
    else:
        print("check your digits")
        check_response = False
    return check_response
