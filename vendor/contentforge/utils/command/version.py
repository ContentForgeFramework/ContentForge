#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file is a utility script that extracts version information from the pyproject.toml file.
#
# This script is used to extract the version information from the pyproject.toml file in the project root directory.
# 
# @filename   version.py
# @path       vendor\contentforge\utils\command\version.py
# @project    ContentForge
# @encoding   utf-8
# 
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/8 21:14
# 
# @version    git
# @record     2024/12/8 21:54 <Carl Chen> Create file.
#             2024/12/8 21:54 <Carl Chen> Update header comment.
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
import toml
from pathlib import Path


def get_version():
    """
    Extracts version

    This function reads the version information from the pyproject.toml file in the project root directory.

    :return: (str) - The version information, or an error message if the file is not found.
    """
    # get the project root directory
    project_root = Path(__file__).resolve().parents[4]
    pyproject_path = os.path.join(project_root, 'pyproject.toml')
    
    # output the path for debugging
    # print(pyproject_path)
    
    try:
        # use toml to load the pyproject.toml file
        if os.path.exists(pyproject_path):
            
            data = toml.load(pyproject_path)
            
            # extract the version information from tool.poetry
            project_version = data.get('tool', {}).get('poetry', {}).get('version', 'Unknown')
            return f"version: {project_version}"
        else:
            # if the file is not found, return an error message
            return "pyproject.toml not found, version is unknown!"
    except Exception as e:
        # if an error occurs, return an error message
        return f"An error occurred: {e}"
        

# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    get_version()
