#!/usr/bin/env bash

echo "Started at: $(date)"
while read s
do
	echo $s
	part1=$(dirname "$s")
	part2=$(dirname "$part1")
	fn1=$(basename "$part1")
	# echo $fn1
	part3=$(dirname "$part2")
	fn2=$(basename "$part2")
	# echo $fn2
	part4=$(dirname "$part3")
	fn3=$(basename "$part3")
	# echo $fn3
	targetDir="/home/miranda/Documents/data/INSPIRE/subtype/V10.2"
	mkdir -p ${targetDir}/$fn3/$fn2/$fn1 
	DESTDIR=${targetDir}/$fn3/$fn2/$fn1
	flirt -in $s -ref $"/home/miranda/Documents/code/official/ClinicalCTSeg/atlas/INSPIRE_CT_template.nii.gz" -out $DESTDIR/reg -omat $DESTDIR/tmat.txt
done < /home/miranda/Documents/data/INSPIRE/subtype/v101.txt
echo "Finished at: $(date)"

