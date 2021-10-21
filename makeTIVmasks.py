import nibabel.nifti1 as nitool
import os
import pandas as pd

#%% 

data_folder = '/home/miranda/Documents/data/INSPIRE/subtype/V10.32'

gm_filename = r'c1reg.nii'
wm_filename = r'c2reg.nii'
csf_filename = r'c3reg.nii'

df1 = pd.read_csv('/home/miranda/Documents/data/INSPIRE/subtype/v85_c1.txt', header=None, sep='\t')


for index, row in df1.iterrows():
    f = row[0]
    current_dir = os.path.dirname(f)
    gm_file = nitool.load(f)
    gm_img = gm_file.get_fdata()

    
    wm_file = nitool.load(os.path.join(current_dir, wm_filename))
    wm_img = wm_file.get_fdata()
    
    csf_file = nitool.load(os.path.join(current_dir, csf_filename))
    csf_img = csf_file.get_fdata()
    
    tiv_img = gm_img + wm_img + csf_img
    tiv_file = nitool.Nifti1Image(tiv_img, gm_file.affine)

    parts = f.split("/")
    fn = parts[-4]
    fn1 = parts[-3]
    fn2 = parts[-2]
    targ_dir = os.path.join(data_folder,fn,fn1,fn2)
    if not os.path.exists(targ_dir):
        os.makedirs(targ_dir)

    tiv_filename = os.path.join(targ_dir, 'tivmask_image.nii.gz')
    print (tiv_filename)
    nitool.save(tiv_file,tiv_filename)
