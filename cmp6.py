import json
import sys

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_raw_lines(doc1, doc2):
    lines1 = set(json.dumps(doc1, indent=2).splitlines())
    lines2 = set(json.dumps(doc2, indent=2).splitlines())
    
    only_in_first = lines1 - lines2
    only_in_second = lines2 - lines1
    
    return only_in_first, only_in_second

def print_side_by_side(lines1, lines2):
    max_len = max(len(lines1), len(lines2))
    lines1 = list(lines1) + [""] * (max_len - len(lines1))
    lines2 = list(lines2) + [""] * (max_len - len(lines2))

    print(f"{'File 1'.ljust(50)} | {'File 2'}")
    print('-' * 50 + ' | ' + '-' * 50)
    for line1, line2 in zip(lines1, lines2):
        print(f"{line1.ljust(50)} | {line2}")

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
        only_in_first, only_in_second = compare_raw_lines(doc1, doc2)
        if only_in_first or only_in_second:
            print(f"Differences in documents with ID {_id}:")
            print_side_by_side(only_in_first, only_in_second)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_collections.py <file1.json> <file2.json>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    compare_collections(file1, file2)
