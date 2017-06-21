# -*- coding: utf-8 -*-


import re

def remove_color_code(msg):
    """ remove the color code part in command response.
    """
    return re.sub("\033\[[0-9;]*m", "", msg)