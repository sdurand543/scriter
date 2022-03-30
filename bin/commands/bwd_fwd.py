from metadata import *
from commands.CMD import CMD

def set_entry_num(entry_num):
    """
    Sets the current entry num (with bounds check).
    """
    if entry_num >= 0 and entry_num <= int(meta_dict["num_entries"]):
        meta_dict["entry_num"] = entry_num
    
def backward_model():
    set_entry_num(int(meta_dict["entry_num"]) - 1)

def backward_view(args):
    assert len(args) == 2
    backward_model()

def forward_model():
    set_entry_num(int(meta_dict["entry_num"]) + 1)

def forward_view(args):
    assert len(args) == 2
    forward_model()

backward = CMD \
(
    'bwd',
    'scr bwd',
    'iterates to the previous scriter entry',
    backward_model,
    backward_view,
)

forward = CMD \
(
    'fwd',
    'scr fwd',
    'iterates to the next scriter entry',
    forward_model,
    forward_view,
)
