#!/usr/bin/env bash

part-one() {
    local sum=0
    while read -r line; do
        ((sum += line))
    done <<<"$DATA"

    echo "ONE: $sum"
}

part-two() {
    local sum=0
    local -A seen

    while true; do
        while read -r line; do
            ((sum += line))

            # Check if we've been here before
            if [[ -n ${seen[$sum]+x} ]]; then
                echo "TWO: $sum"
                return 0
            fi

            # Add to the list
            seen[$sum]=1
        done <<<"$DATA"
    done
}

main() {
    declare -g DATA
    DATA=$(get-data 2018 1)

    part-one
    part-two
}

main "$@"
