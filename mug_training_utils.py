import cv2
import os
import numpy as np

def process_image(input_image):
    target_size = (224, 224) 
    img = cv2.imread(input_image)
    resized_img = cv2.resize(img, target_size)
    normalized_img = cv2.normalize(resized_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    reshaped = normalized_img.reshape(-1,1).T

    return reshaped

def process_batch(input_folder):
    target_size = (224, 224) 
    images = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpeg') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(input_folder, filename))
            resized_img = cv2.resize(img, target_size)  
            normalized_img = cv2.normalize(resized_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
            reshaped = normalized_img
            images.append(reshaped)
    return np.array(images)

def load_images_and_labels(image_folder, label):
    images = []
    labels = []
    for image_file in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        images.append(image)
        labels.append(label)
    return np.array(images), np.array(labels)