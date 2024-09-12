# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:14:49 2024

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage
import random


def bruitage_additif(image, taux):
    bruit = np.random.normal(0, taux, image.shape)
    bruitage = image + bruit
    return bruitage

def bruitage_multiplicatif(image, taux):
    bruit = np.random.normal(0, taux, image.shape)
    bruitage = image + (image * bruit)
    return bruitage

def bruitage_sel_poivre(image, taux):
    image_filtrer = np.zeros((len(image), len(image)))
    for i in range(len(image)) :
        for j in range(len(image[i])) :
            if random.randint(0, 100) <= taux * 100 :
                if random.randint(1, 2) == 1:
                    image_filtrer[i][j] = 255
                
            else :
                image_filtrer[i][j] = image[i][j]
                
    return image_filtrer


def display_images(image, titre):
    skimage.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()


image = skimage.io.imread(fname='image.png')
display_images(image, "Image Originale")

image_sel_poivre = bruitage_sel_poivre(image, 0.1)
display_images(image_sel_poivre, "Buitage Sel et Poivre")


image_additif = bruitage_additif(image, 0.1)
display_images(image_additif, "Buitage Additif")

image_multipli = bruitage_multiplicatif(image, 0.01)
display_images(image_multipli, "Buitage Multiplicatif")
