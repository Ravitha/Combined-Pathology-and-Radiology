#!/bin/sh
Prefix='cbtc_test_'
Suffix='.svs'
OUTPUT_FOLDER='/root/Pathology/testfiles/process_'
for i in `seq 33 34` 
do
	c=$Prefix$i$Suffix
	slash='\'
	output=$OUTPUT_FOLDER$i$slash
	vips dzsave $c $output
done
