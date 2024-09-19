# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:14:49 2024

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
import random as rd

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
            if rd.randint(0, 100) <= taux * 100 :
                if rd.randint(1, 2) == 1:
                    image_filtrer[i][j] = 255
                
            else :
                image_filtrer[i][j] = image[i][j]
                
    return image_filtrer

def puissance_signal(image):
    puissance_image = 0
    for i in range(len(image)):
        for j in range(len(image[i])):
            puissance_image += image[i][j]**2
    return puissance_image

def puissance_bruit(signal, bruit):
    puissance_image = 0
    for i in range(len(signal)):
        for j in range(len(signal[i])):
            if (bruit[i][j] <= signal[i][j]):
                puissance_image += (signal[i][j]-bruit[i][j])**2
            else:
                puissance_image += (bruit[i][j]-signal[i][j])**2

            
    return puissance_image

def SNR (signal, bruit):
    return 10*np.log10(puissance_signal(signal)/puissance_bruit(signal, bruit))

##      DEBRUITAGE

def debruitage_filtre_median(image):
    debruitage = np.zeros((len(image), len(image)))
    
    for i in range(2, len(image)-2):
        for j in range(2, len(image[i])-2):
            pixels = [image[i-2][j-2], image[i-2][j-1], image[i-2][j], image[i-2][j+1], image[i-2][j+2],
                      image[i-1][j-2], image[i-1][j-1], image[i-1][j], image[i-1][j+1], image[i-1][j+2],
                      image[i][j-2], image[i][j-1], image[i][j], image[i][j+1], image[i][j+2],
                      image[i+1][j-2], image[i+1][j-1], image[i+1][j], image[i+1][j+1], image[i+1][j+2],
                      image[i+2][j-2], image[i+2][j-1], image[i+2][j], image[i+2][j+1], image[i+2][j+2]]
    
            pixels.sort()
            debruitage[i][j] = pixels[len(pixels)//2]
            
    return debruitage

def debruitage_convolution(image, kernel):
    debruitage = np.zeros((len(image), len(image)))

    for i in range(2, len(image)-2):
        for j in range(2, len(image[i])-2):
            nouveau_pixel = 0

            for ker in range(len(kernel)):
                for nel in range(len(kernel[ker])):
                    nouveau_pixel += image[i-ker-1][j-nel-1]*kernel[ker][nel]
            debruitage[i][j] = nouveau_pixel
            
    return debruitage
                      

def display_image(image, titre):
    sk.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()

image = sk.io.imread(fname='./images_reference/image1_reference.png')
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

#Tests de SNR
bruit9  = sk.io.imread(fname='./images_reference/image1_bruitee_snr_9.2885.png')
bruit41 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_41.8939.png')
bruit36 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_36.1414.png')
print("Tests des images SNR de test")
print(np.around(SNR(image,bruit9)))
print(np.around(SNR(image,bruit41)))
print(np.around(SNR(image,bruit36)))