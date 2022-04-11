#!/usr/bin/python

import os, sys

from metadata import *
from commands.CMD import cmds
from commands.init import init
from commands.cmd_imports import *

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
    meta_dict["source_cmd"] = ""
    cmd.f_view(args)
    
if __name__ == "__main__":
    main(sys.argv)
