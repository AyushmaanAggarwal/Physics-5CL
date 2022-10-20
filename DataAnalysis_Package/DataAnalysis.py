# Data Analysis for Physics 5C Lab
# Written by Ayushmaan Aggarwal 
# Date Created: 9/13/2022

# Currently implemented features:
# Covariance, Variance, Standard Deviation, Correlation Coefficents

import numpy as np

def covariance(x, y):
    assert len(x) == len(y)
    u_x, u_y = np.mean(x), np.mean(y)
    sum_covar = 0
    for i in range(len(x)):
        sum_covar += (x[i]-u_x)*(y[i]-u_y)

    return sum_covar/(len(x)-1)

def variance(x):
    u_x = np.mean(x)
    sum_covar = 0
    for i in range(len(x)):
        sum_covar += (x[i]-u_x)**2

    return sum_covar/(len(x)-1)

def std(x):
    return (variance(x))**.5

def quartrature_sum(x):
    sum_quart = 0
    for val in x:
        sum_quart += val**2
    return sum_quart**.5

def correlation_coefficients(x,y):
    sigma_xy = covariance(x,y)
    sigma_x = np.sqrt(variance(x))
    sigma_y = np.sqrt(variance(y))
    return sigma_xy/(sigma_x*sigma_y)