#!/usr/bin/env python2
# -*- coding: utf-8 -*-

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