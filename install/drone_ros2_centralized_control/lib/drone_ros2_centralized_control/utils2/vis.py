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

def format_logger(text, color=None, bg_color=None, styles=None):
    """
    支持彩色和多样式的终端格式化输出。
    
    参数:
    - text: 显示的文字
    - color: 前景色名称，如 'red'
    - bg_color: 背景色名称，如 'bg_blue'
    - styles: 样式列表，如 ['bold', 'underline']
    """
    color_codes = {
        'black': '30', 'red': '31', 'green': '32', 'yellow': '33',
        'blue': '34', 'magenta': '35', 'cyan': '36', 'white': '37'
    }

    bg_color_codes = {
        'bg_black': '40', 'bg_red': '41', 'bg_green': '42', 'bg_yellow': '43',
        'bg_blue': '44', 'bg_magenta': '45', 'bg_cyan': '46', 'bg_white': '47'
    }

    style_codes = {
        'bold': '1',  'dim': '2',     'italic' : '3', 'underline': '4',
        'blink': '5', 'reverse': '7', 'hidden' : '8', 'strikethrough': '9'
    }


    codes = []

    if color in color_codes:
        codes.append(color_codes[color])
    if bg_color in bg_color_codes:
        codes.append(bg_color_codes[bg_color])
    if styles:
        for style in styles:
            if style in style_codes:
                codes.append(style_codes[style])

    if codes:
        prefix = f"\033[{';'.join(codes)}m"
        suffix = "\033[0m"
        return f"{prefix}{text}{suffix}"
    else:
        return text
