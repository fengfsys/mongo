import json
import sys

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_documents(doc1, doc2):
    differences = {}
    keys = set(doc1.keys()).union(doc2.keys())
    for key in keys:
        if key not in doc1:
            differences[key] = (None, doc2[key])
        elif key not in doc2:
            differences[key] = (doc1[key], None)
        elif doc1[key] != doc2[key]:
            differences[key] = (doc1[key], doc2[key])
    return differences

def compare_collections(file1, file2):
    docs1 = {doc['_id']: doc for doc in load_json_file(file1)}
    docs2 = {doc['_id']: doc for doc in load_json_file(file2)}

    ids1 = set(docs1.keys())
    ids2 = set(docs2.keys())

    # IDs only in the first file
    only_in_first = ids1 - ids2
    for _id in only_in_first:
        print(f"Left side only (File 1): {_id} => {docs1[_id]}")

    # IDs only in the second file
    only_in_second = ids2 - ids1
    for _id in only_in_second:
        print(f"Right side only (File 2): {_id} => {docs2[_id]}")

    # IDs present in both files
    in_both = ids1 & ids2
    for _id in in_both:
        doc1 = docs1[_id]
        doc2 = docs2[_id]
        differences = compare_documents(doc1, doc2)
        if differences:
            print(f"Different in both for ID {_id}:")
            for key, (val1, val2) in differences.items():
                print(f"    {key}: File 1 -> {val1}, File 2 -> {val2}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_collections.py <file1.json> <file2.json>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    compare_collections(file1, file2)
