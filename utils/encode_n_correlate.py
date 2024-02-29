def encode_and_correlate(data, target_variable, categorical_columns=None, annot=False):
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  import numpy as np
  """
  One-hot encode specified categorical columns or those with <= 12 unique values,
  calculate the correlation matrix, and plot a heatmap of the correlations focusing
  on the lower triangle and highlighting correlations with the target variable.
  
  :param data: DataFrame to be processed.
  :param target_variable: The name of the target variable column in the DataFrame.
  :param categorical_columns: Optional list of column names to be one-hot encoded.
  :param annot: Whether to annotate the heatmap.
  """
  # If categorical_columns is None, use the <= 12 strategy
  if categorical_columns is None:
      categorical_columns = [col for col in data.columns if data[col].nunique() <= 12 and col != target_variable]
  
  # One-hot encode the categorical columns
  df_encoded = pd.get_dummies(data, columns=categorical_columns, drop_first=False)
  
  # Calculate the correlation matrix
  correlation_matrix = df_encoded.corr()
  
  # Plot only the lower triangle of the correlation matrix
  mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
  plt.figure(figsize=(20, 15))
  cmap = sns.diverging_palette(230, 20, as_cmap=True)
  sns.heatmap(correlation_matrix, mask=mask, annot=annot, cmap=cmap, fmt=".2f", cbar_kws={"shrink": .5})
  plt.title('Lower Triangle Correlation Heatmap (One-Hot Encoded Features)')
  plt.show()
  
  # Highlighting the correlations with the target variable
  print(f"Correlations of features with {target_variable}:")
  target_correlations = correlation_matrix[target_variable].sort_values(ascending=False)
  # Exclude the target variable itself to avoid self-correlation
  target_correlations = target_correlations.drop(target_variable, errors='ignore')
  print(target_correlations)

# Example usage (assuming 'df' is your DataFrame and 'good_bad' is the target variable):
# encode_and_correlate(df, 'good_bad', categorical_columns=None, annot=False)
