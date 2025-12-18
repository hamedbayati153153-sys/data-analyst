import pandas as pd

def analyze_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Perform some analysis
    summary = data.describe()

    # Display the summary of the analyzed data
    print("Dataset analysis summary:")
    print(summary)
    
    # New code to display the first 5 rows of the summary or all rows if less than 5 exist
    print("\nDisplaying the first 5 rows of the analysis summary:")
    print(summary.head(5) if len(summary) > 5 else summary)

# Example usage
if __name__ == "__main__":
    analyze_data("sample_dataset.csv")