import numpy as np

def puissance_signal(image):
    puissance_image = 0
    for i in range(len(image)):
        for j in range(len(image[i])):
            puissance_image += abs(image[i][j])**2
    return puissance_image

def puissance_bruit(signal, bruit):
    puissance_image = 0
    for i in range(len(signal)):
        for j in range(len(signal[i])):
            if (bruit[i][j] <= signal[i][j]):
                puissance_image += (signal[i][j]-bruit[i][j])**2
            else:
                puissance_image += (bruit[i][j]-signal[i][j])**2

            
    return puissance_image

def SNR (signal, bruit):

    return 10*np.log10(puissance_signal(signal)/puissance_bruit(signal, bruit))
