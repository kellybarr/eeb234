#! /bin/bash

tail -n +2 $1 > formatted_$1

sed '/"/,/"/d' formatted_$1 > reformatted_eBird_data.csv

python ebird_summarizer.py reformatted_eBird_data.csv