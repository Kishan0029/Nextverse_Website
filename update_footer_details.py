import os
import re
import glob

base_dir = "."
html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)

# 1. Regex patterns for address and contact
addr_pattern1 = r'4517 Washington Ave\.\s*<br>\s*Manchester,\s*<br>\s*Kentucky'
addr_pattern2 = r'4517 Washington Ave\.\s*Manchester,\s*Kentucky\s*39495'

contact_pattern = r'sara\.cruz@example\.com'

menu_pattern = r'<div class="agn-footer-3-menu mb-70">[\s\S]*?</div>'

modified_count = 0

for file_path in html_files:
    # Skip templates if necessary or search all
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    orig = content
    
    # Replace address
    content = re.sub(addr_pattern1, 'Belagavi, Karnataka, <br>India — 590006', content, flags=re.IGNORECASE)
    content = re.sub(addr_pattern2, 'Belagavi, Karnataka, India — 590006', content, flags=re.IGNORECASE)
    
    # Replace email
    content = re.sub(contact_pattern, 'kishan@gonextverse.in<br>+91 73497 32341', content, flags=re.IGNORECASE)
    
    # Update footer menu links with correct relative depth prefix
    rel_path = os.path.relpath(file_path, base_dir)
    depth = rel_path.count(os.sep)
    if depth == 0:
        prefix = "./"
    else:
        prefix = "../" * depth
        
    new_menu = f"""<div class="agn-footer-3-menu mb-70">
            <a target="_self" href="{prefix}" aria-label="name" class="menu-link">
            home        </a>
            <a target="_self" href="{prefix}services/" aria-label="name" class="menu-link">
            services        </a>
            <a target="_self" href="{prefix}about-us/" aria-label="name" class="menu-link">
            about us        </a>
            <a target="_self" href="{prefix}projects/" aria-label="name" class="menu-link">
            case studies        </a>
            <a target="_self" href="{prefix}contact-us/" aria-label="name" class="menu-link">
            contact us        </a>
    </div>"""
    
    content = re.sub(menu_pattern, new_menu, content, flags=re.IGNORECASE)
    
    if content != orig:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_count += 1

print(f"Successfully updated footer details in {modified_count} HTML files.")
