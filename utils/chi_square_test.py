def chi_squared_test(data, target, feature):
  import pandas as pd
  from scipy.stats import chi2_contingency
  # Create a contingency table
  contingency_table = pd.crosstab(data[target], data[feature])

  # Perform the Chi-Squared test
  chi2, p, dof, expected = chi2_contingency(contingency_table)

  # Print the results
  print(f"Chi-Squared Test for independence between {target} and {feature}")
  print(f"Chi2 Statistic: {chi2}, p-value: {p}")