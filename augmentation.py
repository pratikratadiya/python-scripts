import os
import random
from scipy import ndarray

# image processing library
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io

def rotate(image_array: ndarray,angle):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = angle
    return sk.transform.rotate(image_array, random_degree)

def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]

folder_path = '/media/pratik/New Volume/Tomato/segmented/Tomato___Tomato_mosaic_virus/'
num_files_desired = 2000

# find all files paths from the folder
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

random.shuffle(images)

num_generated_files = len(images)
i = 0

while num_generated_files < num_files_desired:

    image_path = images[i]
    image_to_transform = sk.io.imread(image_path)
    transformed_image = None

    transformed_image = horizontal_flip(image_to_transform)
    new_file_path = '%s/augmented_image_%s.jpg' % (folder_path, num_generated_files)
    io.imsave(new_file_path, transformed_image)
    num_generated_files += 1
    
#    transformed_image = rotate(image_to_transform,3)
#    new_file_path = '%s/augmented_image_%s.jpg' % (folder_path, num_generated_files)    
#    io.imsave(new_file_path, transformed_image)
#    num_generated_files += 1
    
#    transformed_image = rotate(image_to_transform,-3)
#   new_file_path = '%s/augmented_image_%s.jpg' % (folder_path, num_generated_files)    
#    io.imsave(new_file_path, transformed_image)
#    num_generated_files += 1    
    
#    transformed_image = rotate(image_to_transform,5)
#    new_file_path = '%s/augmented_image_%s.jpg' % (folder_path, num_generated_files)    
#    io.imsave(new_file_path, transformed_image)
#    num_generated_files += 1    
    
#    transformed_image = rotate(image_to_transform,-5)
#    new_file_path = '%s/augmented_image_%s.jpg' % (folder_path, num_generated_files)    
#    io.imsave(new_file_path, transformed_image)
#    num_generated_files += 1                    
    
    i += 1
