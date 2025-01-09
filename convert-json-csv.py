import json
import pandas as pd

# 5. Convert JSON file to CSV file
def convert_json_to_csv(json_file, output_csv_base):
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Convert JSON to pandas DataFrame
    data_frame = pd.DataFrame(json_data["primary_table_data"])
    data_frame2 = pd.DataFrame(json_data["secondary_table_data"])
    
    # Save DataFrame to unique CSV files
    primary_csv = f"{output_csv_base}_primary.csv"
    secondary_csv = f"{output_csv_base}_secondary.csv"
    
    data_frame.to_csv(primary_csv, index=False)
    data_frame2.to_csv(secondary_csv, index=False)
    
    print(f"Primary data successfully saved to {primary_csv}")
    print(f"Secondary data successfully saved to {secondary_csv}")

# Main script to demonstrate visualization, modeling, and JSON to CSV conversion
def main():
    convert_json_to_csv('data.json', 'output_data')

if __name__ == "__main__":
    main()
