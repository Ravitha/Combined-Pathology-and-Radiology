#!/bin/bash
file="sample.txt"
while read line
do
	wget $line
done < "$file"
