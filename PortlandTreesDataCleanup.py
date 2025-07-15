# Portland trees data clean up

import pandas as pd
import matplotlib.pyplot as plt  # to plot in graph
import seaborn as sns


def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occured :{e}")

    # We Display the first 7 rows of the Data frame
    # print("First 7 rows of the DataFrame:")
    # print(df.head())


def explore_data(df):
    print(df.head(7))

    print("The info of the dataframe")
    df.info()  # this tells up how many colums we have and their name
    print("This is describe:")
    print(df.describe(include="all"))


def plot_top_families(df, top_n=7):
    if "Family" in df.columns:  # we are wanting all the family label from the dataframe
        species_counts = df["Family"].value_counts()

        plt.figure(figsize=(7, 7), num="Portland Trees")  # graph size
        sns.barplot(
            x=species_counts.values, y=species_counts.index, palette="viridis"
        )  # how we will have the graph plotted
        plt.xlabel("Tree Nums", fontsize=12)  # label for x on the graph
        plt.ylabel("Tree Family", fontsize=12)  # label for y and the font size

        plt.tight_layout()  # this adjusts spacing between subplots and the figure margins
        # tight layout automates the process  manually tweaking
        plt.show()  # this displays the Matplotlib figures that were created.


# Run the project
file_path = "/Users/liz/PortlandTreeDataClean/PortlandTrees.csv"
# we make a data frame from the CSV files
df = load_data(file_path)
if df is not None:
    explore_data(df)
    plot_top_families(df)
