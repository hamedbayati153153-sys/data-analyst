def save_results(df, file_path):
    """ Save the DataFrame to a CSV file. """
    try:
        df.to_csv(file_path, index=False)
        print("Results saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")