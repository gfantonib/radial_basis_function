import numpy as np

def distribute_poles(poles_row, data_row, sigma):
	gaussian_line = np.e**(-1/(2*(sigma**2)) * np.linalg.norm(data_row.values - poles_row.values)**2)
	return gaussian_line

def gaussian_function(row, poles, sigma):
	df_main_matrix = poles.apply(distribute_poles, axis=1, args=(row, sigma))
	return df_main_matrix

def truth_gaussian_function(row, nbr_of_poles, poles, sigma, a):
	result = poles.apply(distribute_poles, axis=1, args=(row, sigma))
	df_result = np.dot(result.values, a[:nbr_of_poles]) + a[-1]
	return df_result