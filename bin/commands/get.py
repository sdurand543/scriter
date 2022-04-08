from metadata import *
from commands.CMD import CMD

def get(var_name):
    if meta_dict.contains_key(var_name):
        return meta_dict[var_name]
    return ""

def get_view(args):
    var_name = args[2]
    view(get(var_name))

get_cmd = CMD \
(
    'get',
    'scr get <var_name>',
    'returns the value of the given variable',
    get_view,
    [1],
)
