from metadata import *
from commands.CMD import CMD
from commands.CMD import cmds

def helpp_model():
    help_text  = "Available Commands:\n"
    for cmd in cmds.values():
        help_text += "\t%s\n"%(cmd.semantics)
        help_text +=     "\t\t- %s\n"%(cmd.description)
    return help_text

def helpp_view(args):
    assert(len(args)) == 2
    view(helpp_model())

helpp = CMD \
(
    'help',
    'scr help',
    'displays information about available commands',
    helpp_model,
    helpp_view,
)
