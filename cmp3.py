import argparse
import json
from itertools import zip_longest

def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_json_docs(doc1, doc2):
    """Compare two JSON documents and yield differing keys with their values."""
    for key in set(doc1.keys()).union(doc2.keys()):
        val1 = doc1.get(key)
        val2 = doc2.get(key)
        if val1 != val2:
            yield key, val1, val2

def compare_json_files(file1_path, file2_path):
    """Compare two JSON files and print differing keys with values."""
    data1 = load_json(file1_path)
    data2 = load_json(file2_path)
    
    # Ensure both are lists for proper comparison
    assert isinstance(data1, list) and isinstance(data2, list), "Both files must contain JSON arrays."
    
    # Pairwise comparison of documents
    for doc1, doc2 in zip_longest(data1, data2, fillvalue={}):
        differing_keys_values = list(compare_json_docs(doc1, doc2))
        if differing_keys_values:
            print(f"Differences found in document pair:")
            for key, val1, val2 in differing_keys_values:
                print(f"Key: {key}, Value in File 1: {val1}, Value in File 2: {val2}")
            print()  # Add a newline for separation between document pairs

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Compare two JSON files and print differences including values.")
    parser.add_argument("file1", help="Path to the first JSON file.")
    parser.add_argument("file2", help="Path to the second JSON file.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the comparison function with the provided file paths
    compare_json_files(args.file1, args.file2)

if __name__ == "__main__":
    main()
