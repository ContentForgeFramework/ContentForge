#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# 此文件是一个示例脚本，展示如何定义一个简单的命令行工具
#
# 该文件包含一个使用 Click 库实现的命令行工具示例，能够通过命令行与用户交互并输出问候语。
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
# @record     2024/12/8 1:46 <Carl Chen> Create file.
#             2024/12/8 1:46 <Carl Chen> Update header comment.
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


@click.command()
@click.option('--name', default='world', help='Name to greet')
def cli(name):
    """
    一个简单的示例命令行工具。

    该工具接收一个可选参数 `--name`，用于生成问候语并在终端中输出。

    参数:
        name (str): 要问候的名字，默认为 'world'。

    示例用法:
        python example.py --name Alice
    输出:
        Hello, Alice!
    """
    click.echo(f"Hello, {name}!")


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    # 如果直接运行该脚本，不执行命令，仅作为模块存在时供外部调用。
    pass
