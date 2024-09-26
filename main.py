import snr_lib as snr
import bruitage_lib as bruitage
import debruitage_lib as debruitage
import graphiques as graph

import numpy as np
import matplotlib.pyplot as plt
import skimage as sk

def display_image(image, titre):
    sk.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()

image = sk.io.imread(fname='./images_reference/image1_reference.png')
image = image.astype(np.float64)

kernel = [[1,1,1],
        [1,1,1],
        [1,1,1]]

###############################################################################
# SEL POIVRE

images_sel_poivre = []

for taux in range(1, 8,2):
    image_sel_poivre = bruitage.bruitage_sel_poivre(image, taux/10)
    images_sel_poivre.append(image_sel_poivre)
    display_image(image_sel_poivre, "Bruitage Sel et Poivre Taux {}".format(taux/10))

convolution = debruitage.debruitage_convolution(images_sel_poivre[0], kernel)
print(np.around(snr.SNR(image,convolution)))
display_image(convolution, "Debruitage Convolution Sel et Poivre")

'''
snr_median =[]
snr_convolution =[]

for i in range(0,len(images_sel_poivre)):
    median = debruitage.debruitage_filtre_median(images_sel_poivre[i])
    snr_median.append(np.around(snr.SNR(image,median)))
    convolution = debruitage.debruitage_convolution(images_sel_poivre[i], kernel)
    snr_convolution.append(np.around(snr.SNR(image,convolution)))

graph.SNR_sur_bruitage([0.1,0.3,0.5,0.7],snr_median,snr_convolution)


# Affichage des meilleurs cas
display_image(median, "Debruitage Sel et Poivre")
display_image(convolution, "Debruitage Convolution Sel et Poivre")


###############################################################################
# Additif
image_additif = bruitage.bruitage_additif(image, 30)
display_image(image_additif, "Buitage Additif")

debruitage_additif = debruitage.debruitage_filtre_median(image_additif)
display_image(debruitage_additif, "Debruitage Additif Median")

convolution_additif = debruitage.debruitage_convolution(image_additif, kernel)
display_image(convolution_additif, "Debruitage Convolution Additif")

###############################################################################
# Multiplicatif
image_multipli = bruitage.bruitage_multiplicatif(image, 1)
display_image(image_multipli, "Buitage Multiplicatif")

debruitage_multipli = debruitage.debruitage_filtre_median(image_multipli)
display_image(debruitage_multipli, "Debruitage Multiplicatif Median")

convolution_multipli = debruitage.debruitage_convolution(image_multipli, kernel)
display_image(convolution_multipli, "Debruitage Convolution Multiplicatif")

#-------------- Tests de la fonciton SNR --------------#
bruit9  = sk.io.imread(fname='./images_reference/image1_bruitee_snr_9.2885.png').astype(np.float64)
bruit41 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_41.8939.png').astype(np.float64)
bruit36 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_36.1414.png').astype(np.float64)
print("Tests des images SNR de test")
print(np.around(snr.SNR(image,bruit9)))
print(np.around(snr.SNR(image,bruit41)))
print(np.around(snr.SNR(image,bruit36)))



#graph.SNR_sur_bruitage(X,Y,Z)

'''