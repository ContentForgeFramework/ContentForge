#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# This file defines the command-line interface (CLI) entry point and loads related commands for the ContentForge project.
#
# Responsibilities:
# 1. Set up the CLI entry point.
# 2. Dynamically load commands from the `contentforge.utils.command` module.
#
# @filename   artisan.py
# @path       artisan.py
# @project    ContentForge
# @encoding   utf-8
#
# @product    PyCharm
# @author     Carl Chen
# @email      mailto:ContentForge.org@hotmail.com
# @time       2024/12/8 00:57
#
# @version    git
# @record     2024/12/8 0:57 <Carl Chen> Create file.
#             2024/12/8 0:57 <Carl Chen> Update header comment.
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
import importlib
import os
import pkgutil
import sys

import click

# Get the current directory of the file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the vendor directory to sys.path
sys.path.insert(0, os.path.join(current_dir, 'vendor'))

# Import the contentforge.utils command module
from contentforge.utils import command


@click.group(invoke_without_command=True)
@click.option('--version', '-v', is_flag=True, help="Get the contentforge framework version")
@click.pass_context
def cli(ctx, version):
    """
    ContentForge Command-Line Tool

    This tool is used to execute various commands in the ContentForge project.

    Example usage:
        python artisan <command> [options]
    """

    if version:
        # Import the version command
        from contentforge.utils.command import version
        
        msg = version.get_version()
        click.echo(msg)
        ctx.exit()
    
    if ctx.invoked_subcommand is None:
        
        if help:
            # Print the help message
            click.secho(ctx.get_help(), fg="green")
            ctx.exit()
        else:
            # Print an error message and exit with a non-zero status code
            click.secho("No command provided. Use 'python artisan --help' to see available commands.", fg="red", bold=True, err=True)
            ctx.exit(1)


def load_commands():
    """
    Dynamically load commands from the contentforge.utils.command module.

    This function iterates through all the modules in the command package, checking if each module contains a
    'cli' command. If present, the command is added to the main CLI entry point. This ensures that all command
    modules defined in contentforge.utils.command are automatically loaded into the CLI.
    """
    for _, module_name, _ in pkgutil.iter_modules(command.__path__):
        try:
            # Dynamically load the module
            module = importlib.import_module(f"vendor.contentforge.utils.command.{module_name}")
            # Add the 'cli' command to the CLI if it exists in the module
            if hasattr(module, 'cli'):
                cli.add_command(module.cli, name=module_name)
                
        except ModuleNotFoundError as mnf_err:
            # Print an error message if the module is not found
            print(f"ModuleNotFoundError: '{module_name}': {mnf_err}")
            sys.exit(1)
            
        except ImportError as im_err:
            # Print an error message if the module cannot be imported
            print(f"An error occurred while importing module '{module_name}': {im_err}")
            sys.exit(1)
            
        except Exception as ex:
            # Print an error message if the module cannot be loaded
            print(f"An error occurred while loading module '{module_name}': {ex}")
            sys.exit(1)


# Call the function to load commands
load_commands()

# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # Execute the command-line tool
    cli()
