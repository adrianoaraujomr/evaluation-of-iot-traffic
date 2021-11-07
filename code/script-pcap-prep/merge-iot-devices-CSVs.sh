#!/bin/bash

files=$(tr -s " " < iot_endpoints_2.txt  | cut -d ' ' -f 3)
for file in $files;
do
	help=true
	tomerge=`ls | grep $file`

	for csv in $tomerge;
	do
		if [ "$help" = true ] ; 
		then
			cat $csv > $file".csv"
			rm $csv
			help=false
		else
			tail -n+2 $csv > $file".csv"
			rm $csv
		fi
	done

done
