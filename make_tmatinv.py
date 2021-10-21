import os
import numpy as np
import sys
import pandas as pd

# inverse of the affine registration matrix
def write_tmat_inv(tmat_filename,inv_filename):
    tmat_file = os.path.join(tmat_filename)
    with open(tmat_file, 'rt') as tmatfile:
        lines = tmatfile.readlines()
    
    affine = np.array([[float(m) for m in k.rstrip().split()] for k in lines])       
    affineinv = np.linalg.inv(affine)
    
    tmatinv_filename = os.path.join(inv_filename)
    with open(tmatinv_filename, 'wt') as writefile:
        affineinv_list = affineinv.tolist()
        for i in affineinv_list:
            for j in i:
                writefile.write(str(j)+'  ')
            writefile.write('\n')
    
    return inv_filename
            
            
if __name__ == '__main__' :

    df = pd.read_csv('/home/miranda/Documents/data/INSPIRE/subtype/v102.txt', header=None, sep='\t')
    subjects = []

    for index, row in df.iterrows():
        f = row[0]
        subjects.append(f)

    tmat_filename = 'tmat.txt'
    tmatinv_filename = 'affine_tonative.txt'
    
    for sub in subjects:
        invDir = os.path.dirname(sub)
        tmat_file = os.path.join(invDir,tmat_filename)
        tmatinv_file = os.path.join(invDir,tmatinv_filename)
        print(write_tmat_inv(tmat_file, tmatinv_file))

