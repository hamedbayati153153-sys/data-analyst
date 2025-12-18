def analyze_data(df):
    """ Perform basic analysis on the DataFrame. """
    summary = df.describe()
    print("Basic data analysis completed.")
    return summary