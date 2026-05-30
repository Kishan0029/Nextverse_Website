import os
import re

base_dir = "."

def update_preloader(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    
    # Replace the lower case 'n' with upper case 'N' in nextverse
    content = re.sub(
        r'(<div class="agn-loader-wrap.*?<div class="load-text">\s*)<span>n</span>',
        r'\1<span>N</span>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated_count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            if update_preloader(file_path):
                updated_count += 1

print(f"Updated preloader N to capital in {updated_count} HTML files.")
