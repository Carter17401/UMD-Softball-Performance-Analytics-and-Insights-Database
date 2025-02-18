import pandas as pd

def clean_data(input_file, output_file):
    """Performs data cleaning and saves the processed data."""
    df = pd.read_csv(input_file)
    df.dropna(inplace=True)  # Example cleaning step
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data("data/raw_data.csv", "data/cleaned_data.csv")
