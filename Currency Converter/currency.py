"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Emily Shader
Date:   02/16/2025
"""

import introcs

APIKEY = 'RvZtN7MfH01FiCPs4PqWduKIjJbU9jOMfzqgQ0LvOiEe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """