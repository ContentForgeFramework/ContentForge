#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
#
# This file is part of the ContentForge project.
#
# This file defines the command-line interface (CLI) entry point and loads related commands for the ContentForge project.
#
# @filename   __init__.py
# @path       vendor\contentforge\utils\command\__init__.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/8 00:54
#
# @version    git
# @record     2024/12/8 1:18 <Carl Chen> Create file.
#             2024/12/8 1:18 <Carl Chen> Update header comment.
#             2024/12/10 21:39 <Carl Chen>  add configuration class and pass_configurations decorator
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
import click


class Configuration(object):
    """
    store the configuration information
    """
    
    def __init__(self, debug, *args, **kwargs):
        """
        Initial the configuration object
        :param debug: debug flag, open debug mode if True
        :param args: positional arguments
        :param kwargs: keyword arguments
        """
        self.debug = debug
        self.args = args
        self.kwargs = kwargs


# pass the configuration object to the command
pass_configurations = click.make_pass_decorator(Configuration, ensure=True)

# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Initialize the command package and load the commands
    pass
