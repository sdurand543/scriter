#!/bin/sh

#export SCRITER_BIN=$PWD #(this may be necessary on some systems, but is less versatile)
export SCRITER_BIN="$( cd "$( dirname "$0" )" > /dev/null && pwd )"

function scr() {
    python $SCRITER_BIN/main.py $@
    source $HOME/.scriter/source_cmd
}

scr init
