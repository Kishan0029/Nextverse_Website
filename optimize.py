import os
import re

base_dir = r"c:\Users\kisha\Desktop\simply-static-1-1780122567"

# Regex patterns for WP bloat
bloat_patterns = [
    re.compile(r'<link rel="https://api\.w\.org/"[^>]*>', re.IGNORECASE),
    re.compile(r'<link rel="alternate" title="JSON"[^>]*>', re.IGNORECASE),
    re.compile(r'<link rel="EditURI"[^>]*>', re.IGNORECASE),
    re.compile(r'<meta name="generator" content="WordPress[^>]*>', re.IGNORECASE),
    re.compile(r'<link rel="shortlink"[^>]*>', re.IGNORECASE),
    re.compile(r'<link rel="alternate" title="oEmbed[^>]*>', re.IGNORECASE),
    re.compile(r'<style id="wp-emoji-styles-inline-css">.*?</style>', re.IGNORECASE | re.DOTALL),
    re.compile(r'<script[^>]*wp-emoji-release\.min\.js[^>]*></script>', re.IGNORECASE),
    re.compile(r'<style id="wp-img-auto-sizes-contain-inline-css">.*?</style>', re.IGNORECASE | re.DOTALL),
    re.compile(r'<style id="classic-theme-styles-inline-css">.*?</style>', re.IGNORECASE | re.DOTALL)
]

def get_relative_prefix(file_path, base_path):
    rel_path = os.path.relpath(file_path, base_path)
    depth = rel_path.count(os.sep)
    if depth == 0:
        return "./"
    else:
        return "../" * depth

def optimize_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    
    # 1. Remove WP bloat
    for pattern in bloat_patterns:
        content = pattern.sub('', content)

    # 2. Fix root-relative paths
    prefix = get_relative_prefix(file_path, base_dir)
    
    # Fix href="/..."
    content = re.sub(r'href="/(?!/)', f'href="{prefix}', content)
    # Fix src="/..."
    content = re.sub(r'src="/(?!/)', f'src="{prefix}', content)
    # Fix srcset="/..."
    content = re.sub(r'srcset="/(?!/)', f'srcset="{prefix}', content)
    # Fix url("/...")
    content = re.sub(r'url\((["\']?)/(?!/)', rf'url(\1{prefix}', content)

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

print(f"Optimized {optimized_count} HTML files.")
