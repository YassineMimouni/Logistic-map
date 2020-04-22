from LogisticEquation.Logistic_and_vectorization import Logistic_equation
from Mandelbrot2D.Mandelbrot2D import Mandelbrot_2D
import numpy as np

le = Logistic_equation(n=1)
m2 = Mandelbrot_2D(largeur=2,hauteur=2,max_iteration=4,xmin=1, xmax=2, ymin=1, ymax=2)

def test_logistic():
    assert le.logistic(2, 1) == 0

def test_vectorization():
    assert le.vectorization(1,2) == [(1, 0), (1, 0), (0, 0)]

def test_mandelbrotset():
    assert np.any(m2.Mandelbrotset() == [[1, 1], [1, 1]])
