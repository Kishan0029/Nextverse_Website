import re
import os

base_dir = r"c:\Users\kisha\Desktop\simply-static-1-1780122567"
about_path = os.path.join(base_dir, "about-us", "index.html")
index_path = os.path.join(base_dir, "index.html")

with open(about_path, 'r', encoding='utf-8') as f:
    about_content = f.read()

# The testimonial section is the last <section> before <!-- #page -->
match = re.search(r'(<section[^>]*elementor-element-48af5b21.*?</section>)\s*</div>\s*</div>\s*</div><!-- #page -->', about_content, re.DOTALL | re.IGNORECASE)
if not match:
    print("Could not find testimonial section in about-us/index.html")
    exit(1)

testimonial_html = match.group(1)

# fix the links pointing to ../
testimonial_html = testimonial_html.replace('href="../"', 'href="./"')
testimonial_html = testimonial_html.replace('href="../', 'href="./')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Insert the testimonials html before the 'our projects' section
if 'elementor-element-187e48b9' in index_content:
    new_index_content = re.sub(
        r'(<section[^>]*elementor-element-187e48b9)', 
        testimonial_html + r'\n\n\1', 
        index_content, 
        count=1, 
        flags=re.IGNORECASE
    )
    
    # Inject CSS into the elementor-post-4456 style block
    css_to_add = """
.elementor-4456 .elementor-element.elementor-element-48af5b21{padding:120px 0px 120px 0px;}
.elementor-4456 .elementor-element.elementor-element-1ebcf969 > .elementor-widget-container{padding:0px 0px 25px 0px;}
.elementor-4456 .elementor-element.elementor-element-1ebcf969 .prthalign{text-align:center;}
.elementor-4456 .elementor-element.elementor-element-1ebcf969 .agt-section-title-3 .subtitle{justify-content:center;}
"""
    new_index_content = new_index_content.replace('</style>', css_to_add + '</style>', 1)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index_content)
    print("Successfully inserted testimonials and css into index.html")
else:
    print("Could not find 'our projects' section to insert before.")
