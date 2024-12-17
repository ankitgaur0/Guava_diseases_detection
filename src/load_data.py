# src/data_load.py

import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class DataLoader:
    def __init__(self, data_dir, batch_size=32, image_size=(224, 224)):
        """
        Initialize with the main directory containing train, val, and test folders.
        Each category is a subfolder in train, val, and test.
        """
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.image_size = image_size

        # Directories for training, validation, and test sets
        self.train_dir = os.path.join(data_dir, 'train')
        self.val_dir = os.path.join(data_dir, 'val')
        self.test_dir = os.path.join(data_dir, 'test')

    def load_data(self):
        """
        Loads the data using ImageDataGenerator and resizes images.
        Assumes each subfolder inside 'train', 'val', and 'test' directories represents a class.
        """
        # Initialize the ImageDataGenerator for rescaling pixel values
        datagen = ImageDataGenerator(rescale=1./255)

        # Load train data
        train_data = datagen.flow_from_directory(
            self.train_dir,                   # Path to train directory
            target_size=self.image_size,      # Resize images to the required size
            batch_size=self.batch_size,       # Number of images per batch
            class_mode='categorical'          # Multi-class classification
        )

        # Load validation data
        val_data = datagen.flow_from_directory(
            self.val_dir,                     # Path to validation directory
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='categorical'
        )

        # Load test data
        test_data = datagen.flow_from_directory(
            self.test_dir,                    # Path to test directory
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='categorical'
        )
        print("data_load part complete")
        return train_data, val_data, test_data
