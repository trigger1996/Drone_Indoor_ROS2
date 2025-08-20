#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def print_c(text, color=None, bg_color=None, bold=False, underline=False):
    """
    打印彩色文本。

    参数:
        text (str): 要打印的文本。
        color (str): 文本颜色，可选值为：black, red, green, yellow, blue, magenta, cyan, white。
        bg_color (str): 背景颜色，可选值与color相同。
        bold (bool): 是否加粗。
        underline (bool): 是否加下划线。
    """
    # 颜色代码映射
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
    }
    # 背景颜色代码映射
    bg_colors = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
    }

    # 构建ANSI转义序列
    escape_seq = []
    if color and color in colors:
        escape_seq.append(colors[color])
    if bg_color and bg_color in bg_colors:
        escape_seq.append(bg_colors[bg_color])
    if bold:
        escape_seq.append('1')
    if underline:
        escape_seq.append('4')

    # 如果有样式设置，则添加ANSI转义序列
    if escape_seq:
        start = '\033[' + ';'.join(escape_seq) + 'm'
        end = '\033[0m'
        text = start + text + end

    # 打印文本
    print(text)

def format_logger(text, color=None, bg_color=None, styles=None):
    """
    支持彩色和多样式的终端格式化输出，用于 self.get_logger().info(...) 或 print。

    参数:
    - text (str/unicode): 显示的文字
    - color (str): 前景色名称，如 'red', 'bright_green'，默认None表示默认色
    - bg_color (str): 背景色名称，如 'bg_blue'，默认None表示无背景色
    - styles (str or list): 样式字符串或列表，如 'bold' 或 ['bold', 'underline']

    返回:
    - str: 带有 ANSI 转义序列的格式化字符串
    """
    # 处理 Unicode 输入（Python 2 兼容）
    if isinstance(text, unicode):
        text = text.encode('utf-8')
    if color and isinstance(color, unicode):
        color = color.encode('utf-8')
    if bg_color and isinstance(bg_color, unicode):
        bg_color = bg_color.encode('utf-8')

    # ANSI颜色代码
    fg_colors = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "bright_black": 90, "bright_red": 91, "bright_green": 92,
        "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
        "bright_cyan": 96, "bright_white": 97,
    }

    bg_colors = {
        "bg_black": 40, "bg_red": 41, "bg_green": 42, "bg_yellow": 43,
        "bg_blue": 44, "bg_magenta": 45, "bg_cyan": 46, "bg_white": 47,
        "bg_bright_black": 100, "bg_bright_red": 101, "bg_bright_green": 102,
        "bg_bright_yellow": 103, "bg_bright_blue": 104, "bg_bright_magenta": 105,
        "bg_bright_cyan": 106, "bg_bright_white": 107,
    }

    style_codes = {
        "bold": 1, "dim": 2, "italic": 3, "underline": 4,
        "blink": 5, "reverse": 7, "hidden": 8, "strikethrough": 9,
    }

    codes = []

    if color and color.lower() in fg_colors:
        codes.append(str(fg_colors[color.lower()]))

    if bg_color and bg_color.lower() in bg_colors:
        codes.append(str(bg_colors[bg_color.lower()]))

    if styles:
        if isinstance(styles, (str, unicode)):
            styles = [styles]
        for style in styles:
            if isinstance(style, unicode):
                style = style.encode('utf-8')
            if style.lower() in style_codes:
                codes.append(str(style_codes[style.lower()]))

    prefix = "\033[{}m".format(";".join(codes)) if codes else ""
    suffix = "\033[0m" if codes else ""
    return "{}{}{}".format(prefix, text, suffix)

