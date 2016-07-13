__author__ = 'tomek'
import os
from settings.settings import *

def is_file_exists(file_name):
    return os.path.isfile(file_name)

def delete_file(file_name):
    if is_file_exists(file_name):
        os.remove(file_name)

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def decode_and_replace_polish_chars(string):
    string = string.decode('utf8')
    return_string = ""
    for c in string:
        if c in POLISH_CHARS:
            return_string += POLISH_CHARS[c]
        else:
            return_string += c
    return return_string

def get_substring(html, prefix, last_char):
    p = html.index(prefix) + len(prefix)
    loop = True
    last_index = 0
    while loop:
        last_index += 1
        ch = html[p + last_index]
        if ch == last_char:
            loop = False
    return html[p: (p + last_index)]