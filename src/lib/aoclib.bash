#!/usr/bin/env bash

# Bash Utilities for solving AOC challenges.

###############################################
#   LOGGERS                                   #
###############################################

fatal() {
    echo -e "[\033[31m-\033[0m] FATAL: $1" >&2
    exit 1
}

debug() {
    (($DEBUG == 1)) || return 0
    echo -e "[\033[32m+\033[0m] $1" >&2
}

###############################################
#   MAIN FUNCTIONS                            #
###############################################

# Get the input data for a specified year/date.
get-data() {
    local inpfile=input/"$YEAR"/day-"$DATE".txt
    [[ -f "$inpfile" ]] || fatal "missing input file: ${YEAR@A} ${DATE@A}"

    cat "$inpfile"
}
