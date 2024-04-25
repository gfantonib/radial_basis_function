import numpy as np

def distribute_poles(poles_row, data_row, sigma):
	gaussian_line = np.e**(-1/(2*(sigma**2)) * np.linalg.norm(data_row - poles_row)**2)
	return gaussian_line

def gaussian_function(row, poles, sigma):
	result = poles.apply(distribute_poles, axis=1, args=(row, sigma))
	print(result)
	return result

def truth_gaussian_function(row, pole_zero, pole_one, sigma, a):
	first_term = a[0] * np.e**(-1/(2*(sigma**2)) * np.linalg.norm(row - pole_zero)**2)
	second_term = a[1] * np.e**(-1/(2*(sigma**2)) * np.linalg.norm(row - pole_one)**2)
	third_term = a[2]
	result = first_term + second_term + third_term
	return result