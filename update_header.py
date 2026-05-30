import os
import re

base_dir = "."
index_html_path = os.path.join(base_dir, "index.html")

with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    root_content = f.read()

# Extract the header from index.html
header_match = re.search(r'(<header class="[^"]*agn-header[^"]*".*?</header>)', root_content, flags=re.DOTALL | re.IGNORECASE)
if not header_match:
    print("Could not find header in index.html")
    exit(1)

root_header = header_match.group(1)

# Ensure the header's contact us link uses a relative path from the root
root_header = re.sub(
    r'href="https://themexriver\.com/[^"]*/contact-us/"',
    r'href="./contact-us/"',
    root_header,
    flags=re.IGNORECASE
)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content

    # Calculate depth to generate prefix
    rel_path = os.path.relpath(file_path, base_dir)
    depth = rel_path.count(os.sep)
    if depth == 0:
        prefix = "./"
    else:
        prefix = "../" * depth

    # Replace header links prefix
    new_header = root_header.replace('href="./', f'href="{prefix}')
    
    # Replace existing header
    content = re.sub(
        r'<header class="[^"]*agn-header[^"]*".*?</header>',
        new_header,
        content,
        count=1,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Replace yay icon size if not already wrapped
    if 'vertical-align: middle;">🤟</span>' not in content:
        content = content.replace('🤟', '<span style="font-size: 0.3em; vertical-align: middle;">🤟</span>')

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            if process_file(os.path.join(root, file)):
                count += 1

print(f"Updated header and yay icons in {count} HTML files.")
