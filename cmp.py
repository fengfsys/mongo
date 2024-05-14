import json

# Read document 1 from file
with open('doc1.json', 'r') as file:
    doc1 = file.read()

# Read document 2 from file
with open('doc2.json', 'r') as file:
    doc2 = file.read()

# Convert JSON strings to Python dictionaries
doc1_dict = json.loads(doc1)
doc2_dict = json.loads(doc2)

# Find the keys that are different between the two documents
all_keys = set(doc1_dict.keys()) | set(doc2_dict.keys())

# Find the keys that have different values between the two documents
diff_keys = {key for key in all_keys if doc1_dict.get(key) != doc2_dict.get(key)}

# Find the differing values for the differing keys
diff_values = {key: (doc1_dict.get(key), doc2_dict.get(key)) for key in diff_keys}

# Print the differing keys and values
for key, value in diff_values.items():
    #print(f"Difference in key '{key}': {value[0]} (Document 1) vs {value[1]} (Document 2)")
    print(f"'{key}': {value[0]}  | {value[1]} ")
