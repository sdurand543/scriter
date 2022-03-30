from metadata import *
from commands.CMD import CMD

def sett_model(var_name, new_value):
    meta_dict[var_name] = new_value

def sett_view(args):
    assert len(args) == 4
    var_name = args[2]
    new_value = args[3]
    sett_model(var_name, new_value)
    view("set %s to %s"%(var_name, new_value))

sett = CMD \
(
    'set',
    'scr set <var_name> <new_value>',
    'sets the given variable to the given value',
    sett_model,
    sett_view,
)
