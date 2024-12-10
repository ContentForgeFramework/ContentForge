#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file is a sample example
#
# This file is a sample example of a command-line tool implemented using the Click library,
# which can interact with users through the command line and output greetings.
#
# @filename   example.py
# @path       vendor\contentforge\utils\command\example.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/8 01:03
#
# @version    git
# @record     2024/12/08 01:46 <Carl Chen> Create file.
#             2024/12/08 01:46 <Carl Chen> Update header comment.
#             2024/12/10 21:54 <Carl Chen> add debug mode
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

from contentforge.utils.command import pass_configurations


@click.command()
@click.option('--name', default='world', help='Name to greet')
@pass_configurations
def cli(configurations, name):
    """
    A sample command-line tool that outputs a greeting message.

    This tool allows users to interact through the command line and outputs a greeting message.
    
    Args: \n
        configurations (Configuration): The configuration object. It may include a debug mode flag.\n
        name (str): The name of the person to greet.

    Example Usage:\n
        py artisan example --name Alice

    Example Output:\n
        Hello, Alice!
    """
    debug = getattr(configurations, 'debug', False)
    
    if debug:
        click.secho("Example command is running in debug mode.", fg='yellow')
        
    click.echo(f"Hello, {name}!")


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Initialize this file and load the command
    pass
