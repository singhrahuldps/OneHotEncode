# One-Hot Encode
A python script to deploy One-Hot encoding in Pandas Dataframes

Requirements -> Pandas, Numpy

## Installation
	pip install OneHotEncode

## Usage
	from OneHotEncode.OneHotEncode import *

#### Input -> (pandas_dataframe,cols,check_numerical=False,max_var=20)
	pandas_dataframe -> The Pandas Dataframe object that contains the column you want to one-hot encode	
	
	cols -> List of column names in pandas_dataframe that you want to one-hot encode
	
	check_numerical (Default=False) -> A naive way of checking if the column contains numerical
	                                   data or is unsuitable for one-hot encoding
	                                   Set it to True to turn on the detection
					   
	max_var (Default=20) -> Max number of diferent variables allowed in a category
                                     
#### Returns df,dropped_cols,all_new_cols,new_col_dict
	df -> Pandas dataframe that returns the one-hot encoded data with the original columns dropped
	
	dropped_cols -> List of arrays containg the dropped columns that were originally input
	
	all_new_cols -> List of list of names of all new columns made for a past single column 
	
	new_col_dict -> List of dictionary of names of all new columns made for a past single column
   

More info would be soon provided through a Medium page.
