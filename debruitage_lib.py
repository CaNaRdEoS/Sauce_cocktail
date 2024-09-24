import numpy as np

def debruitage_filtre_median(image):
    debruitage = np.zeros((len(image), len(image)))
    
    for i in range(2, len(image)-2):
        for j in range(2, len(image[i])-2) :
            pixels = [image[i+x][j+y] for x in range(-2, 3) for y in range(-2, 3)]
    
            debruitage[i][j] = np.median(pixels)
            
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