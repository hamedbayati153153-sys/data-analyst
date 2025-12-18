# analyze_sample_data.py

"""
This script reads financial data from a CSV file, performs analysis, and generates visualizations.
The results are saved to an output file and visualized using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the input CSV file
input_file_path = 'data/sample_financial_data.csv'
# Path to the output CSV file
output_file_path = 'output/analysis_summary.csv'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

def main():
    """Main function to perform data analysis and visualization."""

    try:
        # Read the CSV file
        print(f"Reading data from {input_file_path}...")
        data = pd.read_csv(input_file_path)

        # Ensure the required columns exist
        required_columns = ['Revenue', 'Expenses', 'Profit']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Perform analysis
        print("Performing analysis...")
        analysis = {
            'Metric': ['Total', 'Average'],
            'Revenue': [data['Revenue'].sum(), data['Revenue'].mean()],
            'Expenses': [data['Expenses'].sum(), data['Expenses'].mean()],
            'Profit': [data['Profit'].sum(), data['Profit'].mean()]
        }

        # Convert analysis results to DataFrame
        analysis_df = pd.DataFrame(analysis)
        print("Analysis complete.")

        # Save analysis summary to a CSV file
        print(f"Saving analysis summary to {output_file_path}...")
        analysis_df.to_csv(output_file_path, index=False)
        print("Analysis summary saved.")

        # Generate a bar chart visualization
        print("Generating bar chart...")
        metrics = ['Revenue', 'Expenses', 'Profit']
        totals = [data['Revenue'].sum(), data['Expenses'].sum(), data['Profit'].sum()]

        plt.bar(metrics, totals, color=['blue', 'orange', 'green'])
        plt.title('Financial Analysis: Total Revenue, Expenses, and Profit')
        plt.ylabel('Amount')
        plt.xlabel('Metrics')
        
        # Save the bar chart as an image file
        chart_output_path = 'output/financial_bar_chart.png'
        plt.savefig(chart_output_path)
        print(f"Bar chart saved to {chart_output_path}.")

        # Show the bar chart
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()