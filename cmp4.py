import re

def process_line(line):
    # Match the lines containing "_id"
    match = re.match(r'("_id":\s*"([^"]+)",?)\s*("_id":\s*"([^"]+)",?)', line)
    if match:
        first_key = match.group(1)
        first_id = match.group(2)
        second_key = match.group(3)
        second_id = match.group(4)

        # Create hyperlink for _id
        first_part = f'"_id": "<a href="./fsa/{first_id}.json">{first_id}</a>",'
        second_part = f'"_id": "<a href="./fsa/{second_id}.json">{second_id}</a>",'

        # Insert 40 blank characters between first_part and second_part
        processed_line = f'<span style="color:green">{first_part}</span>{" " * 40}<span style="color:red">{second_part}</span>'
        return processed_line
    else:
        return line

def convert_to_html(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        outfile.write('<html>\n<body>\n<pre>\n')

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('"_id"'):
                if i + 1 < len(lines) and lines[i + 1].strip().startswith('"_id"'):
                    i += 1  # Skip the current line if the next line also starts with "_id"
                    continue
                # Add a newline before lines starting with "_id"
                outfile.write('\n')
                # Wrap the line with <b> tags to make it bold
                processed_line = f'<b>{process_line(line)}</b>'
            else:
                processed_line = process_line(line)
            outfile.write(f'{processed_line}\n')
            i += 1

        outfile.write('</pre>\n</body>\n</html>')

# Usage
input_file = 'input.txt'
output_file = 'output.html'
convert_to_html(input_file, output_file)
