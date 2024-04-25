#!/usr/bin/env python3

import pandas as pd

from source.oil_database import oil_database

from source.core_functions import select_poles
from source.core_functions import calculate_euclidian_distance
from source.core_functions import calculate_sigma
from source.core_functions import apply_radial_basis_function_in_database
from source.core_functions import calculate_pseudo_inverse
from source.core_functions import transform_column_ref_in_matrix
from source.core_functions import calculate_radial_basis_function_constants
from source.core_functions import predict_new_values

# main function
# Open database
df_1 = pd.read_excel("data/rbf_data_1.xlsx")
df_2 = pd.read_excel("data/rbf_data_2.xlsx")
df_3 = pd.read_excel("data/rbf_data_3.xlsx")
df_4 = pd.read_excel("data/rbf_data_4.xlsx")

# Treat database
df_op_1, df_op_2, df_op_3, df_op_4, \
column_ref_1, column_ref_2, column_ref_3, column_ref_4 = \
oil_database(df_1, df_2, df_3, df_4)

# Chose datas to be processed
df_op = df_op_4
column_ref = column_ref_4

# Algorithm core
nbr_of_poles, poles = select_poles(df_op)
print(poles)

pole_distance = calculate_euclidian_distance(pole_zero, pole_one)
exit(1)
sigma = calculate_sigma(nbr_of_poles, pole_distance)
R = apply_radial_basis_function_in_database(df_op, pole_zero, pole_one, sigma)
R_pseudo_inv = calculate_pseudo_inverse(R)
A = transform_column_ref_in_matrix(column_ref)
a = calculate_radial_basis_function_constants(R_pseudo_inv, A)

# Define datas to be predicted
df_op_to_predic = df_op

# Predict data reference
prediction = predict_new_values(df_op_to_predic, pole_zero, pole_one, sigma, a)
print(prediction)