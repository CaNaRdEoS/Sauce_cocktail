import snr_lib as snr
import bruitage_lib as bruitage
import debruitage_lib as debruitage
import contour_lib as contour
import affichage as affiche
import tests as tests

import numpy as np
import skimage as sk
from skimage import feature

# Charger l'image de référence
def charger_image(fichier):
    image = sk.io.imread(fname=fichier)
    return image.astype(np.float64)

# Appliquer le bruitage et afficher les images
def appliquer_bruitage(image, taux, type_bruitage, facteur=1):
    images_bruit = []
    for taux_valeur in taux:
        if type_bruitage == 'sel_poivre':
            image_bruit = bruitage.bruitage_sel_poivre(image, taux_valeur)
            affiche.display_image(image_bruit, f"Bruitage Sel et Poivre Taux {taux_valeur}")
        elif type_bruitage == 'additif':
            image_bruit = bruitage.bruitage_additif(image, taux_valeur * facteur)
            affiche.display_image(image_bruit, f"Bruitage Additif Intensité {taux_valeur * facteur}")
        elif type_bruitage == 'multiplicatif':
            image_bruit = bruitage.bruitage_multiplicatif(image, taux_valeur)
            affiche.display_image(image_bruit, f"Bruitage Multiplicatif Intensité {taux_valeur}")
        images_bruit.append(image_bruit)
    return images_bruit

# Évaluer le SNR et trouver les meilleurs filtres
def evaluer_snr(image, images_bruit, kernel):
def evaluer_snr(image, images_bruit, kernel1, kernel2):
    snrs_median3 = []
    snrs_median5 = []
    snrs_convolution1 = []
    snrs_convolutio2 = []
    meilleur_median3, meilleur_median5, meilleur_convolution = None, None, None
    meilleur_snr_median3, meilleur_snr_median5, meilleur_snr_convolution1, meilleur_snr_convolution2 = -100, -100, -100, -100

    for signal in images_bruit:
        # Filtre médian 3x3
        median = debruitage.debruitage_filtre_median(signal, 3)
        median_snr = snr.SNR(image, median)
        snrs_median3.append(np.around(median_snr))
        if median_snr > meilleur_snr_median3:
            meilleur_snr_median3 = median_snr
            meilleur_median3 = median
        

        # Filtre médian 5x5
        median = debruitage.debruitage_filtre_median(signal, 5)
        median_snr = snr.SNR(image, median)
        snrs_median5.append(np.around(median_snr))
        if median_snr > meilleur_snr_median5:
            meilleur_snr_median5 = median_snr
            meilleur_median5 = median
        
        # Filtre convolution SIGMA 0.2
        convolution = debruitage.debruitage_convolution(signal, kernel1)
        convolution_snr = snr.SNR(image, convolution)
        snrs_convolution1.append(np.around(convolution_snr))
        if convolution_snr > meilleur_snr_convolution1:
            meilleur_snr_convolution1 = convolution_snr
            meilleur_convolution1 = convolution

        # Filtre convolution SIGMA 0.8
        convolution = debruitage.debruitage_convolution(signal, kernel2)
        convolution_snr = snr.SNR(image, convolution)
        snrs_convolution2.append(np.around(convolution_snr))
        if convolution_snr > meilleur_snr_convolution2:
            meilleur_snr_convolution2 = convolution_snr
            meilleur_convolution2 = convolution

    return snrs_median3, snrs_median5, snrs_convolution1, snrs_convolution2, meilleur_median3, meilleur_median5, meilleur_convolution1, meilleur_convolution2

# Processus principal de traitement du bruitage et du débruitage
def traitement_bruit(image, taux, kernel1, kernel2, type_bruitage, facteur=1):
    print(f"Traitement du bruitage {type_bruitage.capitalize()}...")
    images_bruit = appliquer_bruitage(image, taux, type_bruitage, facteur)
    snrs_median3, snrs_median5, snrs_convolution1, snrs_convolution2, meilleur_median3, meilleur_median5, meilleur_convolution1, meilleur_convolution2 = evaluer_snr(image, images_bruit, kernel1, kernel2)
    affiche.SNR_sur_bruitage(taux, type_bruitage,snrs_median3, snrs_median5, snrs_convolution)
    affiche.display_image(meilleur_median3, f"Meilleur filtre médian pour {type_bruitage}")
    affiche.display_image(meilleur_median5, f"Meilleur filtre médian pour {type_bruitage}")
    affiche.display_image(meilleur_convolution, f"Meilleur filtre convolution pour {type_bruitage}")

# Paramètres
taux = [0.1, 0.2, 0.4, 0.6]
kernel = []

def gaussian(x, y, x0, y0, sigma):
    return (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

somme = 0
for i in range(5):
    ligne = []
    for j in range(5):
        somme += gaussian(i, j, 2, 2, 0.8)
        ligne.append(gaussian(i, j, 2, 2, 0.8))
    kernel.append(ligne)


# Charger l'image
image = charger_image('./images_reference/image1_reference.png')

# Tests SNR
tests.tests_snr(image)


# Traitement pour chaque type de bruitage
traitement_bruit(image, taux, kernel, 'sel_poivre')
traitement_bruit(image, taux, kernel, 'additif', facteur=100)
traitement_bruit(image, taux, kernel, 'multiplicatif')


#Bonus

# Detection des contours
image_sobel = contour.contours_Sobel(image)
image_canny = feature.canny(image, 5)

affiche.display_image(image_sobel, "Contours de l'image Sobel")
affiche.display_image(image_canny, "Contours de l'image Canny")


#Debruitage adaptatif
bruitage = bruitage.bruitage_multiplicatif(image, 0.3)
debruitage_canny = debruitage.debruitage_convolution(bruitage, kernel, "canny")
debruitage_sobel = debruitage.debruitage_convolution(bruitage, kernel, "sobel")

affiche.display_image(bruitage, "Image bruité")
affiche.display_image(debruitage_canny, "Image débruité Canny")
affiche.display_image(debruitage_sobel, "Image débruité Sobel")
