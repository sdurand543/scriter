import os, shutil

from metadata import *
from commands.CMD import CMD

def remove(path):
    """
    Removes the subtree of directories rooted at path.
    """
    if os.path.exists(path):  
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)

def clean_model():
    remove(meta_path)
    
def clean_view(args):
    assert len(args) == 2
    clean_model()
    view("cleaned scriter HOME meta-directory")

clean = CMD \
(
    'clean',
    'scr clean',
    'cleans scriter HOME meta-directory',
    clean_model,
    clean_view,
)
