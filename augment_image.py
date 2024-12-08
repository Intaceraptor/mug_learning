from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, array_to_img, img_to_array
import os
# Augmentation Function making use of datagen

# set up datagen, setting parameters for augmentation
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
)

# Directory to save augmented images
save_dir = 'augmented_mug_images'
os.makedirs(save_dir, exist_ok=True)

# Generate and save augmented images (for further use, rename mug_images with the desired name)
num_augmented_images = 1000  # Total number of augmented images to create
for i in range(mug_images.shape[0]):
    img = mug_images[i].reshape((1,) + mug_images[i].shape)  # Reshape to (1, 64, 64, 3)
    
    
    # Generate augmented images
    for j, augmented_image in enumerate(datagen.flow(img, batch_size=1)):
        if j >= num_augmented_images // train_set_x.shape[0]:
            break  # Stop after generating enough images for this original image
            
        # Convert to uint8 and save the augmented image
        file_path = os.path.join(save_dir, f'augmented_{i}_{j}.jpg')
        cv2.imwrite(file_path, augmented_image[0].astype(np.uint8))  # Ensure values are in the right range

print(f"Generated {num_augmented_images} augmented images in '{save_dir}' directory.")

x = load_img('augmented_mug_images/augmented_0_0.jpg')