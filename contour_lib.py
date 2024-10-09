import numpy as np
import debruitage_lib as debruitage

def contours_Sobel(image):
      print("Détection des contours en cours")
      Gx = [[1,0,-1],
            [2,0,-2],
            [1,0,-1]]

      Gy = [[1 , 2, 1],
            [0 , 0, 0],
            [-1,-2,-1]]

      GxA = debruitage.debruitage_convolution(image, Gx)
      GyA = debruitage.debruitage_convolution(image, Gy)
      
      return np.sqrt(GxA**2 + GyA**2)