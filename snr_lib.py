import numpy as np

def puissance_signal(signal):
    puissance_image = 0
    for i in range(len(signal)):
        for j in range(len(signal[i])):
            puissance_image += abs(signal[i][j])**2
    return puissance_image

def puissance_bruit(signal, bruit):
    puissance_image = 0
    for i in range(len(signal)):
        for j in range(len(signal[i])):
            puissance_image += (signal[i][j]-bruit[i][j])**2

    return puissance_image

def SNR (signal, bruit):
    puissance_signal_val = puissance_signal(signal)
    puissance_bruit_val = puissance_bruit(signal, bruit)

    return 10*np.log10(puissance_signal_val/puissance_bruit_val)
