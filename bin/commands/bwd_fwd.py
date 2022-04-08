from metadata import *
from commands.CMD import CMD

def backward():
    set_entry_num(int(meta_dict["entry_num"]) - 1)

def backward_view(args):
    backward()

def forward():
    set_entry_num(int(meta_dict["entry_num"]) + 1)

def forward_view(args):
    forward()

backward_cmd = CMD \
(
    'bwd',
    'scr bwd',
    'iterates to the previous scriter entry',
    backward_view,
    [0],
)

forward_cmd = CMD \
(
    'fwd',
    'scr fwd',
    'iterates to the next scriter entry',
    forward_view,
    [0],
)
