#!/usr/bin/env python3

import pandas as pd

# Import function that treat the database.
from source.oil_database import oil_database

# Import core functions.
from source.core_functions import select_poles
from source.core_functions import calculate_euclidian_distance
from source.core_functions import calculate_sigma
from source.core_functions import apply_radial_basis_function_in_database
from source.core_functions import calculate_pseudo_inverse
from source.core_functions import transform_column_ref_in_matrix
from source.core_functions import calculate_radial_basis_function_constants
from source.core_functions import predict_new_values

# Import radial functions
from source.radial_functions import gaussian_function
from source.radial_functions import multiquadratic_function
from source.radial_functions import versiera_function
from source.radial_functions import reciprocal_multiquadratic_function

# main function.
# Open database.
df_1 = pd.read_excel("data/rbf_data_1.xlsx")
df_2 = pd.read_excel("data/rbf_data_2.xlsx")
df_3 = pd.read_excel("data/rbf_data_3.xlsx")
df_4 = pd.read_excel("data/rbf_data_4.xlsx")

# Treat database.
df_op_1, df_op_2, df_op_3, df_op_4, \
column_ref_1, column_ref_2, column_ref_3, column_ref_4 = \
oil_database(df_1, df_2, df_3, df_4)

# Chose data to be processed.
df_op = df_op_3
column_ref = column_ref_3

# Chose radial function.
radial_function = reciprocal_multiquadratic_function

# Algorithm core.
nbr_of_poles, poles = select_poles(df_op)
pole_distance = calculate_euclidian_distance(poles)
sigma = calculate_sigma(nbr_of_poles, pole_distance)
R = apply_radial_basis_function_in_database(df_op, nbr_of_poles, poles, sigma, radial_function)
R_pseudo_inv = calculate_pseudo_inverse(R)
A = transform_column_ref_in_matrix(column_ref)
a = calculate_radial_basis_function_constants(R_pseudo_inv, A)

# Define datas to be predicted.
df_op_to_predic = df_op

# Predict data reference.
prediction = predict_new_values(df_op_to_predic, nbr_of_poles, poles, sigma, a, radial_function)
print(prediction)