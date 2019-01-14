#!/bin/bash

crnt_data=`date`
touch /tmp/"${crnt_data}_test.txt"

f_cnt=`find /tmp -name "*_test.txt" | wc -l`
if [ $f_cnt -eq 3 ]; then
    exit 9
fi

sleep 5
exit 0
