#!/usr/bin/python

import os
import sys

from serial_dict import serial_dict
from cmd_view import cmd_view

ENTRY_PREFIX = "#"

home_path = os.environ["HOME"]
meta_path = os.path.join(home_path, ".scriter/")
meta_dict = serial_dict(meta_path)

# stdout the display_cmd on given input
def view(text):
    cmd_view(meta_dict["display_cmd"], text);

# gets the number of entries in a src file
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
def init():
    if not os.path.isdir(meta_path):
        try:
            os.mkdir(meta_path)
        except OSError:
            cmd_view("cat", "Cannot Initialize Persistence")
            exit()
        meta_dict["display_cmd"] = "cat"
        meta_dict["src_path"] = ""
        meta_dict["entry_num"] = 0
        meta_dict["num_entries"] = 0

def init_public(args):
    init()
    view("initialized scriter (use scr.help for help)")
    
# scriter.py help
def hlp():
    help_text  = "Available Commands:\n"
    help_text += "\tscr.help\n"
    help_text +=     "\t\t- brings up this help screen\n"
    help_text += "\tscr.status\n"
    help_text +=     "\t\t- details scriter state\n"
    help_text += "\tscr.get <var_name>\n"
    help_text +=     "\t\t- returns a variable's value\n"
    help_text += "\tscr.display_cmd <cmd>\n"
    help_text +=     "\t\t- sets the scriter display cmd\n"
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
    return help_text

def hlp_public(args):
    view(hlp())

# scriter.py status
def status():
    return("display_cmd: %s\nsrc_path: %s\nAt entry_num: %s\nnum_entries: %s"%(meta_dict["display_cmd"], meta_dict["src_path"], meta_dict["entry_num"], meta_dict["num_entries"]))

def status_public(args):
    view(status())

# scriter.py get <var_name>
def get(var_name):
    if meta_dict.contains_key(var_name):
        return meta_dict[var_name]
    return ""

def get_public(args):
    view(get(args[2]))

# scriter.py display_cmd <cmd>
def display_cmd(cmd):
    meta_dict["display_cmd"] = cmd

def display_cmd_public(args):
    display_cmd(args[2])
    view("display_cmd set to %s"%(args[2]))
    
# scriter.py use <filepath>
def use(path):
    src_path = os.path.abspath(path)
    meta_dict["src_path"] = src_path
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(src_path)

def use_public(args):
    use(args[2])
    view("using %s"%(args[2]))    

# scriter.py reset
def reset():
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(meta_dict["src_path"])

def reset_public(args):
    reset()
    view("reset %s"%(meta_dict["src_path"]))

# scriter.py rep
def repeat():
    src_path = meta_dict["src_path"]
    try:
        src = open(src_path, 'r')
    except IOError:
        return "src_path could not be opened"
    entry_num = int(meta_dict["entry_num"])
    
    if entry_num == 0:
        return "Start of File"
    
    if entry_num == int(meta_dict["num_entries"]):
        return "End of File"
    
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
            return "File Modified Since Use"
    
    # proceed to next line
    try:
        line = src.next()
    except StopIteration:
        return ""

    # go until next entry_num
    entry = ""    
    search_str = "%s"%(ENTRY_PREFIX)
    while line[:len(search_str)] != search_str:
        entry += line
        try:
            line = src.next()
        except StopIteration:
            break

    # view
    src.close()
    return entry.strip()

def repeat_public(args):
    view(repeat())

# scriter.py goto
def goto(entry_num):
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num

def goto_public(args):
    goto(int(args[2]))

# scriter.py bwd
def bwd():
    entry_num = int(meta_dict["entry_num"]) - 1
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num

def bwd_public(args):
    bwd()
    
# scriter.py fwd
def fwd():
    entry_num = int(meta_dict["entry_num"]) + 1
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num

def fwd_public(args):
    fwd()

# scriter.py prev
def prev():
    bwd()
    return repeat()

def prev_public():
    view(prev())

# scriter.py next
def nxt():
    fwd()
    return repeat()

def nxt_public(args):
    view(nxt())

# UI
commands = dict()
commands["init"] = init_public
commands["help"] = hlp_public
commands["status"] = status_public
commands["get"] = get_public
commands["display_cmd"] = display_cmd_public
commands["use"] = use_public
commands["reset"] = reset_public
commands["rep"] = repeat_public
commands["goto"] = goto_public
commands["bwd"] = bwd_public
commands["fwd"] = fwd_public
commands["prev"] = prev_public
commands["next"] = nxt_public
    
def main(args):
    if len(args) == 1:
        raise Exception("No Command Specified")
    if args[1] in commands:
        commands[args[1]](args)
    else:
        raise Exception("Command " + args[1] + " Unrecognized")

if __name__ == "__main__":
    main(sys.argv)
