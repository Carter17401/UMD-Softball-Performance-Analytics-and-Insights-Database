import pandas as pd

def convert_to_csv(input_file, output_file):
    """Converts raw data file into CSV format."""
    df = pd.read_fwf(input_file)  # Assuming fixed-width format
    df.to_csv(output_file, index=False)
    print(f"Data successfully converted to {output_file}")

if __name__ == "__main__":
    convert_to_csv("data.docx", "data/raw_data.csv")
