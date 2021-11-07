#!/bin/bash

macs=$(cat iot_endpoints.txt | tr -s " " | cut -d ' ' -f3)
echo $macs
pcaps=$(ls ./PCAPs/IOT | grep ".pcap")
echo $pcaps

for pcap in $pcaps;
do
	for mac in $macs;
	do
		echo $mac
		if test -f "./PCAPs/IOT/MAC/"$mac"_"$pcap".pcap"; 
		then
			echo $mac" alredy done for file "$pcap
		else
			tshark -r "./PCAPs/IOT/"$pcap -w "./PCAPs/IOT/MAC/"$mac"_"$pcap".pcap" -Y "eth.addr == $mac"
		fi
	done
done
