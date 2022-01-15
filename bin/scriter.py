#!/usr/bin/python

import os
import sys

from serial_dict import serial_dict
from cmd_view import cmd_view

ENTRY_PREFIX = "#"

home_path = os.environ["HOME"]
meta_path = os.path.join(home_path, ".scriter/")
meta_dict = serial_dict(meta_path)

# stdout the cmd_view on given input
def view_and_exit(text):
    cmd_view(meta_dict["cmd_view"], text);
    exit()

# gets the number of entries in the src file
def get_num_entries(src_path):
    src = open(src_path, 'r')
    num_entries = 1
    while True:
        try:
            line = src.next()
            search_str = "%s"%(ENTRY_PREFIX)
            if line[:len(search_str)] == search_str:
                num_entries += 1
        except StopIteration:
            break
    return num_entries

# scriter.py init
def init(args):
    if not os.path.isdir(meta_path):
        try:
            os.mkdir(meta_path)
        except OSError:
            cmd_view("cat", "Cannot Initialize Persistence")
            exit()
        meta_dict["cmd_view"] = "cat"
        meta_dict["src_path"] = ""
        meta_dict["entry_num"] = 0
        meta_dict["num_entries"] = 0
    view_and_exit("initialized scriter (use scr.help for help)")
    
# scriter.py help
def hlp(args):
    help_text  = "Available Commands:\n"
    help_text += "\tscr.help\n"
    help_text +=     "\t\t- brings up this help screen\n"
    help_text += "\tscr.status\n"
    help_text +=     "\t\t- details scriter state\n"
    help_text += "\tscr.use <file_path>\n"
    help_text +=     "\t\t- selects the given file to iterate on\n"
    help_text += "\tscr.reset\n"
    help_text +=     "\t\t- resets to the first entry\n"
    help_text += "\tscr.rep\n"
    help_text +=     "\t\t- repeats the current entry\n"
    help_text += "\tscr.goto <entry_num>\n"
    help_text +=     "\t\t- jumps to the given entry\n"
    help_text += "\tscr.bwd\n"
    help_text +=     "\t\t- iterates to the previous entry\n"
    help_text += "\tscr.fwd\n"
    help_text +=     "\t\t- iterates to the next entry\n"
    help_text += "\tscr.prev\n"
    help_text +=     "\t\t- iterates to the previous entry and runs it\n"
    help_text += "\tscr.next\n"
    help_text +=     "\t\t- iterates to the next entry and runs it\n"
    help_text += "\tscr.clean\n"
    help_text +=     "\t\t- removes the scriter metadata folder"
    cmd_view("cat", help_text)
    exit()

# scriter.py status
def status(args):
    view_and_exit("Cmd View: %s\nUsing: %s\nAt Entry: %s\nTotal Entries: %s"%(meta_dict["cmd_view"], meta_dict["src_path"], meta_dict["entry_num"], meta_dict["num_entries"]))
    
# scriter.py use <filepath>
def use(args):
    src_path = os.path.abspath(args[2])
    meta_dict["src_path"] = src_path
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(src_path)
    view_and_exit("using %s"%(args[2]))

# scriter.py reset
def reset(args):
    src_path = meta_dict["src_path"]
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(src_path)
    view_and_exit("reset %s"%(src_path))

# scriter.py rep
def repeat(args):
    src_path = meta_dict["src_path"]
    if not os.path.isfile(src_path):
        view_and_exit("src_path does not exist")
    src = open(src_path, 'r')
    entry_num = int(meta_dict["entry_num"])

    if entry_num == 0:
        view_and_exit("Start of File")

    if entry_num == int(meta_dict["num_entries"]):
        view_and_exit("End of File")

    # goto entry
    line = ""
    iter_entry_num = 0
    while iter_entry_num < entry_num:
        search_str = "%s"%(ENTRY_PREFIX)    
        try:
            line = src.next()
            if line[:len(search_str)] == search_str:
                iter_entry_num += 1
        except StopIteration:
            view_and_exit("File Modified Since Use")
    
    # proceed to next line
    try:
        line = src.next()
    except StopIteration:
        view_and_exit("")

    # go until next entry_num
    entry = ""    
    search_str = "%s"%(ENTRY_PREFIX)
    while line[:len(search_str)] != search_str:
        entry += line
        try:
            line = src.next()
        except StopIteration:
            break

    # view_and_exit
    src.close()
    view_and_exit(entry.strip())

# scriter.py goto
def goto(args):
    entry_num = int(args[2])
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num

# scriter.py bwd
def bwd(args):
    entry_num = int(meta_dict["entry_num"]) - 1
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num
    
# scriter.py fwd
def fwd(args):
    entry_num = int(meta_dict["entry_num"]) + 1
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num

# scriter.py prev
def prev(args):
    bwd(args)
    repeat(args)

# scriter.py next
def nxt(args):
    fwd(args)
    repeat(args)

# UI
commands = dict()
commands["init"] = init
commands["help"] = hlp
commands["status"] = status
commands["use"] = use
commands["reset"] = reset
commands["rep"] = repeat
commands["goto"] = goto
commands["bwd"] = bwd
commands["fwd"] = fwd
commands["prev"] = prev
commands["next"] = nxt
    
def main(args):
    if len(args) == 1:
        raise Exception("No Command Specified")
    if args[1] in commands:
        commands[args[1]](args)
    else:
        raise Exception("Command " + args[1] + " Unrecognized")

if __name__ == "__main__":
    main(sys.argv)
