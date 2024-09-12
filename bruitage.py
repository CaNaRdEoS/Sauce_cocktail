# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:14:49 2024

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage
import random


def bruitage_additif(image, intensite):
    bruit = np.random.normal(0, intensite, image.shape)
    bruitage = image + bruit
    bruitage = np.clip(bruitage, 0, 255)
    return bruitage

def bruitage_multiplicatif(image, intensite):
    bruit = np.random.normal(0, intensite, image.shape)
    bruitage = image * (1 + bruit)
    bruitage = np.clip(bruitage, 0, 255)
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

def puissance(image):
    puissance_image = 0
    for i in range(len(image)):
        for j in range(len(image)):
            puissance_image += image[i][j]**2
    return puissance_image

def SNR (signal, bruit):
    return 10*np.log10(puissance(signal)/puissance(bruit))

def display_image(image, titre):
    skimage.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()
    print("La puissance de l'image ",titre," est de : ",puissance(image))

image = skimage.io.imread(fname='image.png')
display_image(image, "Image Originale")

image_sel_poivre = bruitage_sel_poivre(image, 0.1)
display_image(image_sel_poivre, "Bruitage Sel et Poivre")
print()

print("Signal sur bruit : ",SNR(image, image_sel_poivre))


image_additif = bruitage_additif(image, 10)
display_image(image_additif, "Buitage Additif")

image_multipli = bruitage_multiplicatif(image, 0.2)
display_image(image_multipli, "Buitage Multiplicatif")
