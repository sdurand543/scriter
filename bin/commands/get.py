from metadata import *
from commands.CMD import CMD

def get_model(var_name):
    if meta_dict.contains_key(var_name):
        return meta_dict[var_name]
    return ""

def get_view(args):
    assert len(args) == 3
    var_name = args[2]
    view(get_model(var_name))

get = CMD \
(
    'get',
    'scr get <var_name>',
    'returns the value of the given variable',
    get_model,
    get_view,
)
