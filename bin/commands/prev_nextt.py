from metadata import *
from commands.CMD import CMD

from commands.repeat import repeat
from commands.bwd_fwd import backward
from commands.bwd_fwd import forward

def previous_model():
    backward.f_model()
    return repeat.f_model()

def previous_view(args):
    assert(len(args)) == 2
    view(previous_model())

# scriter.py next
def nextt_model():
    forward.f_model()
    return repeat.f_model()

def nextt_view(args):
    assert(len(args)) == 2
    view(nextt_model())

previous = CMD \
(
    'prev',
    'scr prev',
    'iterates to the previous scriter entry and repeats it',
    previous_model,
    previous_view,
)

nextt = CMD \
(
    'next',
    'scr next',
    'iterates to the next scriter entry and repeats it',
    nextt_model,
    nextt_view,
)
