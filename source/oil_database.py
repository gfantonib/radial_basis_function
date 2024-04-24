def oil_database(df_1, df_2, df_3, df_4):

	# 1
	df_op_1 = df_1.drop(columns=["REFERENCE"])
	column_ref_1 = df_1["REFERENCE"].astype(float)
	
	# 2
	df_op_2 = df_2.drop(columns=["REFERENCE"])
	column_ref_2 = df_2["REFERENCE"].astype(float)
	
	# 3
	df_op_3 = df_3.drop(columns=["REFERENCE"])
	column_ref_3 = df_3["REFERENCE"].astype(float)
	
	# 4
	df_4.iloc[6, 3] = 2.11
	df_op_4 = df_4.drop(columns=["REFERENCE"])
	column_ref_4 = df_4["REFERENCE"].astype(float)
	
	return df_op_1, df_op_2, df_op_3, df_op_4, \
		   column_ref_1, column_ref_2, column_ref_3, column_ref_4