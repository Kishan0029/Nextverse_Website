import os

style_to_remove = """<style>
  elevenlabs-convai {
    position: fixed;
    bottom: 20px;
    left: 20px;
    right: auto;
    z-index: 9999;
  }
</style>
"""

def remove_style_from_html_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                if style_to_remove in content:
                    content = content.replace(style_to_remove, "")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Removed style from {file_path}")

if __name__ == '__main__':
    root_dir = r"E:\01_Nextverse\Nextverse Website"
    remove_style_from_html_files(root_dir)
