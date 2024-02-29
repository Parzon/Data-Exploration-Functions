#Funtion to one hot encode a df, 3 params, the df, which column to encode else <=12 will be encoded, and if you want drop first or not
def one_hot_encode_df(data, column_names=None, drop_first_tf=False):
  import pandas as pd
  # If no specific column names are provided, encode all columns with <= 12 unique values
  if column_names is None:
      column_names = [col for col in data.columns if data[col].nunique() <= 12]
  
  # Perform one hot encoding only on the specified columns
  for col in column_names:
      # Check if the column is in the DataFrame to avoid KeyErrors
      if col in data.columns:
          one_hot = pd.get_dummies(data[col], prefix=col, drop_first=drop_first_tf)
          data = pd.concat([data, one_hot], axis=1)  # Concatenate the one-hot encoded DataFrame
          data.drop(col, axis=1, inplace=True)  # Drop the original column
  
  return data
