from metadata import *
from commands.CMD import CMD

def status_model():
    return("display_cmd: %s\nsrc_path: %s\nAt entry_num: %s\nnum_entries: %s"%
           (meta_dict["display_cmd"],
            meta_dict["src_path"],
            meta_dict["entry_num"],
            meta_dict["num_entries"]))

def status_view(args):
    assert len(args) == 2
    view(status_model())

status = CMD \
(
    'status',
    'scr status',
    'details scriter state',
    status_model,
    status_view,
)
