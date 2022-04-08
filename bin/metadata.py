import os, shutil

from serial_dict import serial_dict
from cmd_view import cmd_view

ENTRY_PREFIX = "#"

home_path = os.environ["HOME"]
meta_path = os.path.join(home_path, ".scriter/")
meta_dict = serial_dict(meta_path)

def initialized():
    """
    Returns if the scriter HOME directory exists.
    """
    return os.path.exists(meta_path)

def view(text):
    """
    use the preprocessor to write to the 'source' file
    """
    if meta_dict.contains_key("display_cmd"):
        display_cmd = meta_dict["display_cmd"]
    else:
        display_cmd = 'cat'
    cmd_view(display_cmd, text)

def err(msg):
    """
    Displays the error message and exits.
    """
    view(msg)
    exit()

def remove(path):
    """
    Removes the subtree of directories rooted at path.
    """
    if os.path.exists(path):  
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)

def get_num_entries(src_path):
    """
    Returns the number of scriter entries in a file.
    """
    try:
        src = open(src_path, 'r')
    except IOError:
        err("src_path could not be opened")        
    num_entries = 1
    while True:
        try:
            line = next(src)
            search_str = "%s"%(ENTRY_PREFIX)
            if line[:len(search_str)] == search_str:
                num_entries += 1
        except StopIteration:
            break
    return num_entries

def set_entry_num(entry_num):
    """
    Sets the current entry num (with bounds check).
    """
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num
