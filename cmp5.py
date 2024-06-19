import json
import sys

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_documents(doc1, doc2):
    lines1 = json.dumps(doc1, indent=4).split('\n')
    lines2 = json.dumps(doc2, indent=4).split('\n')
    
    differences = []
    max_len = max(len(lines1), len(lines2))
    
    for i in range(max_len):
        line1 = lines1[i] if i < len(lines1) else ''
        line2 = lines2[i] if i < len(lines2) else ''
        if line1 != line2:
            differences.append((line1, line2))
    
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
            for line1, line2 in differences:
                print(f"    File 1: {line1}")
                print(f"    File 2: {line2}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_collections.py <file1.json> <file2.json>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    compare_collections(file1, file2)
