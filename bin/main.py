#!/usr/bin/python

import os, sys

from metadata import *
from commands.CMD import cmds
from commands.init import init

from commands.init import init_cmd
from commands.status import status_cmd
from commands.helpp import helpp_cmd
from commands.get import get_cmd
from commands.sett import sett_cmd
from commands.use import use_cmd
from commands.reset import reset_cmd
from commands.goto import goto_cmd
from commands.repeat import repeat_cmd
from commands.bwd_fwd import forward_cmd
from commands.bwd_fwd import backward_cmd
from commands.prev_nextt import previous_cmd
from commands.prev_nextt import nextt_cmd
from commands.clean import clean_cmd

def main(args):
    if len(args) == 1:
        err("No Command Specified")
    cmd_name = args[1]
    if cmd_name not in cmds:
        err("Command %s Unrecognized"%(cmd_name))
    if not initialized():
        init()
    cmd = cmds[cmd_name]
    if (len(args) - 2) not in cmd.argc:
        err("Invalid Number of Arguments (Usage: %s)"%(cmd.semantics))
    cmd.f_view(args)
    
if __name__ == "__main__":
    main(sys.argv)
