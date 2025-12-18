import matplotlib.pyplot as plt

def visualize_data(df, column):
    """ Create a simple bar chart for the specified column. """
    if column not in df:
        print(f"Column {column} does not exist.")
        return

    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar')
    plt.title(f"Value Count for {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()