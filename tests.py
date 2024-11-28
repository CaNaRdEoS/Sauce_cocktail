import snr_lib as snr
import skimage as sk
import numpy as np

def tests_snr(image):
	bruit9  = sk.io.imread(fname='./images_reference/image1_bruitee_snr_9.2885.png').astype(np.float64)
	bruit41 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_41.8939.png').astype(np.float64)
	bruit36 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_36.1414.png').astype(np.float64)
	bruit32 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_32.6777.png').astype(np.float64)
	bruit28 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_28.2378.png').astype(np.float64)
	bruit22 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_22.2912.png').astype(np.float64)
	bruit16 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_16.4138.png').astype(np.float64)
	bruit13 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_13.0913.png').astype(np.float64)
	bruit10 = sk.io.imread(fname='./images_reference/image1_bruitee_snr_10.8656.png').astype(np.float64)

	print("Tests des images SNR de test")
	print(np.around(snr.SNR(image,bruit9)))
	print(np.around(snr.SNR(image,bruit41)))
	print(np.around(snr.SNR(image,bruit36)))
	print(np.around(snr.SNR(image,bruit32)))
	print(np.around(snr.SNR(image,bruit28)))
	print(np.around(snr.SNR(image,bruit22)))
	print(np.around(snr.SNR(image,bruit16)))
	print(np.around(snr.SNR(image,bruit13)))
	print(np.around(snr.SNR(image,bruit10)))