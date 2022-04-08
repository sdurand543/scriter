from metadata import *
from commands.CMD import CMD

def sett(var_name, new_value):
    meta_dict[var_name] = new_value

def sett_view(args):
    var_name = args[2]
    new_value = args[3]
    sett(var_name, new_value)
    view("set %s to %s"%(var_name, new_value))

sett_cmd = CMD \
(
    'set',
    'scr set <var_name> <new_value>',
    'sets the given variable to the given value',
    sett_view,
    [2],
)
