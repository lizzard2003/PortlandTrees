# Portland trees data clean up

import pandas as pd
import matplotlib.pyplot as plt  # to plot in graph
import seaborn as sns

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

if "Species" in df.columns:
    species_counts = df["Species"].value_counts()

    top_10_species = species_counts.head(7)

    labels = top_10_species.index.tolist()
    values = top_10_species.values.tolist()

    plt.figure(figsize=(10, 7))
    sns.barplot(x=values, y=labels, palette="viridis")
    plt.xlabel("Tree Nums", fontsize=12)
    plt.ylabel("Tree Species", fontsize=12)

    plt.tight_layout()

    plt.show()
