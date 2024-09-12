# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:14:49 2024

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage
import random

##♥     BRUITAGE
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

##      CALCUL DU SNR
def puissance(image):
    puissance_image = 0
    for i in range(len(image)):
        for j in range(len(image)):
            puissance_image += image[i][j]**2
    return puissance_image

def SNR (signal, bruit):
    return 10*np.log10(puissance(signal)/puissance(bruit))

##      DEBRUITAGE

def debruitage_filtre_median(image):
    debruitage = np.zeros((len(image), len(image)))
    
    for i in range(2, len(image)-2):
        for j in range(2, len(image[i])-2) :
            pixels = [image[i-2][j-2], image[i-2][j-1], image[i-2][j], image[i-2][j+1], image[i-2][j+2],
                      image[i-1][j-2], image[i-1][j-1], image[i-1][j], image[i-1][j+1], image[i-1][j+2],
                      image[i][j-2], image[i][j-1], image[i][j], image[i][j+1], image[i][j+2],
                      image[i+1][j-2], image[i+1][j-1], image[i+1][j], image[i+1][j+1], image[i+1][j+2],
                      image[i+2][j-2], image[i+2][j-1], image[i+2][j], image[i+2][j+1], image[i+2][j+2]]
    
            pixels.sort()
            debruitage[i][j] = pixels[len(pixels)//2]
            
    return debruitage
                      

def display_image(image, titre):
    skimage.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()
    print("La puissance de l'image ",titre," est de : ",puissance(image))

image = skimage.io.imread(fname='image.png')
display_image(image, "Image Originale")

image_sel_poivre = bruitage_sel_poivre(image, 0.1)
display_image(image_sel_poivre, "Bruitage Sel et Poivre")
print("Signal sur bruit : ",SNR(image, image_sel_poivre))
debruitage_sel_poivre = debruitage_filtre_median(image_sel_poivre)
display_image(debruitage_sel_poivre, "Debruitage Sel et Poivre")


image_additif = bruitage_additif(image, 30)
display_image(image_additif, "Buitage Additif")
debruitage_additif = debruitage_filtre_median(image_additif)
display_image(debruitage_additif, "Debruitage Additif")

image_multipli = bruitage_multiplicatif(image, 0.2)
display_image(image_multipli, "Buitage Multiplicatif")
debruitage_multipli = debruitage_filtre_median(image_multipli)
display_image(debruitage_multipli, "Debruitage Multiplicatif")
