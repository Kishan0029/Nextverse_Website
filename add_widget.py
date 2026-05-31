import os

widget_code = """
<style>
  elevenlabs-convai {
    position: fixed;
    bottom: 20px;
    left: 20px;
    right: auto;
    z-index: 9999;
  }
</style>
<elevenlabs-convai agent-id="agent_2601kstqgt7qe34b7f7nk2x4yygj"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""

def add_widget_to_html_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Check if it's already added to avoid duplication
                if "agent_2601kstqgt7qe34b7f7nk2x4yygj" in content:
                    continue
                
                # Insert before </body>
                if "</body>" in content:
                    content = content.replace("</body>", f"{widget_code}\n</body>")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Added to {file_path}")
                else:
                    print(f"No </body> found in {file_path}")

if __name__ == '__main__':
    root_dir = r"E:\01_Nextverse\Nextverse Website"
    add_widget_to_html_files(root_dir)
