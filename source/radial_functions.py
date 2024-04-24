import numpy as np

def gaussian_function(row, pole_zero, pole_one, sigma):
	result1 = np.e**(-1/(2*(sigma**2)) * np.linalg.norm(row - pole_zero)**2)
	result2 = np.e**(-1/(2*(sigma**2)) * np.linalg.norm(row - pole_one)**2)
	return result1, result2

def truth_gaussian_function(row, pole_zero, pole_one, sigma, a):
	first_term = a[0] * np.e**(-1/(2*(sigma**2)) * np.linalg.norm(row - pole_zero)**2)
	second_term = a[1] * np.e**(-1/(2*(sigma**2)) * np.linalg.norm(row - pole_one)**2)
	third_term = a[2]
	result = first_term + second_term + third_term
	return result