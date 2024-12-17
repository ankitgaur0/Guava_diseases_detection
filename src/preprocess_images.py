# src/data_preprocessing.py

from tensorflow.keras.preprocessing.image import ImageDataGenerator

class DataPreprocessor:
    def __init__(self, rotation_range=40, width_shift_range=0.2, height_shift_range=0.2,
                 shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest'):
        self.rotation_range = rotation_range
        self.width_shift_range = width_shift_range
        self.height_shift_range = height_shift_range
        self.shear_range = shear_range
        self.zoom_range = zoom_range
        self.horizontal_flip = horizontal_flip
        self.fill_mode = fill_mode

    def get_data_augmentation(self):
        """
        Returns an ImageDataGenerator with augmentations.
        """
        datagen = ImageDataGenerator(
            rotation_range=self.rotation_range,
            width_shift_range=self.width_shift_range,
            height_shift_range=self.height_shift_range,
            shear_range=self.shear_range,
            zoom_range=self.zoom_range,
            horizontal_flip=self.horizontal_flip,
            fill_mode=self.fill_mode
        )
        return datagen

    def scale_images(self, images):
        """
        Scales the image values to [0,1].
        """
        return images / 255.0
