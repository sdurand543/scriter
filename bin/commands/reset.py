from metadata import *
from commands.CMD import CMD

def reset():
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(meta_dict["src_path"])

def reset_view(args):
    reset()
    view("reset %s"%(meta_dict["src_path"]))

reset_cmd = CMD \
(
    'reset',
    'scr reset',
    'resets scriter to the first entry',
    reset_view,
    [0],
)
