import nibabel as nib
import ants
import pandas as pd


df = pd.read_csv('/home/miranda/Documents/data/INSPIRE/subtype/v91_c.csv', header=None, sep='\n')

list_img = []
for index, row in df.iterrows():
    f = row[0]
    list_img.append(f)

image1 = ants.image_read(list_img[0])
image2 = ants.image_read(list_img[1])
image3 = ants.image_read(list_img[2])
image4 = ants.image_read(list_img[3])
image5 = ants.image_read(list_img[4])
image6 = ants.image_read(list_img[5])
image7 = ants.image_read(list_img[6])
image8 = ants.image_read(list_img[7])
image9 = ants.image_read(list_img[8])
image10 = ants.image_read(list_img[9])
image11 = ants.image_read(list_img[10])
image12 = ants.image_read(list_img[11])
image13 = ants.image_read(list_img[12])
image14 = ants.image_read(list_img[13])
image15 = ants.image_read(list_img[14])
image16 = ants.image_read(list_img[15])
image17 = ants.image_read(list_img[16])
image18 = ants.image_read(list_img[17])
image19 = ants.image_read(list_img[18])
image20 = ants.image_read(list_img[19])
image21 = ants.image_read(list_img[20])
image22 = ants.image_read(list_img[21])
image23 = ants.image_read(list_img[22])
image24 = ants.image_read(list_img[23])
image25 = ants.image_read(list_img[24])
image26 = ants.image_read(list_img[25])
image27 = ants.image_read(list_img[26])
image28 = ants.image_read(list_img[27])
image29 = ants.image_read(list_img[28])
image30 = ants.image_read(list_img[29])


ini_template = ants.image_read('/home/miranda/Documents/code/official/ClinicalCTSeg/atlas/sct1_unsmooth.nii')

timagew = ants.build_template(initial_template = ini_template,\
image_list = (image1, image2, image3, image4,\
image5, image6, image7, image8, image9, image10, image11, image12, image13,\
image14, image15, image16, image17, image18, image19, image20, image21,\
image22, image23, image24, image25, image26, image27, image28, image29, image30), iterations=4)


ants_timagew = timagew.to_nibabel()
nib.save(ants_timagew, 'INSPIRE_CT_template.nii.gz')

