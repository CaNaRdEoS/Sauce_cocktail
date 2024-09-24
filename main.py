import snr_lib as snr
import bruitage_lib as bruitage
import debruitage_lib as debruitage

import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
import random as rd

def display_image(image, titre):
    sk.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()

image = sk.io.imread(fname='./images_reference/image1_reference.png')
#np.float_ n'existe plus dans la dernière version de numpy
#image = image.astype(np.float_)
image = image.astype(np.float64)

kernel = [[1,1,1],
        [1,1,1],
        [1,1,1]]

image_sel_poivre = bruitage.bruitage_sel_poivre(image, 0.1)
display_image(image_sel_poivre, "Bruitage Sel et Poivre")
print("Signal sur bruit : ",snr.SNR(image, image_sel_poivre))
debruitage_sel_poivre = debruitage.debruitage_filtre_median(image_sel_poivre)
display_image(debruitage_sel_poivre, "Debruitage Sel et Poivre")


image_additif = bruitage.bruitage_additif(image, 30)
display_image(image_additif, "Buitage Additif")
debruitage_additif = debruitage.debruitage_filtre_median(image_additif)
display_image(debruitage_additif, "Debruitage Additif")

convolution = debruitage.debruitage_convolution(image_additif, kernel)
display_image(convolution, "Debruitage Convolution Sel et Poivre")

image_multipli = bruitage.bruitage_multiplicatif(image, 0.2)
display_image(image_multipli, "Buitage Multiplicatif")
debruitage_multipli = debruitage.debruitage_filtre_median(image_multipli)
display_image(debruitage_multipli, "Debruitage Multiplicatif")

#-------------- Tests de la fonciton SNR --------------#
#np.float_ n'existe plus dans la dernière version de numpy
bruit9  = sk.io.imread(fname='./images_reference/image1_bruitee_snr_9.2885.png').astype(np.float64)
bruit41 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_41.8939.png').astype(np.float64)
bruit36 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_36.1414.png').astype(np.float64)
print("Tests des images SNR de test")
print(np.around(snr.SNR(image,bruit9)))
print(np.around(snr.SNR(image,bruit41)))
print(np.around(snr.SNR(image,bruit36)))