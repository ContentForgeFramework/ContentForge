#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file is responsible for parsing environment-specific configuration files or data.
#
# The primary purpose of this file is to define functions and utilities for reading, parsing,
# and validating environment configuration data, enabling seamless integration with the environment management module.
#
# @filename   parser.py
# @path       vendor\contentforge\utils\env_manager\parser.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/11 00:00
#
# @version    git
# @record     2024/12/11 00:00 <Carl Chen> Create file.
#             2024/12/11 00:06 <Carl Chen> Update header comment.
#             CURRENT_USER_NAME description
#
# @license    http://www.opensource.org/licenses/mit-license.html  MIT License
#
# @copyright  Copyright (c) 2024. All rights reserved.
#
#             This software, including its code, documentation, and related materials,
#             is protected by copyright law and international treaties.
#             Unauthorized use, reproduction, or distribution of any part of this software is prohibited.
#
#             ContentForge is a trademark of ContentForge.org.
#             All other trademarks and registered trademarks are the property of their respective owners.
#
#             For permissions, please contact ContentForge.org@hotmail.com.
# ====================================================================================================================================================
from __future__ import print_function, unicode_literals

import logging

# =============================================================================================================
# Standard Python Imports
# =============================================================================================================
logging.basicConfig(level=logging.INFO)


def parse_value(value):
    """
    Parse a single value according to the defined rules.

    :param value: (str) A single value from the .env file.
    :return: (str | list) Cleaned value or list of values if commas are present.
    """
    if ',' in value:
        return [' '.join(v.strip().split()) for v in value.split(',')]

    return ' '.join(value.split()) if value else ""


def parse_file(data):
    """
    Parse the entire .env file and return a cleaned dictionary.
    
    :param data: (dict) The raw data from the .env file.
    
    :return: (dict | None) The cleaned environment configuration.
    
    """
    if not isinstance(data, dict):
        logging.error(f"Invalid data type: {type(data)}")
        return None
        
    return {k: parse_value(v) for k, v in data.items()}


def get_parse_value(key, data):
    """
    Get a parsed value from the environment configuration.

    :param key: (str) The key to retrieve from the environment configuration.
    :param data: (dict) The raw data from the .env file.
    
    :return: (str | list | None) The parsed value or list of values if commas are present.
    """
    if not isinstance(data, dict):
        logging.error(f"Invalid data type: {type(data)}")
        return None
        
    value = data.get(key)
    if value is None:
        logging.warning(f"Key '{key}' not found or has no value.")
        return None
    return parse_value(value)


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # This is the script entry point, but currently no specific logic is defined.
    # Add appropriate code here for testing or parsing configurations as needed.
    pass
