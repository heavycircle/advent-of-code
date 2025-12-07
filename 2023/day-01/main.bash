#!/usr/bin/env bash

find-matches() {
    local -n m=$1

    # Build the regex string
    local regex
    regex="($(
        IFS='|'
        echo "${!m[*]}"
    ))"

    # Read each file
    local sum=0
    while read -r line; do
        local first="" last="" total

        # Get our match
        while [[ $line =~ $regex ]]; do
            local match="${BASH_REMATCH[1]}"

            # Set first and last
            if [[ -z $first ]]; then
                first="$match"
            else
                last="$match"
            fi

            # Find where the match is
            local idx=-1 len="${#match}"
            for ((i = 0; i < ${#line}; i++)); do
                [[ ${line:i:len} == "$match" ]] || continue

                idx="$i"
                break
            done

            # Slice to move on
            line=${line:((idx + 1))}
        done

        # Get big digit
        [[ -n "$first" ]] || first=zero
        [[ -n "$last" ]] || last="$first"
        total="${maps[$first]}${maps[$last]}"
        ((sum += total))

    done <<<"$DATA"

    echo "$sum"
}

part-one() {
    local -A maps=(
        [0]=0 [1]=1 [2]=2 [3]=3 [4]=4 [5]=5 [6]=6 [7]=7 [8]=8 [9]=9
    )

    echo "ONE: $(find-matches maps)"
}

part-two() {
    local -A maps=(
        [zero]=0 [one]=1 [two]=2 [three]=3 [four]=4
        [five]=5 [six]=6 [seven]=7 [eight]=8 [nine]=9
        [0]=0 [1]=1 [2]=2 [3]=3 [4]=4 [5]=5 [6]=6 [7]=7 [8]=8 [9]=9
    )

    echo "TWO: $(find-matches maps)"
}

main() {
    declare -g DATA
    DATA=$(get-data 2023 1)

    part-one
    part-two
}

main "$@"
