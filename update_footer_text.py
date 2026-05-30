import os
import glob
import re

base_dir = r"c:\Users\kisha\Desktop\simply-static-1-1780122567"
html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)

old_pattern = r'LET’S\s*<span class="has-stoke">\s*get\s*</span>\s*IN\s*<span class="has-stoke">\s*TOUCH\s*</span>'
new_string = 'LET’S <span class="has-stoke">go</span> <span class="has-stoke">NEXTVERSE</span>'

modified_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(old_pattern, content):
        new_content = re.sub(old_pattern, new_string, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1

print(f"Successfully updated footer text in {modified_count} files.")
