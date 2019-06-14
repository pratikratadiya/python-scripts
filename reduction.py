import os,glob,random

files = glob.glob('/media/pratik/New Volume/Tomato/segmented/Tomato___Bacterial_spot/*')

random.shuffle(files)
i = len(files) - 2000

for f in files:
    if i == 0:
        break
    os.remove(f)
    i = i - 1
