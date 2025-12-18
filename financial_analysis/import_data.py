import pandas as pd

def import_data(file_path):
    """ Import data from a CSV file. """
    try:
        data = pd.read_csv(file_path)
        print("Data successfully imported.")
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None