import numpy as np
import pandas as pd

from .radial_functions import gaussian_function
from .radial_functions import truth_gaussian_function

def select_poles(df_op):
	pole_size = len(df_op.columns)
	nbr_of_poles = pole_size + 1
	poles = df_op.sample(nbr_of_poles)
	poles = poles.reset_index(drop=True)
	poles.loc[0] = 0
	return nbr_of_poles, poles

# How to find the maximum distance?
def calculate_euclidian_distance(poles):
	pole_distance = np.linalg.norm(poles.loc[1] - poles.loc[0])**2
	return pole_distance

def calculate_sigma(nbr_of_poles, pole_distance):
	sigma = np.sqrt(pole_distance) / np.sqrt(2 * nbr_of_poles)
	return sigma

def apply_radial_basis_function_in_database(df_op, nbr_of_poles, poles, sigma):
	df_main_matrix = df_op.apply(gaussian_function, axis=1, args=(poles, sigma))
	print(df_main_matrix)
	df_main_matrix[f"{nbr_of_poles}"] = 1
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

def predict_new_values(new_df_op, nbr_of_poles, poles, sigma, a):
	result = new_df_op.apply(truth_gaussian_function, axis=1, args=(nbr_of_poles, poles, sigma, a))
	return result