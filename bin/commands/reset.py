from metadata import *
from commands.CMD import CMD

def get_num_entries(src_path):
    """
    Returns the number of scriter entries in a file.
    """
    src = open(src_path, 'r')
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

def reset_model():
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(meta_dict["src_path"])

def reset_view(args):
    assert len(args) == 2
    reset_model()
    view("reset %s"%(meta_dict["src_path"]))

reset = CMD \
(
    'reset',
    'scr reset',
    'resets scriter to the first entry',
    reset_model,
    reset_view,
)
