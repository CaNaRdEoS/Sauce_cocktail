import numpy as np
import random as rd

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