#!/bin/bash

while IFS='\n' read -r s
do
	# echo $s
	fn0=$(basename "$s")
	# echo $fn0
	part1=$(dirname "$s")
	part2=$(dirname "$part1")
	fn1=$(basename "$part1")
	# echo $fn1
	part3=$(dirname "$part2")
	fn2=$(basename "$part2")
	# echo $fn2
	targetDir="/home/miranda/Documents/data/INSPIRE/subtype/V7.1"
	# echo ${targetDir}/$fn2/$fn1/$fn0
	mkdir -p ${targetDir}/$fn2/$fn1/$fn0
	niftidir=${targetDir}/$fn2/$fn1/$fn0

	cd "$s"
	/home/miranda/Downloads/MRIcroGL_linux/MRIcroGL/Resources/dcm2niix -o $niftidir -f %p_%s -g y "$s"

done < /home/miranda/Documents/data/INSPIRE/subtype/subtype_INSPIRE_dcm_folders.csv