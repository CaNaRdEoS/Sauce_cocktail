import matplotlib.pyplot as plt
import skimage as sk

def SNR_sur_bruitage(X_bruitage, titre, median3, median5, convolution):
    plt.title("Calcul du SNR par rapport au niveau de bruitage pour la méthode "+titre)
    plt.plot(X_bruitage, median3, label='Médian 3x3')
    plt.plot(X_bruitage, median5, label='Médian 5x5')
    plt.plot(X_bruitage, convolution, label='Convolution')
    plt.xlabel('Niveau de bruitage')
    plt.ylabel('SNR')
    plt.legend()
    plt.show()


def display_image(image, titre):
    sk.io.imshow(image, cmap="gray")
    plt.title(titre)
    plt.show()