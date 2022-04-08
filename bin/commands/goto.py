from metadata import *
from commands.CMD import CMD

def goto(entry_id):
    if entry_id.isdigit:
        meta_dict["entry_num"] = entry_id
    else:
        meta_dict["entry_num"] = find_label(entry_id)

def goto_view(args):
    entry_id = args[2]
    goto(entry_id)

goto_cmd = CMD \
(
    'goto',
    'scr goto <entry_id>',
    'jumps to the given scriter entry',
    goto_view,
    [1],
)
