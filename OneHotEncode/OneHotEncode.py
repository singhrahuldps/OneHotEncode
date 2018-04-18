def OneHotEncode(pandas_dataframe,category_columns=[],check_numerical=False,max_var=None):
	# Parameter explanation ----
	# pandas_dataframe -> The Pandas Dataframe object that contains the column you want to one-hot encode
	# category_columns -> List of column names in pandas_dataframe that you want to one-hot encode
	# override_alert (Default=False) -> A naive way of checking if the column contains numerical
	#                                   data or is unsuitable for one-hot encoding
	#                                   Set it to True to turn on the detection

	import numpy as numpylib

	# The dataframe is copied to a new variable
	df=pandas_dataframe.copy()

	# List of list of names of all new columns made for a single column 
	all_new_cols=[]

	# List of dictionary of names of all new columns made for a single column
	new_col_dict=[]

	# List of arrays containg the dropped columns that were originally input
	dropped_cols=[]

	numerical_const=20
	
	for col in category_columns:

		# Total number of rows in each column
		total_rows=len(df[category_columns[0]].values)

		category_elements=[]
		main_row=df[str(col)].values
		for category_element in main_row:
			category_elements.append(category_element)
		category_elements=list(set(category_elements))

		if check_numerical:
			if max_var!=None:
				if len(category_elements) > max_var:
					print(col+' not suitable for One-Hot Encoding')
					continue
			else:
				if len(category_elements)>numerical_const:
					print(col+' has more variables than permitted')
					continue
		
		if max_var != None:
			if len(category_elements) > max_var:
					print(col+' has more variables than allowed')
					continue

		category_element_dict={}
		for i in range(len(category_elements)):
			category_element_dict[category_elements[i]]=i

		category_element_reverse_dict={}
		for i in range(len(category_elements)):
			category_element_reverse_dict[col+str(i)]=category_elements[i]

		dict_new_columns={}

		category_element_str = [(col+str(x)) for x in range(len(category_elements))]
		for string in category_element_str:
			zero_row=numpylib.zeros((total_rows,), dtype=numpylib.int)
			dict_new_columns[string]=zero_row

		colnames=[]
		for i in range(total_rows):
			colnames.append(category_element_str[category_element_dict[main_row[i]]])
		for i in range(total_rows):
			dict_new_columns[colnames[i]][i]=1
		for element in category_element_str:
			df[element]=dict_new_columns[element]

		# Original columns are dropped from the dataframe
		df=df.drop(col,1)

		all_new_cols.append(category_element_str)
		new_col_dict.append(category_element_reverse_dict)
		dropped_cols.append(main_row)

	return df,dropped_cols,all_new_cols,new_col_dict