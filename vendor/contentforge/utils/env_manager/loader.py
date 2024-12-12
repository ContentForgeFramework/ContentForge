#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file serves as the loader for the environment management module.
#
# The primary purpose of this file is to handle the loading of environment-specific configurations,
# such as parsing configuration files, setting up environment variables, or initializing related components.
#
# @filename   loader.py
# @path       vendor\contentforge\utils\env_manager\loader.py
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
#             2024/12/11 00:05 <Carl Chen> Update header comment.
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

# =============================================================================================================
# Standard Python Imports
# =============================================================================================================
import os
import logging
from pathlib import Path

from dotenv import dotenv_values

# Set up logging
logging.basicConfig(level=logging.INFO)

# get the project root directory
_project_root = Path(__file__).resolve().parents[4]
_project_path = os.path.join(_project_root, '.env')


def load_env(path=_project_path):
    """
    Load Environment

    This function reads the environment configuration from the .env file in the project root directory.

    :return: (dict) - The environment configuration, or an error message if the file is not found.
    """
    # output the path for debugging
    # print(_pyproject_path)
    
    if not os.path.exists(path):
        logging.error(f"File {path} not found or inaccessible.")
        return None
    
    # use dotenv to load the .env file
    try:
        env_config = dotenv_values(path)
        return env_config
    
    except Exception as e:
        logging.error(f"Error loading .env file: {e}")
        return None


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # This is the script entry point, but no specific logic is currently defined.
    # Add appropriate code here for testing or loading configurations if needed.
    pass
