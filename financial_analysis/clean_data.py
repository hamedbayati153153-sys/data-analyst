def clean_data(df):
    """ Clean the DataFrame by handling missing values and duplicates. """
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    print("Data cleaned successfully.")
    return df