import os

from metadata import *
from commands.CMD import CMD

def init():
    if not os.path.isdir(meta_path):
        try:
            os.mkdir(meta_path)
        except OSError:
            err("Cannot Initialize Persistence")
    meta_dict["display_cmd"] = "cat"
    meta_dict["src_path"] = ""
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = 0
    meta_dict["source_cmd_path"] = \
        "%s/source_command_path"%(meta_path)

def init_view(args):
    init()
    view("initialized scriter (use 'scr help' for help)")

init_cmd = CMD \
(
    'init',
    'scr init',
    '(re)initializes scriter',
    init_view,
    [0],
)
