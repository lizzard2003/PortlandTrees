# Portland trees data clean up

import pandas as pd

try:
    # This is the location of the file we are going to be looking at
    file_path = "/Users/liz/PortlandTreeDataClean/PortlandTrees.csv"

    # we make a data frame from the CSV files
    df = pd.read_csv(file_path)

    # We Display the first 7 rows of the Data frame
    # print("First 7 rows of the DataFrame:")
    # print(df.head())
    print(df.head(7))

    print("The info of the dataframe")
    df.info()  # this tells up how many colums we have and their name
    print("This is describe:")
    print(df.describe(include="all"))
except FileNotFoundError:
    print(
        f"Error: The file '{file_path}' was not found. Please ensure the file is in the correct directory."
    )
except Exception as e:
    print(f"An error occurred: {e}")
