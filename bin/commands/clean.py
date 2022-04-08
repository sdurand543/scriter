import os

from metadata import *
from commands.CMD import CMD

def clean():
    remove(meta_path)
    
def clean_view(args):
    clean()
    view("cleaned scriter HOME meta-directory")

clean_cmd = CMD \
(
    'clean',
    'scr clean',
    'cleans scriter HOME meta-directory',
    clean_view,
    [0],
)
