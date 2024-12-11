#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file is responsible for writing environment-specific configurations or data to appropriate storage.
#
# The primary purpose of this file is to define functions and utilities for creating, updating, and saving
# configuration data for the environment management module, ensuring data persistence and consistency.
#
# @filename   writer.py
# @path       vendor\contentforge\utils\env_manager\writer.py
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
#             2024/12/11 00:08 <Carl Chen> Update header comment.
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
import logging
import os

from pathlib import Path
from dotenv import dotenv_values, set_key

# set logging level
logging.basicConfig(level=logging.INFO)

# get the project root directory
_project_root = Path(__file__).resolve().parents[4]
_project_path = os.path.join(_project_root, '.env')


def write_key_value(key, value=None):
    """
    Write Environment Configuration

    This function writes or updates the environment configuration to the .env file. If `value` is `None`,
    the key will be written with an empty value.
    
    :param key: (str) - The key to write to the configuration file.
    :param value: (str | None) - The value to write to the configuration file. If None, the key will be written with an empty value.


    :return: (bool) - True if the operation was successful (key written or deleted).
                      False if the operation failed or the key was not found (in delete_key).

    """
    if not key:
        logging.error("The 'key' must be provided.")
        return False
    
    try:
        set_key(_project_path, key, value)
        return True
    
    except FileNotFoundError as file_not_found_err:
        logging.error(f'Error writing configuration: {file_not_found_err}')
        return False
    
    except PermissionError as permission_err:
        logging.error(f'Error writing configuration: {permission_err}')
        return False
    
    except IOError as io_err:
        logging.error(f'Error writing configuration: {io_err}')
        return False
    
    except Exception as e:
        logging.error(f'Error writing configuration: {e}')
        return False


def delete_key(key):
    """
    Delete Environment

    This function deletes the environment configuration from the .env file in the project root directory.
    
    :param key: (str) - The key to delete from the configuration file.

    :return: (bool) - True if the configuration was successfully deleted, False otherwise.
    """
    
    try:
        env_data = dotenv_values(_project_path)
        
        if key in env_data:
            env_data.pop(key)
            
            with open(_project_path, 'w') as file:
                for k, v in env_data.items():
                    file.write(f'{k}={v}\n')
            logging.info(f"Key '{key}' successfully deleted.")
            return True
        else:
            logging.warning(f"Key '{key}' not found in the .env file.")
            return False
    
    except FileNotFoundError as file_not_found_err:
        logging.error(f'Error writing configuration: {file_not_found_err}')
        return False
    
    except PermissionError as permission_err:
        logging.error(f'Error writing configuration: {permission_err}')
        return False
    
    except IOError as io_err:
        logging.error(f'Error writing configuration: {io_err}')
        return False
    
    except Exception as e:
        logging.error(f'Error writing configuration: {e}')
        return False


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # This is the script entry point, but currently no specific logic is defined.
    # Add appropriate code here for testing or writing configurations as needed.
    pass
