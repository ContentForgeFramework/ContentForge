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
from contentforge.utils.env_manager.validator import validate_env

# get the project root directory
_project_root = Path(os.getenv('PROJECT_ROOT', Path(__file__).resolve().parents[4]))


def get_project_paths():
    """
    Retrieve project path information.

    :return: dict containing project root, environment file paths, etc.
    """
    return {'project_root': _project_root, 'env_file': _project_root / '.env',
            'env_example_file': _project_root / '.env.example',
            'app_dir': _project_root / 'app', }


@click.command()
@click.option('--init', '-i', is_flag=True, help='Initialize the environment file.')
@click.option('--delete', '-d', is_flag=True, help='Delete the environment file.')
@click.option('--clean', '-c', is_flag=True, help='Clean the environment.')
@click.option('--validate', '-v', is_flag=True, help='Validate the environment file.')
@pass_configurations
def cli(configurations, init, delete, clean, validate):
    """
    CLI entry point for environment-related operations.

    :param configurations: (Configurations): Configuration object.
    :param init: (bool): Initialize the environment.
    :param delete: (bool): Delete the environment file.
    :param clean: (bool): Clean the environment.
    :param validate: (bool): Validate the environment file.
    """
    debug = getattr(configurations, 'debug', False)
    
    if debug:
        click.secho('Open debug mode on env command', fg='yellow')
    
    paths = get_project_paths()
    
    if init:
        _init_env(paths, debug)
    
    if delete:
        _delete_env(paths, debug)
    
    if clean:
        clean_env(paths, debug)
        
    if validate:
        _validate_env(paths, debug)


def clean_env(paths, debug):
    """
    Clean the environment by removing cache files and temporary directories.

    :param paths: (dict): Dictionary containing path information.
    :param debug: (bool): Debug mode.
    """
    click.secho('Cleaning the environment...', fg='green')
    app_dir = paths['app_dir']
    
    if debug:
        click.secho(f"   App directory: {app_dir}", fg='yellow')
    
    # remove cache files
    for file in app_dir.rglob('*.py[cod]'):
        try:
            file.unlink()
            
            if debug:
                click.secho(f"   Removed file: {file}", fg='green')
                
        except Exception as ex:
            click.secho(f"   Failed to remove {file}: {ex}", fg='red')
    
    # remove cache directories
    for pycache in app_dir.rglob('__pycache__'):
        try:
            pycache.rmdir()
            
            if debug:
                click.secho(f"   Removed directory: {pycache}", fg='green')
                
        except Exception as ex:
            click.secho(f"   Failed to remove {pycache}: {ex}", fg='red')


def _init_env(paths, debug):
    """
    Initialize the environment by copying the `.env.example` file to `.env`.

    :param paths: (dict): Dictionary containing path information.
    :param debug: (bool): Debug mode.
    """
    click.secho('Initializing the environment...', fg='green')
    
    try:
        env_example_file = paths['env_example_file']
        env_file = paths['env_file']
        
        if debug:
            click.secho(f"   Environment example file: {env_example_file}", fg='yellow')
            click.secho(f"   Target environment file: {env_file}", fg='yellow')
        
        data = env_example_file.read_text()
        env_file.write_text(data)
        
        click.secho('   Environment initialized successfully.', fg='green')
    
    except Exception as ex:
        click.secho(f"   Failed to initialize environment: {ex}", fg='red')


def _delete_env(paths, debug):
    """
    Delete the `.env` file.

    :param paths: (dict): Dictionary containing path information.
    :param debug: (bool): Debug mode.
    """
    click.secho('Deleting the environment...', fg='green')
    
    env_file = paths['env_file']
    
    if debug:
        click.secho(f"   Target environment file: {env_file}", fg='yellow')
    
    # double-check with the user
    if not click.confirm('Are you sure you want to delete the .env file?', default=False):
        click.secho('   Operation cancelled.', fg='yellow')
        return
    
    # delete the environment file
    try:
        env_file.unlink()
        click.secho('   Environment file deleted successfully.', fg='green')
    
    except Exception as ex:
        click.secho(f"   Failed to delete environment file: {ex}", fg='red')


def _validate_env(paths, debug):
    """
    Validate the environment by checking for required settings.

    :param paths: (dict): Dictionary containing path information.
    :param debug: (bool): Debug mode.
    """
    click.secho('Validating the environment...\n', fg='green')

    env_file = paths['env_file']
    example_file = paths['env_example_file']

    if debug:
        click.secho(f"   Environment file: {env_file}", fg='yellow')
        click.secho(f"   Environment example file: {example_file}", fg='yellow')

    if not env_file.exists():
        click.secho("Missing .env file.", fg="red")
        return

    if not example_file.exists():
        click.secho("Missing .env.example file.", fg="red")
        return

    result = validate_env(str(env_file), str(example_file))

    if result['missing']:
        click.secho(f"  Missing keys: {', '.join(result['missing'])}\n", fg="red")

    if result['extra']:
        click.secho(f"    Extra keys: {', '.join(result['extra'])}\n", fg="yellow")

    if result['mismatched']:
        for mismatch in result['mismatched']:
            click.secho(f"Mismatched key: {mismatch['key']}", fg="red")
            click.secho(f"      - Actual: {mismatch['actual']}", fg="cyan")
            click.secho(f"    - Expected: {mismatch['expected'] if mismatch['expected'] and mismatch['expected'].strip() else 'None'}\n", fg="yellow")
            
    if not result['missing'] and not result['extra'] and not result['mismatched']:
        click.secho("Environment file is valid.", fg="green")

    
# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    pass
