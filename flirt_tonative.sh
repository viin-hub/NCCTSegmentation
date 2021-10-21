#!/usr/bin/env bash


OUTPUTNAME=cTBVmask

echo "PROCESSING subjects"
echo "...Registering using inverse transformation matrix"
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
    targetDir="/home/miranda/Documents/data/INSPIRE/subtype/V10.3"
    INPUTIMAGE="tbvmask_image.nii.gz"
    affDir="/home/miranda/Documents/data/INSPIRE/subtype/V10.2"
    DESTDIR="/home/miranda/Documents/data/INSPIRE/subtype/V10.3"
    mkdir -p $DESTDIR/$fn3/$fn2/$fn1
    flirt \
        -in $targetDir/$fn3/$fn2/$fn1/$INPUTIMAGE \
        -ref $s \
        -applyxfm \
        -init $affDir/$fn3/$fn2/$fn1/affine_tonative.txt \
        -out $DESTDIR/$fn3/$fn2/$fn1/$OUTPUTNAME \
        -v
done < /home/miranda/Documents/data/INSPIRE/subtype/v101.txt
echo "Finished at: $(date)"


