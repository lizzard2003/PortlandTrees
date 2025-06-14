# Portland trees data clean up

import pandas as pd

# This is the location of the file we are going to be looking at
file_path = "/Users/liz/PortlandTreeDataClean/PortlandTrees.csv"

# we make a data frame from the CSV files
df = pd.read_csv(file_path)

# We Display the first 5 rows of the Data frame
print("First 5 rows of the DataFrame:")
print(df.head())
