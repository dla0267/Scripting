#! /bin/bash

file="/Users/Yuun/Desktop/scripting/Assignment3/sampleInteg.txt"

while IFS=" " read -r f1 f2 f3 f4 f5 f6 f7 f8 f9 
do
        # display fields using f1, f2,..,f7
        echo "$f7" "$f9"
        #printf 'Cookies: %s, Segments: %s\n' "$f7" "$f9"
done <"$file"