import matplotlib
matplotlib.use('Agg')  # Set backend before importing pyplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_missing_values(df, output_path, filename):
    # Calculate missing values
    missing_values = df.isnull().sum()
    missing_percentages = (missing_values / len(df)) * 100
    
    # Create summary DataFrame
    missing_df = pd.DataFrame({
        'Missing Values': missing_values,
        'Percentage': missing_percentages
    }).sort_values('Percentage', ascending=False)
    
    # Filter only columns with missing values
    missing_df = missing_df[missing_df['Missing Values'] > 0]
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing_df.index, y='Percentage', data=missing_df)
    plt.xticks(rotation=45, ha='right')
    plt.title('Percentage of Missing Values by Column')
    plt.tight_layout()
    
    # Save plot instead of showing
    output_file = os.path.join(output_path, f'missing_values_{filename}.png')
    plt.savefig(output_file)
    plt.close()  # Close the figure to free memory
    
    # Print summary
    print("\nMissing Values Summary:")
    print("-" * 50)
    print(missing_df)
    
    return missing_df

def process_all_csv_files(data_folder):
    # Create output directory for plots
    output_path = 'output/plots'
    os.makedirs(output_path, exist_ok=True)
    
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(data_folder, filename)
            df = pd.read_csv(file_path, low_memory=False)
            print(f"\nProcessing file: {filename}")
            analyze_missing_values(df, output_path, filename.replace('.csv', ''))

if __name__ == "__main__":
    data_folder = 'data/raw'
    process_all_csv_files(data_folder)