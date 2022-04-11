from metadata import *
from commands.CMD import CMD

def status():
    return("display_cmd: %s\nsrc_path: %s\nAt entry_num: %s\nnum_entries: %s"%
           (meta_dict["preprocessor"],
            meta_dict["src_path"],
            meta_dict["entry_num"],
            meta_dict["num_entries"]))

def status_view(args):
    view(status())

status_cmd = CMD \
(
    'status',
    'scr status',
    'details scriter state',
    status_view,
    [0],
)
