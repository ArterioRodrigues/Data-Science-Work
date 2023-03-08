"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8
I attended lecture today.
Row:  2
Seat:  72
"""
import numpy as np
from scipy.stats import norm



def compute_smoothing(xes,points):
    '''
    This function takes a numpy array xes and a list, points, of numeric values.
    For each p in points, the function should compute the normal probability distribution
    function (scipy.norm.pdf) centered at loc = p with standard deviation scale = 0.5
    for all values in xes. The return value is a numpy array of the sum of these at each point.
    '''

    res = []
    sum = np.zeros(len(xes)) 
    
    for i in points:
        res = norm.pdf(xes, i, 0.5)
        for j in range(len(res)):
            sum[j] += res[j]

    return sum

