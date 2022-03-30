import os

from metadata import *
from commands.CMD import CMD

def init_model():
    if not os.path.isdir(meta_path):
        try:
            os.mkdir(meta_path)
        except OSError:
            return "Cannot Initialize Persistence"
        meta_dict["display_cmd"] = "cat"
        meta_dict["src_path"] = ""
        meta_dict["entry_num"] = 0
        meta_dict["num_entries"] = 0

def init_view(args):
    assert(len(args)) == 2
    init_model()
    view("initialized scriter (use scr.help for help)")

init = CMD \
(
    'init',
    'scr init',
    '(re)initializes scriter',
    init_model,
    init_view,
)
