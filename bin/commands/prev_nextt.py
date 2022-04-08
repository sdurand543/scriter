from metadata import *
from commands.CMD import CMD

from commands.repeat import repeat
from commands.bwd_fwd import backward
from commands.bwd_fwd import forward

def previous():
    backward()
    return repeat()

def previous_view(args):
    view(previous())

# scriter.py next
def nextt():
    forward()
    return repeat()

def nextt_view(args):
    view(nextt())

previous_cmd = CMD \
(
    'prev',
    'scr prev',
    'iterates to the previous scriter entry and repeats it',
    previous_view,
    [0],
)

nextt_cmd = CMD \
(
    'next',
    'scr next',
    'iterates to the next scriter entry and repeats it',
    nextt_view,
    [0],
)
