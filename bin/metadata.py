import os

from serial_dict import serial_dict
from cmd_view import cmd_view

ENTRY_PREFIX = "#"

home_path = os.environ["HOME"]
meta_path = os.path.join(home_path, ".scriter/")
meta_dict = serial_dict(meta_path)

def view(text):
    """
    stdout the display_cmd on the given input
    """
    if meta_dict.contains_key("display_cmd"):
        display_cmd = meta_dict["display_cmd"]
    else:
        display_cmd = 'cat'
    cmd_view(display_cmd, text);
