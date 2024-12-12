#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file is responsible for validating environment-specific configurations or data.
#
# The primary purpose of this file is to define functions and utilities for verifying the correctness,
# consistency, and completeness of environment configuration data, ensuring reliable operations within the environment management module.
#
# @filename   validator.py
# @path       vendor\contentforge\utils\env_manager\validator.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/11 00:01
#
# @version    git
# @record     2024/12/11 00:01 <Carl Chen> Create file.
#             2024/12/11 00:07 <Carl Chen> Update header comment.
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
from contentforge.utils.env_manager.loader import load_env

# Set up logging
logging.basicConfig(level=logging.INFO)


def validate_env(env_file_path, example_file_path):
    """
    Validate Environment

    This function verifies the environment configuration data to ensure that all required settings are present,
    and that the data is consistent and correct.

    :param env_file_path: (str) - The path to the environment configuration file.
    :param example_file_path: (str) - The path to the example environment configuration file.
    :return: (dict) - A dictionary containing details of missing, extra, and mismatched settings.
    """
    try:
        # Load the environment configuration data
        env_data = load_env(env_file_path)
        example_data = load_env(example_file_path)
        
        if env_data is None or example_data is None:
            logging.warning("One of the environment files could not be loaded. Returning empty results.")
            return {
                "missing": [],
                "extra": [],
                "mismatched": [],
            }
        
        # Check for missing, extra, and mismatched settings
        missing_settings = []
        extra_settings = []
        mismatched_settings = []
        
        for key in example_data:
            if key not in env_data:
                missing_settings.append(key)
            elif env_data[key] != example_data[key]:
                mismatched_settings.append({
                    "key": key,
                    "actual": env_data[key],
                    "expected": example_data[key],
                })
        
        for key in env_data:
            if key not in example_data:
                extra_settings.append(key)
        
        # Return the validation results
        return {
            "missing": missing_settings,
            "extra": extra_settings,
            "mismatched": mismatched_settings,
        }
    except Exception as ex:
        logging.error(f"Error validating environment: {ex}")
        return {
            "missing": [],
            "extra": [],
            "mismatched": [],
        }


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # This is the script entry point, but currently no specific logic is defined.
    # Add appropriate code here for testing or validating configurations as needed.
    pass
