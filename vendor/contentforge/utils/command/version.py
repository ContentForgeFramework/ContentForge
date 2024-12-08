#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================================================================================================================
# 
# 该文件用于提取项目版本信息，特别是从 pyproject.toml 文件中读取版本号。
#
# 该文件通过解析 pyproject.toml 中的内容，提取版本信息，便于在项目中动态管理和引用版本号。
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
    提取项目版本号。

    从项目根目录中的 pyproject.toml 文件中读取版本号。如果文件不存在或解析失败，将返回适当的错误信息。

    :return: str 包含版本号信息的字符串，如果无法读取则返回错误提示。
    """
    # 获取项目根目录
    project_root = Path(__file__).resolve().parents[4]
    pyproject_path = os.path.join(project_root, 'pyproject.toml')
    
    # 输出路径以供debug
    # print(pyproject_path)
    
    try:
        # 使用 toml 库加载 pyproject.toml
        if os.path.exists(pyproject_path):
            data = toml.load(pyproject_path)
            # 从工具节点中获取 Poetry 的版本信息
            project_version = data.get('tool', {}).get('poetry', {}).get('version', 'Unknown')
            return f"version: {project_version}"
        else:
            # 如果文件不存在，返回提示
            return "pyproject.toml not found, version is unknown!"
    except Exception as e:
        # 捕获异常并返回错误信息
        return f"An error occurred: {e}"
        

# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == '__main__':
    get_version()
