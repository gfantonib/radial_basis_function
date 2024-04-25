import numpy as np
import pandas as pd

def generate_random_arrays_df(n, m, a, b):
    arrays = [np.random.uniform(a, b, size=m) for _ in range(n)]
    df = pd.DataFrame(arrays)
    return df

def select_poles(df_op):
	pole_size = len(df_op.columns)
	nbr_of_poles = pole_size + 1
	max_value = df_op.values.max()
	min_value = df_op.values.min()
	poles = generate_random_arrays_df(nbr_of_poles, pole_size, min_value, max_value)
	poles.loc[0] = 0
	return nbr_of_poles, poles

# How to find the maximum distance?
def calculate_euclidian_distance(poles):
	pole_distance = np.linalg.norm(poles.loc[1] - poles.loc[0])**2
	return pole_distance

def calculate_sigma(nbr_of_poles, pole_distance):
	sigma = np.sqrt(pole_distance) / np.sqrt(2 * nbr_of_poles)
	return sigma

def put_poles_in_database(row, poles, sigma, radial_function):
	df_main_matrix = poles.apply(radial_function, axis=1, args=(row, sigma))
	return df_main_matrix

def apply_radial_basis_function_in_database(df_op, nbr_of_poles, poles, sigma, radial_function):
	df_main_matrix = df_op.apply(put_poles_in_database, axis=1, args=(poles, sigma, radial_function))
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

def predict_line(row, nbr_of_poles, poles, sigma, a, radial_function):
	result = poles.apply(radial_function, axis=1, args=(row, sigma))
	df_result = np.dot(result.values, a[:nbr_of_poles]) + a[-1]
	return df_result

def predict_new_values(new_df_op, nbr_of_poles, poles, sigma, a, radial_function):
	result = new_df_op.apply(predict_line, axis=1, args=(nbr_of_poles, poles, sigma, a, radial_function))
	return result