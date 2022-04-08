from metadata import *
from commands.CMD import CMD
from commands.CMD import cmds

def helpp(cmd_name = None):
    if cmd_name == None:
        help_text  = "Available Commands:\n"
        for cmd in cmds.values():
            help_text += "\t%s\n"%(cmd.semantics)
            help_text +=     "\t\t- %s\n"%(cmd.description)
        return help_text[:-1]
    else:
        cmd = cmds[cmd_name]
        help_text = "%s\n"%(cmd.semantics)
        help_text +=     "\t- %s\n"%(cmd.description)
        return help_text[:-1]

def helpp_view(args):
    if len(args) == 2:
        view(helpp())
    if len(args) == 3:
        cmd = args[2]
        view(helpp(cmd))

helpp_cmd = CMD \
(
    'help',
    'scr help [optional_cmd]',
    'displays information about available commands',
    helpp_view,
    [0, 1],
)
