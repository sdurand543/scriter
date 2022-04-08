import os

from metadata import *
from commands.CMD import CMD

def use(src_path):
    src_path = os.path.abspath(src_path)
    meta_dict["src_path"] = src_path
    meta_dict["entry_num"] = 0
    meta_dict["num_entries"] = get_num_entries(src_path)

def use_view(args):
    if len(args) != 3:
        err("Invalid number of arguments")
    src_path = args[2]
    use(src_path)
    view("using %s"%(src_path))

use_cmd = CMD \
(
    'use',
    'scr use <src_path>',
    'selects the given src_path to iterate on',
    use_view,
    [1],
)
