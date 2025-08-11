#!/usr/bin/env bash

set -eu

runner() {
    local data="$1"
    local times="$2"

    match=$(printf '0%.0s' $(seq 1 "$times"))

    local sum="" i=0
    while true; do
        sum=$(printf '%s' "$data$i" | md5sum)
        ((i % 1000 == 0)) && debug "$i"

        [[ "${sum:0:$times}" == "$match" ]] && break
        ((++i))
    done

    echo "SOLVE: $i - $sum"
}

main() {
    local data=$(get-data 2015 4)

    runner "$data" 5
    runner "$data" 6
}

main "$@"
