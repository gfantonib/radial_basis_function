import numpy as np
import pandas as pd

from .radial_functions import gaussian_function
from .radial_functions import truth_gaussian_function

def select_two_poles(df_op):
	pole_size = len(df_op.columns)
	pole_zero = np.zeros(pole_size)
	pole_one = df_op.max().values
	nbr_of_poles = 2
	return nbr_of_poles, pole_zero, pole_one

def calculate_euclidian_distance(pole_zero, pole_one):
	pole_distance = np.linalg.norm(pole_one - pole_zero)**2
	return pole_distance

def calculate_sigma(nbr_of_poles, pole_distance):
	sigma = np.sqrt(pole_distance) / np.sqrt(2 * nbr_of_poles)
	return sigma

def apply_radial_basis_function_in_database(df_op, pole_zero, pole_one, sigma):
	tuple_series = df_op.apply(gaussian_function, axis=1, args=(pole_zero, pole_one, sigma))
	df_main_matrix = pd.DataFrame(tuple_series.tolist(), columns=['Column 1', 'Column 2'])
	df_main_matrix["Column 3"] = 1
	R = df_main_matrix.values
	return R

def calculate_pseudo_inverse(R):
	R_pseudo_inv = np.dot(np.linalg.inv(np.dot(R.T, R)), R.T)
	return R_pseudo_inv

def transform_column_ref_in_matrix(column_ref):
	A = column_ref.to_numpy().reshape(-1, 1)
	return A

def calculate_radial_basis_function_constants(R_pseudo_inv, A):
	a = np.dot(R_pseudo_inv, A)
	return a

def predict_new_values(new_df_op, pole_zero, pole_one, sigma, a):
	result = new_df_op.apply(truth_gaussian_function, axis=1, args=(pole_zero, pole_one, sigma, a))
	return result