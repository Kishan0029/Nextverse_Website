import os

hide_branding_script = """
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver(() => {
      const widget = document.querySelector('elevenlabs-convai');
      if (widget && widget.shadowRoot) {
        const style = document.createElement('style');
        style.textContent = 'a[href*="elevenlabs.io"], .powered-by, [class*="footer"], [class*="powered"], [class*="watermark"] { display: none !important; }';
        widget.shadowRoot.appendChild(style);
        observer.disconnect();
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  });
</script>
"""

def add_hide_branding(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                if "mutationObserver" in content or "widget.shadowRoot" in content:
                    continue
                
                if "</body>" in content:
                    content = content.replace("</body>", f"{hide_branding_script}\n</body>")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Added script to {file_path}")

if __name__ == '__main__':
    root_dir = r"E:\01_Nextverse\Nextverse Website"
    add_hide_branding(root_dir)
