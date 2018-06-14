#!/bin/bash

# TODO: Figure this out dynamically. Used command line:
#
#     $ kaggle datasets list --page 383
#
# mixed with divide and conquer technique to land on this number.
last_page=383

kaggle datasets list --csv --page 1 > datasets.csv

for page in $(seq 2 $last_page)
do
    echo $page
    kaggle datasets list --csv --page $page | tail -n20 >> datasets.csv
    sleep 1
done
