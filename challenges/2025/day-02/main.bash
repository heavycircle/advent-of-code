#!/usr/bin/env bash

main() {
    declare -g DATA=$(get-data 2025 2)
    echo "$DATA"
}

main "$@"
