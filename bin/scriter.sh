#!/bin/sh

#export SCRITER_BIN=$PWD #(this may be necessary on some systems)
export SCRITER_BIN="$( cd "$( dirname "$0" )" > /dev/null && pwd )"

function scr() {
    scr.help
}

function scr.help() {
    eval "$(python $SCRITER_BIN/scriter.py help)"
}

function scr.status() {
    eval "$(python $SCRITER_BIN/scriter.py status)"
}

function scr.get() {
    eval "$(python $SCRITER_BIN/scriter.py get $1)"
}

function scr.display_cmd() {
    eval "$(python $SCRITER_BIN/scriter.py display_cmd $1)"
}

function scr.use() {
    eval "$(python $SCRITER_BIN/scriter.py use $1)"
}

function scr.reset() {
    eval "$(python $SCRITER_BIN/scriter.py reset)"
}

function scr.rep() {
    eval "$(python $SCRITER_BIN/scriter.py rep)"
}

function scr.goto() {
    eval "$(python $SCRITER_BIN/scriter.py goto $1)"
}

function scr.bwd() {
    eval "$(python $SCRITER_BIN/scriter.py bwd)"
}

function scr.fwd() {
    eval "$(python $SCRITER_BIN/scriter.py fwd)"
}

function scr.prev() {
    eval "$(python $SCRITER_BIN/scriter.py prev)"
}

function scr.next() {
    eval "$(python $SCRITER_BIN/scriter.py next)"
}

function scr.clean() {
    rm -rf $HOME/.scriter
}

eval "$(python $SCRITER_BIN/scriter.py init)"
