# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for OrangePi 5

Usage:

.. code:: python
   import orangepi.pi5
   from OPi import GPIO

   GPIO.setmode(orangepi.pi5.BOARD) or GPIO.setmode(orangepi.pi5.BCM)
"""

# The Rockchip RK3399 GPIO has 5 banks, GPIO0 to GPIO4, each with 32 pins.
# Each bank is then divided into 4 parts with 8 pins each, labeled A through D (A=0, B=1, C=2, D=3)
# So, GPIO4_D5 is 4*32 + 3*8 + 5 = 157

# NanoPi M4 physical board pin to GPIO pin
BOARD = {
    2  : 47,
    3  : 46,
    4  : 54,
    14 : 131,
    15 : 132,
    17 : 138,
    18 : 29,
    27 : 139,
    22 : 28,
    23 : 59,
    24 : 58,
    10 : 49,
    9  : 48,
    25 : 92,
    11 : 50,
    8  : 52,
    7  : 35
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
