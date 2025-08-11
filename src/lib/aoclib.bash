#!/usr/bin/env bash

# Bash Utilities for solving AOC challenges.

# Get the input data for a specified year/date.
get-data() {
    local inpfile=input/"$year"/day-"$date".txt
    [[ -f "$inpfile" ]] || fatal "missing input file: ${year@A} ${date@A}"

    cat "$inpfile"
}