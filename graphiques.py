import matplotlib.pyplot as plt

def SNR_sur_bruitage(X_bruitage, Y_SNR, Z_SNR):

	plt.plot(X_bruitage,Y_SNR,label='Convolution')
	plt.plot(X_bruitage,Z_SNR,label='Médian')
	plt.xlabel('Niveau de bruitage')
	plt.ylabel('SNR')
	plt.legend()
	plt.show()