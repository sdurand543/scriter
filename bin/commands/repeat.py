from metadata import *
from commands.CMD import CMD

def repeat_model():
    src_path = meta_dict["src_path"]
    try:
        src = open(src_path, 'r')
    except IOError:
        return "src_path could not be opened"
    entry_num = int(meta_dict["entry_num"])
    
    if entry_num == 0:
        return "Start of File"
    
    if entry_num == int(meta_dict["num_entries"]):
        return "End of File"
    
    # goto entry
    line = ""
    iter_entry_num = 0
    while iter_entry_num < entry_num:
        search_str = "%s"%(ENTRY_PREFIX)    
        try:
            line = next(src)
            if line[:len(search_str)] == search_str:
                iter_entry_num += 1
        except StopIteration:
            return "File Modified Since Use"
    
    # proceed to next line
    try:
        line = next(src)
    except StopIteration:
        return ""

    # go until next entry_num
    entry = ""    
    search_str = "%s"%(ENTRY_PREFIX)
    while line[:len(search_str)] != search_str:
        entry += line
        try:
            line = next(src)
        except StopIteration:
            break

    # return entry
    src.close()
    return entry.strip()

def repeat_view(args):
    assert(len(args)) == 2
    view(repeat_model())

repeat = CMD \
(
    'repeat',
    'scr rep',
    'repeats the current scriter entry',
    repeat_model,
    repeat_view,
)
