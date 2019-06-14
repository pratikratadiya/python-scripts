import os,sys
from PIL import Image

def resize():
    dirlist = [f.path for f in os.scandir('snap/') if f.is_dir()]
    for path in dirlist:
        dirs = os.listdir(path)
        for item in dirs:
            print(item)
            if os.path.isfile(path+'/'+item):
                    im = Image.open(path+'/'+item)
                    f,e = os.path.splitext(path+'/'+item)
                    imResize = im.resize((16,16), Image.ANTIALIAS)
                    print("Image resized")
                    imResize.save(f+'.jpg','JPEG',quality=100)
resize()
