from metadata import *
from commands.CMD import CMD

def goto_model(entry_id):
    if entry_id.isdigit:
        meta_dict["entry_num"] = entry_id
    else:
        meta_dict["entry_num"] = find_label(entry_id)

def goto_view(args):
    assert(len(args)) == 3
    entry_id = args[2]
    goto_model(entry_id)

goto = CMD \
(
    'goto',
    'scr goto <entry_id>',
    'jumps to the given scriter entry',
    goto_model,
    goto_view,
)
