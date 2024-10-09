import matplotlib.pyplot as plt
import skimage as sk

def SNR_sur_bruitage(X_bruitage, titre, Y_SNR, Z_SNR):
    plt.title("Calcul du SNR par rapport au niveau de bruitage pour la méthode "+titre)
    plt.plot(X_bruitage, Y_SNR, label='Médian')
    plt.plot(X_bruitage, Z_SNR, label='Convolution')
    plt.xlabel('Niveau de bruitage')
    plt.ylabel('SNR')
    plt.legend()
    plt.show()


def display_image(image, titre):
    sk.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()