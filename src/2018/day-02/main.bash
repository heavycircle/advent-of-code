#!/usr/bin/env python3

part-one() {
    local twos=0 threes=0
    # Read the lines
    while read -r line; do
        # Make the hashmap
        local -A counts=()
        for ((i = 0; i < "${#line}"; ++i)); do
            chr="${line:i:1}"
            ((counts[$chr]++))
        done

        # Check the counts
        local two=0 three=0
        for key in "${!counts[@]}"; do
            ((two == 0 && counts["$key"] == 2)) && two=1
            ((three == 0 && counts["$key"] == 3)) && three=1
        done

        # Aggregate counts
        ((twos += two))
        ((threes += three))
    done <<<"$DATA"

    echo "ONE: $((twos * threes))"
}

part-two() {
    # The standard to check against
    local i=0
    while read -r std; do

        # The list to check
        local j=0
        while read -r chk; do
            ((i == j)) && continue

            # Check for off by one
            local good=1 flag=-1
            for ((k = 0; k < "${#std}"; ++k)); do
                [[ "${std:k:1}" == "${chk:k:1}" ]] && continue

                if ((flag != -1)); then
                    good=0
                    break
                else
                    flag="$k"
                fi
            done

            ((++j))

            # Found an off by one
            ((good == 1)) || continue
            echo "TWO: ${std:0:flag}${std:flag+1}"
            return 0
        done <<<"$DATA"

        ((++i))
    done <<<"$DATA"
}

main() {
    declare -g DATA
    DATA=$(get-data 2018 2)

    part-one
    part-two
}

main "$@"
