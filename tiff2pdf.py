import os
from PIL import Image
import natsort
dirname = "/home/XXX/Videos/Python13/tiff2pdf/input/"
imgs = []
list_of_files =os.listdir(dirname)
print(list_of_files)
list_of_files1=[x for x in list_of_files if (x.endswith(".tiff") or x.endswith(".jpg") or x.endswith(".tif")) ]
list_of_files2=natsort.natsorted(list_of_files1)
for fname in list_of_files2:
 path = os.path.join(dirname, fname)
 if os.path.isdir(path):
  continue
 imgs.append(path)

print(imgs)

imagelist=[]
for f in imgs:
 image_1 = Image.open(r'{}'.format(f))
 im_1 = image_1.convert('RGB')
 imagelist.append(im_1)
im_1.save('Output.pdf',save_all='True',append_images=imagelist)
