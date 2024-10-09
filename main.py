import snr_lib as snr
import bruitage_lib as bruitage
import debruitage_lib as debruitage
import affichage as affiche
import tests as tests

import numpy as np
import matplotlib.pyplot as plt
import skimage as sk



image = sk.io.imread(fname='./images_reference/image1_reference.png')
image = image.astype(np.float64)

kernel = [[1,1,1],
          [1,1,1],
          [1,1,1]]

taux = [0.1,0.2,0.4,0.6]

            #################
            #   Sel Poivre  #
            #################

images_sel_poivre = []

for taux_valeur in (taux):
    image_sel_poivre = bruitage.bruitage_sel_poivre(image, taux_valeur)
    images_sel_poivre.append(image_sel_poivre)
    affiche.display_image(image_sel_poivre, "Bruitage Sel et Poivre Taux {}".format(taux_valeur))

meilleur_median = []
meilleur_convolution = []

meilleur_snr_median = -100
meilleur_snr_convolution = -100

snrs_median = []
snrs_convolution = []

for signal in (images_sel_poivre):
    median = debruitage.debruitage_filtre_median(signal)
    median_snr = snr.SNR(image,median)
    snrs_median.append(np.around(median_snr))
    if(median_snr > meilleur_snr_median):
        meilleur_snr_median = median_snr
        meilleur_median = median
    
    convolution = debruitage.debruitage_convolution(signal, kernel)
    convolution_snr = snr.SNR(image,convolution)
    snrs_convolution.append(np.around(convolution_snr))
    if (convolution_snr > meilleur_snr_convolution):
        meilleur_snr_convolution = convolution_snr
        meilleur_convolution = convolution
    
affiche.SNR_sur_bruitage(taux,snrs_median,snrs_convolution)
affiche.display_image(meilleur_median, "Bruitage Additif meilleure filtre median")
affiche.display_image(meilleur_convolution, "Bruitage Additif meilleure filtre convolution")

            #################
            #    Additif    #
            #################

images_additif = []

for taux_valeur in (taux):
    image_additif = bruitage.bruitage_additif(image, taux_valeur*100)
    images_additif.append(image_additif)
    affiche.display_image(image_additif, "Bruitage Additif Intensité {}".format(taux_valeur*100))

meilleur_median = []
meilleur_convolution = []

meilleur_snr_median = -100
meilleur_snr_convolution = -100

snrs_median = []
snrs_convolution = []

for signal in (images_additif):
    median = debruitage.debruitage_filtre_median(signal)
    median_snr = snr.SNR(image,median)
    snrs_median.append(np.around(median_snr))
    if(median_snr > meilleur_snr_median):
        meilleur_snr_median = median_snr
        meilleur_median = median
    
    convolution = debruitage.debruitage_convolution(signal, kernel)
    convolution_snr = snr.SNR(image,convolution)
    snrs_convolution.append(np.around(convolution_snr))
    if (convolution_snr > meilleur_snr_convolution):
        meilleur_snr_convolution = convolution_snr
        meilleur_convolution = convolution
    
affiche.SNR_sur_bruitage(taux,snrs_median,snrs_convolution)
affiche.display_image(meilleur_median, "Bruitage Additif meilleure filtre median")
affiche.display_image(meilleur_convolution, "Bruitage Additif meilleure filtre convolution")

            #################
            # Multiplicatif #
            #################

images_multiplicatif = []

for taux_valeur in (taux):
    image_multiplicatif = bruitage.bruitage_multiplicatif(image, taux_valeur)
    images_multiplicatif.append(image_multiplicatif)
    affiche.display_image(image_multiplicatif, "Bruitage Additif Intensité {}".format(taux_valeur))

meilleur_median = []
meilleur_convolution = []

meilleur_snr_median = -100
meilleur_snr_convolution = -100

snrs_median = []
snrs_convolution = []

for signal in (images_multiplicatif):
    median = debruitage.debruitage_filtre_median(signal)
    median_snr = snr.SNR(image,median)
    snrs_median.append(np.around(median_snr))
    if(median_snr > meilleur_snr_median):
        meilleur_snr_median = median_snr
        meilleur_median = median
    
    convolution = debruitage.debruitage_convolution(signal, kernel)
    convolution_snr = snr.SNR(image,convolution)
    snrs_convolution.append(np.around(convolution_snr))
    if (convolution_snr > meilleur_snr_convolution):
        meilleur_snr_convolution = convolution_snr
        meilleur_convolution = convolution
    
affiche.SNR_sur_bruitage(taux,snrs_median,snrs_convolution)
affiche.display_image(meilleur_median, "Bruitage multiplicatif meilleure filtre median")
affiche.display_image(meilleur_convolution, "Bruitage multiplicatif meilleure filtre convolution")

            #################
            #   Tests SNR   #
            #################

tests.tests_snr(image)