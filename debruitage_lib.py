import numpy as np

def debruitage_filtre_median(image):
    debruitage = np.zeros((len(image), len(image)))
    
    for i in range(2, len(image)-2):
        for j in range(2, len(image[i])-2) :
            pixels = [image[i+x][j+y] for x in range(-2, 3) for y in range(-2, 3)]
    
            debruitage[i][j] = np.median(pixels)
            
    return debruitage

def debruitage_convolution(image, kernel):
    kernel_size = len(kernel)
    if kernel_size not in [3, 5]:
        print("Kernel non implémenté")
        exit()

    n = kernel_size // 2
    
    debruitage = np.copy(image)

    for i in range(n, image.shape[0] - n):
        for j in range(n, image.shape[1] - n):
            nouveau_pixel = 0
            for ker_i in range(kernel_size):
                for ker_j in range(kernel_size):
                    nouveau_pixel += image[i - n + ker_i][j - n + ker_j] * kernel[ker_i][ker_j]
            
            debruitage[i][j] = nouveau_pixel
            
    return debruitage
