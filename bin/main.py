#!/usr/bin/python

import os
import sys

from commands.CMD import cmds
from commands.init import init
from commands.status import status
from commands.helpp import helpp
from commands.get import get
from commands.sett import sett
from commands.use import use
from commands.reset import reset
from commands.repeat import repeat
from commands.bwd_fwd import forward
from commands.bwd_fwd import backward
from commands.prev_nextt import previous
from commands.prev_nextt import nextt
from commands.clean import clean

def main(args):
    if len(args) == 1:
        raise Exception("No Command Specified")
    cmd = args[1]
    if cmd in cmds:
        cmds[cmd].f_view(args)
    else:
        raise Exception("Command " + cmd + " Unrecognized")

if __name__ == "__main__":
    main(sys.argv)
