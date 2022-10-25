from torchvision.datasets import VisionDataset

from PIL import Image

import os
import os.path
import sys

def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')


class Caltech(VisionDataset):
    def __init__(self, root, split='train', transform=None, target_transform=None):
        super(Caltech, self).__init__(root, transform=transform, target_transform=target_transform)

        self.split = split # This defines the split you are going to use
                           # (split files are called 'train.txt' and 'test.txt')

        '''
        - Here you should implement the logic for reading the splits files and accessing elements
        - If the RAM size allows it, it is faster to store all data in memory
        - PyTorch Dataset classes use indexes to read elements
        - You should provide a way for the __getitem__ method to access the image-label pair
          through the index
        - Labels should start from 0, so for Caltech you will have lables 0...100 (excluding the background class) 
        '''
        self.objectCategories=os.listdir(root+"101_ObjectCategories") #prendo tutte le cartelle di 101_ObjectCategories
        self.objectCategories.remove("BACKGROUND_Google") #rimuovo la cartella di backgroud

        #now i have to create the dataset
        '''
        - You should provide a way for the __getitem__ method to access the image-label pair through the index
        I can create a tuple (img, category) where category is the name of the directory, but numbered.
        '''
        self.dataset={}
        self.key=0
        self.categories={}

        for i, category in zip(range(len(self.objectCategories)),self.objectCategories):
            self.categories[category]=i #the key will the the value, so value = index -> so for example:
            '''
            zip(range(len(self.objectCategories)) gives me the full list of directories but numerical
            self.ObjectCategories gives me the NAME of the category.

            faces for example will be i=0 and self.objectCategories = faces.
            '''
            images=os.listdir(root+"101_ObjectCategories/"+category)
            for image in images:
                self.dataset[self.key]= (pil_loader(root+"101_ObjectCategories/"+category+"/"+image), i)
                '''
                pil_loader gives me the image, so I put in the the key value
                '''
                self.key+=1 

    def __getitem__(self, index):
        '''
        __getitem__ should access an element through its index
        Args:
            index (int): Index

        Returns:
            tuple: (sample, target) where target is class_index of the target class.
        '''

        image, label = self.dataset[index] # Provide a way to access image and label via index
                           # Image should be a PIL Image
                           # label can be int
        #should be able already like this
        # Applies preprocessing when accessing the image - no changing
        if self.transform is not None:
            image = self.transform(image) 

        return image, label

    def __len__(self):
        '''
        The __len__ method returns the length of the dataset
        It is mandatory, as this is used by several other components
        '''
        length = len(self.dataset) # Provide a way to get the length (number of elements) of the dataset
        return length
