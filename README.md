## pipeline to process clinical stroke NCCT

* step 1: dcm to nifti and correct grantry tilt impact (dcm2nii.sh)
* step 2: skull strip (SkullStrip.sh)
* step 3: registration to normalized NCCT brain template (match with the betsct1_unsmooth.nii) flirtCT.sh
* step 4: segmentation. TisSeg.m TisSeg_job.m
* step 5: make tbv, tiv masks. makeTBVmasks.py makeTIVmasks.py
* step 6: Affine transformation to native space. make_tmatinv.py flirt_tonative.sh

build CT template: built_CTtemp.py