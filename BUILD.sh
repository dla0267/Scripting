#! /bin/bash

sed 's/^[0-9][0-9].*: //  ' evaluator-integration.log > sample.txt
awk ' { if (length($1) == 32) print $0} ' sample.txt > formatedSample.txt

sed 's/^[0-9][0-9].*: //  ' evaluator-integration-baseline.log.txt > baseline.txt
awk ' { if (length($1) == 32) print $0} ' baseline.txt > formatedBaseline.txt

