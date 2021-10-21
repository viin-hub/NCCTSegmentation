import nibabel.nifti1 as nitool
import os
import sys
import pandas as pd

#%% 

data_folder = '/home/miranda/Documents/data/INSPIRE/subtype/V10.32'

gm_filename = r'c1reg.nii'
wm_filename = r'c2reg.nii'

df1 = pd.read_csv('/home/miranda/Documents/data/INSPIRE/subtype/v1032.txt', header=None, sep='\t')

for index, row in df1.iterrows():
    f = row[0]
    current_dir = os.path.dirname(f)
    gm_file = nitool.load(f)
    gm_img = gm_file.get_fdata()

    basename = os.path.basename(f)
    wm_filename = basename.replace('c01','c02')
    
    wm_file = nitool.load(os.path.join(current_dir,wm_filename))
    wm_img = wm_file.get_fdata()
    
    tbv_img = gm_img + wm_img
    tbv_file = nitool.Nifti1Image(tbv_img,gm_file.affine)
    parts = f.split("/")
    fn = parts[-4]
    fn1 = parts[-3]
    fn2 = parts[-2]
    targ_dir = os.path.join(data_folder,fn,fn1,fn2)
    if not os.path.exists(targ_dir):
        os.makedirs(targ_dir)
    tbv_filename = os.path.join(targ_dir,'tbvmask_image.nii.gz')
    print(tbv_filename)
    nitool.save(tbv_file,tbv_filename)
