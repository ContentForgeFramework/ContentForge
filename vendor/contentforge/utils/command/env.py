#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# Environment commands script.
#
# This script provides a command-line interface (CLI) for initializing the environment for the project. It includes
# functionality for copying configuration template files to their working counterparts and ensures necessary
# setup steps are performed.
# 
# @filename   env.py
# @path       vendor\contentforge\utils\command\env.py
# @project    ContentForge
# @encoding   utf-8
# 
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/10 22:16
# 
# @version    git
# @record     2024/12/10 23:08 <Carl Chen> Create file.
#             2024/12/10 23:08 <Carl Chen> Update header comment.
#             2024/12/10 23:08 <Carl Chen> add init_env function.
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
from pathlib import Path

import click

from contentforge.utils.command import pass_configurations


@click.command()
@click.option('--init', '-i', is_flag=True, help='Initialize the environment.')
@pass_configurations
def cli(configurations, init):
    """
    CLI entry point for initializing the environment.
    
    :param configurations: (Configurations): Configurations object.\n
    :param init: (bool): Initialize the environment.\n
    """
    debug = getattr(configurations, 'debug', False)
    
    if debug:
        click.secho('Open debug mode on env:init.', fg='yellow')
    
    if init:
        _init_env(debug)


def _init_env(debug):
    """
    Initialize the environment by copying .env.example to .env.
    This function is intended for internal use only.
    
    :param debug: (bool): Debug mode.
    """
    click.secho('Initializing the environment...', fg='green')
    
    # get the project root directory
    project_root = Path(os.getenv('PROJECT_ROOT', Path(__file__).resolve().parents[4]))
    
    # source file path
    env_example_file = project_root / '.env.example'
    
    # target file path
    env_file = project_root / '.env'
    
    if debug:
        click.secho('   Project root directory: {}'.format(project_root), fg='yellow')
        click.secho('   Environment example file: {}'.format(env_example_file), fg='yellow')
    
    try:
        # Read and copy the .env.example file
        data = env_example_file.read_text()
        env_file.write_text(data)
        
        click.secho('Environment initialized successfully.', fg='green')
    
    except FileNotFoundError:
        click.secho('Environment example file not found.', fg='red')
    
    except PermissionError:
        click.secho('Permission denied when accessing files.', fg='red')
    
    except IOError as io_err:
        click.secho('An IO error occurred: {}'.format(io_err), fg='red')
    
    except Exception as ex:
        click.secho('An unexpected error occurred: {}'.format(ex), fg='red')


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    pass
