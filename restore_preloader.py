import os
import re

base_dir = r"c:\Users\kisha\Desktop\simply-static-1-1780122567"

preloader_html = """
        <div class="agn-loader-wrap s">
            <svg viewbox="0 0 1000 1000" preserveaspectratio="none">
                <path id="svg" d="M0,1005S175,995,500,995s500,5,500,5V0H0Z"></path>
            </svg>
            <div class="agn-loader-wrap-heading">
                <div class="load-text">
                    <span>n</span>
                    <span>e</span>
                    <span>x</span>
                    <span>t</span>
                    <span>v</span>
                    <span>e</span>
                    <span>r</span>
                    <span>s</span>
                    <span>e</span>
                </div>
            </div>
        </div>
"""

def add_preloader(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    
    # Ensure it's not already there
    if '<div class="agn-loader-wrap' not in content:
        # Inject right after <div id="page" ... >
        content = re.sub(
            r'(<div id="page"[^>]*>)',
            r'\1' + preloader_html,
            content,
            count=1,
            flags=re.IGNORECASE
        )

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

added_count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            if add_preloader(file_path):
                added_count += 1

print(f"Added preloader to {added_count} HTML files.")
