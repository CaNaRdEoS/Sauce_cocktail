import snr_lib as snr
import bruitage_lib as bruitage
import debruitage_lib as debruitage
import affichage as affiche
import tests as tests

import numpy as np
import skimage as sk

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
    snrs_median = []
    snrs_convolution = []
    meilleur_median, meilleur_convolution = None, None
    meilleur_snr_median, meilleur_snr_convolution = -100, -100

    for signal in images_bruit:
        # Filtre médian
        median = debruitage.debruitage_filtre_median(signal)
        median_snr = snr.SNR(image, median)
        snrs_median.append(np.around(median_snr))
        if median_snr > meilleur_snr_median:
            meilleur_snr_median = median_snr
            meilleur_median = median
        
        # Filtre convolution
        convolution = debruitage.debruitage_convolution(signal, kernel)
        convolution_snr = snr.SNR(image, convolution)
        snrs_convolution.append(np.around(convolution_snr))
        if convolution_snr > meilleur_snr_convolution:
            meilleur_snr_convolution = convolution_snr
            meilleur_convolution = convolution

    return snrs_median, snrs_convolution, meilleur_median, meilleur_convolution

# Processus principal de traitement du bruitage et du débruitage
def traitement_bruit(image, taux, kernel, type_bruitage, facteur=1):
    print(f"Traitement du bruitage {type_bruitage.capitalize()}...")
    images_bruit = appliquer_bruitage(image, taux, type_bruitage, facteur)
    snrs_median, snrs_convolution, meilleur_median, meilleur_convolution = evaluer_snr(image, images_bruit, kernel)
    affiche.SNR_sur_bruitage(taux, type_bruitage, snrs_median, snrs_convolution)
    affiche.display_image(meilleur_median, f"Meilleur filtre médian pour {type_bruitage}")
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

print(somme)
# Charger l'image
image = sk.io.imread(fname='./images_reference/image1_reference.png')
image = image.astype(np.float64)

# Traitement pour chaque type de bruitage
traitement_bruit(image, taux, kernel, 'sel_poivre')
traitement_bruit(image, taux, kernel, 'additif', facteur=100)
traitement_bruit(image, taux, kernel, 'multiplicatif')

# Tests SNR
tests.tests_snr(image)
