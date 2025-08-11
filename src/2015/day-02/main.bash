#!/usr/bin/env bash

min3() {
    local a=$1 b=$2 c=$3 m
    m=$((a < b ? a : b))
    m=$((c < m ? c : m))
    echo "$m"
}

part-one() {
    local sum=0

    while IFS='x' read -r l w h; do
        # Get the faces
        local x=$(($l * $w))
        local y=$(($l * $h))
        local z=$(($w * $h))

        # Get slack
        local m=$(min3 $x $y $z)

        # Get area
        local area=$((2 * ($x + $y + $z) + $m))
        ((sum += $area))
    done <<<"$DATA"

    echo "$sum"
}

part-two() {
    local sum=0

    while IFS='x' read -r l w h; do
        # Sort the list
        read -r -a sorted <<<"$(printf '%s\n' "$l" "$w" "$h" | sort -n | tr '\n' ' ')"

        # Get the pieces
        local base=$((2 * (${sorted[0]} + ${sorted[1]})))
        local ribbon=$((${sorted[0]} * ${sorted[1]} * ${sorted[2]}))

        # Get area
        local area=$(($base + $ribbon))
        ((sum += $area))

    done <<<"$DATA"

    echo "$sum"
}

main() {
    declare -g DATA=$(get-data 2015 2)

    part-one
    part-two
}

main "$@"
