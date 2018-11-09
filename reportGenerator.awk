#! /usr/bin/awk

{
    print $7
    # if NF == 9, then remove [ ] from the regex.
    # check the length
    # if bigger 0
    for (i = 9; i <= NF; i++) {
        print $i;
    }

}