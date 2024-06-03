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
    
    # Find differences in keys and values
    for key in data1.keys():
        if key not in data2 or data1[key] != data2[key]:
            print(f"Difference found at key: {key}")
            print(f"File 1 Value: {data1.get(key)}")
            print(f"File 2 Value: {data2.get(key, 'Key not found in second file.')}")
            print()
    # Check for keys present in the second file but not in the first
    for key in data2.keys():
        if key not in data1:
            print(f"Key '{key}' is present only in the second file.")
            print(f"Value: {data2.get(key)}")
            print()

# Provide the paths to your two JSON files
file1_path = 'file1.json'
file2_path = 'file2.json'

compare_json_files(file1_path, file2_path)
