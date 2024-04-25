import numpy as np

# Gaussian function
def gaussian_function(poles_row, data_row, sigma):
	gaussian_line = np.e**(-1/(2*(sigma**2)) * np.linalg.norm(data_row.values - poles_row.values)**2)
	return gaussian_line

# Multiquadratic function
def multiquadratic_function(poles_row, data_row, sigma):
	multiquadratic_line = np.sqrt(1 + sigma**2 * np.linalg.norm(data_row.values - poles_row.values)**2)
	return multiquadratic_line

# Versiera function
def versiera_function(poles_row, data_row, sigma):
	versiera_line = 1 / (1 + sigma**2 * np.linalg.norm(data_row.values - poles_row.values)**2)
	return versiera_line

# Reciprocal multiquadratic function
def reciprocal_multiquadratic_function(poles_row, data_row, sigma):
	reciprocal_multiquadratic_line = 1 / np.sqrt(1 + sigma**2 * np.linalg.norm(data_row.values - poles_row.values)**2)
	return reciprocal_multiquadratic_line


