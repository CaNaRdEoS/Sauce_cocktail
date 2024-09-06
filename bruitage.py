# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:14:49 2024

@author: romain
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.filters
from skimage.util import random_noise 

def bruitage_additive(image, taux):
    return 0

def bruitage_sel_poivre(image, taux):
    image_filtrer = random_noise(image, mode='s&p', amount=taux)
    return image_filtrer


image = skimage.io.imread(fname='image.png')
image_sel_poivre = bruitage_sel_poivre(image, 0.1)
skimage.io.imshow(image_sel_poivre)