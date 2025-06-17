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

if "Family" in df.columns:  # we are wanting all the family label from the dataframe
    species_counts = df["Family"].value_counts()

    top_7_species = species_counts.head(7)  # e are getting the top 7

    labels = (
        top_7_species.index.tolist()
    )  # will make a list of the indexes and make them labels
    values = top_7_species.values.tolist()

    plt.figure(figsize=(7, 7))  # graph size
    sns.barplot(
        x=values, y=labels, palette="viridis"
    )  # how we will have the graph plotted
    plt.xlabel("Tree Nums", fontsize=12)  # label for x on the graph
    plt.ylabel("Tree Family", fontsize=12)  # label for y and the font size

    plt.tight_layout()  # this adjusts spacing between subplots and the figure margins
    # tight layout automates the process  manually tweaking
    plt.show()  # this displays the Matplotlib figures that were created.
