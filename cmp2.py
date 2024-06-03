import argparse
import json

def load_json_file(file_path):
    """Load a JSON file and return its content as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_json_files(file1_path, file2_path):
    """Compare two JSON files and print keys where values differ."""
    # Load both JSON files into dictionaries
    data1 = load_json_file(file1_path)
    data2 = load_json_file(file2_path)
    
    # Compare dictionaries
    for key in set(data1.keys()).union(data2.keys()):
        if key not in data1:
            print(f"Key '{key}' is present only in the second file.")
            print(f"Value: {data2[key]}")
        elif key not in data2:
            print(f"Key '{key}' is present only in the first file.")
            print(f"Value: {data1[key]}")
        elif data1[key] != data2[key]:
            print(f"Difference found at key: {key}")
            print(f"File 1 Value: {data1[key]}")
            print(f"File 2 Value: {data2[key]}")
        print()

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Compare two JSON files and print differences.")
    parser.add_argument("file1", help="Path to the first JSON file.")
    parser.add_argument("file2", help="Path to the second JSON file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the comparison function with the provided file paths
    compare_json_files(args.file1, args.file2)

if __name__ == "__main__":
    main()
