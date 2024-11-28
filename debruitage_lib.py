import numpy as np
import contour_lib as contour
from skimage import feature

def debruitage_filtre_median(image, taille):
    
    if taille not in [3, 5]:
        print("Kernel non implémenté")
        exit()
        
    debruitage = np.zeros((len(image), len(image)))
    
    if taille == 3 :
        for i in range(1, len(image)-1):
            for j in range(1, len(image[i])-1) :
                pixels = [image[i+x][j+y] for x in range(-1, 2) for y in range(-1, 2)]
    else :
        for i in range(2, len(image)-2):
            for j in range(2, len(image[i])-2) :
                pixels = [image[i+x][j+y] for x in range(-2, 3) for y in range(-2, 3)]
        
    debruitage[i][j] = np.median(pixels)
            
    return debruitage

def debruitage_convolution(image, kernel, avecContour=None):
    kernel_size = len(kernel)
    if kernel_size not in [3, 5]:
        print("Kernel non implémenté")
        exit()
        
    if avecContour == "sobel" :
        image_contour = contour.contours_Sobel(image)
    elif avecContour == "canny" :
        image_contour = feature.canny(image, sigma=5)
    else :
        image_contour = np.zeros((len(image), len(image[0])))

    n = kernel_size // 2
    
    debruitage = np.copy(image)

    for i in range(n, image.shape[0] - n):
        for j in range(n, image.shape[1] - n):
            if image_contour[i][j] < 128 or image_contour[i][j] == False:
                nouveau_pixel = 0
                for ker_i in range(kernel_size):
                    for ker_j in range(kernel_size):
                        nouveau_pixel += image[i - n + ker_i][j - n + ker_j] * kernel[ker_i][ker_j]
                
                debruitage[i][j] = nouveau_pixel
            
    return debruitage
