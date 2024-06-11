import re

def process_line(line):
    # Match the lines containing "id" or "_id"
    match = re.match(r'("id":\s*"[^"]+",)\s*("id":\s*"[^"]+",?)', line)
    if not match:
        match = re.match(r'("_id":\s*"[^"]+",)\s*("_id":\s*"[^"]+",?)', line)
    if match:
        first_part = match.group(1)
        second_part = match.group(2)
        processed_line = f'<span style="color:green">{first_part}</span> <span style="color:red">{second_part}</span>'
        return processed_line
    else:
        return line

def convert_to_html(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write('<html>\n<body>\n<pre>\n')
        for line in infile:
            processed_line = process_line(line.strip())
            outfile.write(f'{processed_line}\n')
        outfile.write('</pre>\n</body>\n</html>')

# Usage
input_file = 'input.txt'
output_file = 'output.html'
convert_to_html(input_file, output_file)
