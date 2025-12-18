# analyze_sample_data.py

import pandas as pd

def analyze_data(data_path, save_path):
    # Load the data
    data = pd.read_csv(data_path)
    
    # Display the first few rows of the dataset
    print("Data before analysis:")
    print(data.head())

    # Perform analysis (example: summary statistics)
    analysis_result = data.describe()

    # Display the analysis summary
    print("Analysis Summary:")
    print(analysis_result)

    # Save the analysis result to a CSV file
    analysis_result.to_csv(save_path)
    
# Example usage
# analyze_data("input.csv", "output.csv")