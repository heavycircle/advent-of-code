#!/usr/bin/env bash

set -u

part-one() {
    # Get number of left
    lp=${data//\(/}
    lc=$((${#data} - ${#lp}))

    # Get number of right
    rp=${data//\)/}
    rc=$((${#data} - ${#rp}))

    echo "ONE: $(($lc - $rc))"
}

part-two() {
    local sum=0
    for i in $(seq 1 "${#data}"); do
        # Get current char
        chr=${data:$((i - 1)):1}
        case "$chr" in
            '(') ((sum++)) ;;
            ')') ((sum--)) ;;
        esac

        # Check if we're below zero
        if ((sum < 0)); then
            echo "TWO: $i"
            return 0
        fi
    done

    echo "never went below!"
}

main() {
    declare -g data=$(get-data 2015 1)

    part-one
    part-two
}

main "$@"
