#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# A simple addition operation test example
#
# This file contains a basic addition function
# and its unit test cases to demonstrate the basic usage of Python unit testing
#
# @filename   test_example.py
# @path       tests\test_example.py
# @project    PROJECT_NAME
# @encoding   utf-8
#
# @product    PyCharm
# @author     USER
# @email      EMAIL
# @time       2025/03/16 18:16
#
# @version    git
# @record     CURRENT_USER_NAME Create file.
#             CURRENT_USER_NAME Update header comment.
#             CURRENT_USER_NAME description
#
# @license    http://www.opensource.org/licenses/mit-license.html  MIT License
#
# @copyright  Copyright (c) 2025. All rights reserved.
#
#             This software, including its code, documentation, and related materials,
#             is protected by copyright law and international treaties.
#             Unauthorized use, reproduction, or distribution of any part of this software is prohibited.
#
#             ContentForge is a trademark of ContentForge.org.
#             All other trademarks and registered trademarks are the property of their respective owners.
#
#             For permissions, please contact ContentForge.org@hotmail.com.
# =============================================================================================================
from __future__ import print_function, unicode_literals

# =============================================================================================================
# Standard Python Imports
# =============================================================================================================
import unittest


# =============================================================================================================
# Function to be tested
# =============================================================================================================
def add(a, b):
    """
    Perform addition operation on two numbers

    Args:
        a: First number operand
        b: Second number operand

    Returns:
        The sum of the two numbers
    """
    return a + b


# =============================================================================================================
# Test Case Class
# =============================================================================================================
class ExampleTestCase(unittest.TestCase):
    """
    Test cases for the addition function

    This test class contains various test scenarios for the add() function, including:
    - Addition of positive numbers
    - Addition of negative numbers
    - Addition of mixed positive and negative numbers
    - Addition with zero
    """

    def test_add_positive_numbers(self):
        """
        Test addition of two positive numbers

        Test scenario:
            Input: 2 and 3
            Expected output: 5
        """
        # Call add function to calculate 2+3
        result = add(2, 3)
        # Verify if the result matches the expected value 5
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """
        Test addition of two negative numbers

        Test scenario:
            Input: -2 and -3
            Expected output: -5
        """
        # Call add function to calculate (-2)+(-3)
        result = add(-2, -3)
        # Verify if the result matches the expected value -5
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        """
        Test addition of a positive and a negative number

        Test scenario:
            Input: 10 and -3
            Expected output: 7
        """
        # Call add function to calculate 10+(-3)
        result = add(10, -3)
        # Verify if the result matches the expected value 7
        self.assertEqual(result, 7)

    def test_add_zero(self):
        """
        Test addition with zero

        Test scenario:
            Input: 0 and 5
            Expected output: 5
        """
        # Call add function to calculate 0+5
        result = add(0, 5)
        # Verify if the result matches the expected value 5
        self.assertEqual(result, 5)


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Execute unit tests when the script is run directly
    unittest.main()
