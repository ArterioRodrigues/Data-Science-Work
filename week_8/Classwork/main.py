"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8
I attended lecture today.
Row:  2
Seat:  72
"""

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA


def approxDigits(numComponents, coefficients, mean, components): 
    '''
    This function has four inputs and returns an array containing the approximation:
        numComponents: the number of componets used in the approximation. Expecting a value between 0 and 64.
        coefficients: an array of coefficients, outputted from PCA().
        mean: an array representing the mean of the dataset.
        components: an array of the components computed by PCA() analysis.
        The function returns the approximation image (flattened array) of the mean and sum of the first numComponents terms (i.e. coefficients[i] * components[i]).
    '''

    for num in range(numComponents):
        mult = coefficients[num] * components[num]
        mean = mean + mult

    return mean