import os
import re

def remove_contact_from_header(root_dir):
    # Regex to match the Contact list item specifically in the header navigation menu
    # Matches: <li id="menu-item-6274"...><a href="...contact-us/...">Contact</a></li>
    contact_li_pattern = re.compile(
        r'<li\s+id="menu-item-6274"[^>]*>\s*<a\s+href="[^"]*contact-us/?(?:index\.html)?"[^>]*>Contact</a>\s*</li>\n?',
        re.IGNORECASE
    )
    
    modified_files = []
    
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    original_content = content
                    content = contact_li_pattern.sub('', content)
                    
                    if content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        modified_files.append(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    
    return modified_files

if __name__ == '__main__':
    root_directory = r"E:\01_Nextverse\Nextverse Website"
    modified = remove_contact_from_header(root_directory)
    print(f"Removed Contact from header in {len(modified)} files.")
    
