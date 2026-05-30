import os
import re

base_dir = r"c:\Users\kisha\Desktop\simply-static-1-1780122567"

def optimize_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    
    # Remove preloader (safely match until the next div or just match the block)
    content = re.sub(r'<div class="agn-loader-wrap[^>]*>.*?<div class="agn-back-to-top', '<div class="agn-back-to-top', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove offcanvas button
    content = re.sub(r'<!-- offcanvas-btn -->\s*<button[^>]*class="[^"]*agn-offcanvas-btn-2[^"]*"[^>]*>.*?</button>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<button[^>]*class="[^"]*agn-offcanvas-btn-2[^"]*"[^>]*>.*?</button>', '', content, flags=re.DOTALL | re.IGNORECASE)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

optimized_count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            if optimize_file(file_path):
                optimized_count += 1

print(f"Removed preloader and menu button from {optimized_count} HTML files.")
