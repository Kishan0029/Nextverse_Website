"""
Nextverse Site Optimizer - Tasks 2, 3, 4
(Contact form / Task 1 skipped - will add Formspree later)
"""
import os, re, glob

BASE_DIR = r"c:\Users\kisha\Desktop\simply-static-1-1780122567"

SEO_MAP = {
    "index.html": ("Nextverse | Creative Digital Agency", "Nextverse is a premium creative agency specializing in motion design, branding, and digital experiences that captivate audiences."),
    "about-us/index.html": ("About Us | Nextverse Creative Agency", "Learn about Nextverse - our story, our team, and our passion for creating world-class digital experiences."),
    "contact-us/index.html": ("Contact Us | Nextverse Creative Agency", "Get in touch with the Nextverse team. Let us collaborate and build something amazing together."),
    "service/index.html": ("Our Services | Nextverse Creative Agency", "Explore Nextverse services: motion design, branding, web design, and more."),
    "projects/index.html": ("Our Projects | Nextverse Creative Agency", "Browse our portfolio and see how Nextverse has helped brands across the globe tell their story."),
    "blog/index.html": ("Blog & Insights | Nextverse Creative Agency", "Read the latest insights, design tips, and industry news from the Nextverse creative team."),
    "faq/index.html": ("FAQ | Nextverse Creative Agency", "Have questions? Find answers about Nextverse services and process."),
}

html_files = glob.glob(os.path.join(BASE_DIR, "**/*.html"), recursive=True)
print(f"Found {len(html_files)} HTML files\n")

# ── TASK 2: Fix Internal Links & Branding ──────────────────────────────────
fixes = [
    (r'My Blog', 'Nextverse'),
    (r'\?simply_static_page=\d+', ''),
    (r'2025 <a[^>]*>Themexriver</a> All Rights Reserved\.', '2025 Nextverse. All Rights Reserved.'),
]
link_count = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    orig = c
    for pat, rep in fixes:
        c = re.sub(pat, rep, c)
    if c != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        link_count += 1
print(f"[2/4] Links & branding fixed in {link_count} files")

# ── TASK 3: SEO Meta Tags ──────────────────────────────────────────────────
seo_count = 0
for rel, (title, desc) in SEO_MAP.items():
    fp = os.path.join(BASE_DIR, rel)
    if not os.path.exists(fp):
        print(f"  [SKIP] Not found: {rel}")
        continue
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', c, flags=re.DOTALL)
    c = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', c, count=1)
    c = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', c)
    c = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', c)
    c = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{title}">', c)
    c = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{desc}">', c)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    seo_count += 1
    print(f"  [OK] {rel}")
print(f"[3/4] SEO updated in {seo_count} pages")

# ── TASK 4: Remove Performance Bloat ──────────────────────────────────────
bloat_patterns = [
    r'<script type="speculationrules">.*?</script>',
    r'<script id="wp-emoji-settings"[^>]*>.*?</script>',
    r'<script type="module">[\s\S]*?wp-emoji-loader[\s\S]*?</script>',
    r'<script id="wp-i18n-js-after">[\s\S]*?</script>',
]
perf_count = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    orig = c
    for pat in bloat_patterns:
        c = re.sub(pat, '', c, flags=re.DOTALL)
    if c != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        perf_count += 1
print(f"[4/4] Performance bloat removed from {perf_count} files")

print("\nALL DONE!")
