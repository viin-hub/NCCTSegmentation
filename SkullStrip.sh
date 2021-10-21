#!/bin/bash

while IFS=, read -r col1 
do
	img=${col1%.*}
	echo $img

	intensity=0.01
	outfile=${img}_fsl_ss_0.01
	tmpfile=`mktemp`

	# Thresholding Image to 0-100
	fslmaths "${img}" -thr 0.000000 -uthr 100.000000  "${outfile}" 
	# Creating 0 - 100 mask to remask after filling
	fslmaths "${outfile}"  -bin   "${tmpfile}"; 
	fslmaths "${tmpfile}.nii.gz" -bin -fillh "${tmpfile}" 
	# Presmoothing image
	fslmaths "${outfile}"  -s 1 "${outfile}"; 
	# Remasking Smoothed Image
	fslmaths "${outfile}" -mas "${tmpfile}"  "${outfile}" 
	# Running bet2
	bet2 "${outfile}" "${outfile}" -f ${intensity} -v 
	# Using fslfill to fill in any holes in mask 
	fslmaths "${outfile}" -bin -fillh "${outfile}_Mask" 
	# Using the filled mask to mask original image
	fslmaths "${img}" -mas "${outfile}_Mask"  "${outfile}" 


done < /home/miranda/Documents/data/INSPIRE/subtype/nii_v71_r.txt