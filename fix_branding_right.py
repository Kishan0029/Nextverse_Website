import os

old_script = """<script>
  document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver(() => {
      const widget = document.querySelector('elevenlabs-convai');
      if (widget && widget.shadowRoot) {
        
        const replaceContent = () => {
            const links = widget.shadowRoot.querySelectorAll('a[href*="elevenlabs.io"], [class*="powered"]');
            links.forEach(link => {
                if(link.innerHTML.includes('Nextverse AI')) return;
                
                // Completely replace the content so we don't get duplicates
                link.innerHTML = `
                  <div style="text-align: center; line-height: 1.4; padding: 4px;">
                    <span style="font-weight: 500; color: inherit;">Powered by Nextverse AI</span><br>
                    <span style="font-size: 0.85em; opacity: 0.8; text-decoration: underline;">Want a custom AI Agent for your site? Click here!</span>
                  </div>
                `;
                
                link.href = '/contact-us/';
                link.target = '_self';
                link.style.textDecoration = 'none';
                link.style.pointerEvents = 'auto';
            });
        };
        
        replaceContent();
        
        const shadowObserver = new MutationObserver(() => {
          replaceContent();
        });
        shadowObserver.observe(widget.shadowRoot, { childList: true, subtree: true });
        
        observer.disconnect();
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  });
</script>"""

new_script = """<script>
  document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver(() => {
      const widget = document.querySelector('elevenlabs-convai');
      if (widget && widget.shadowRoot) {
        
        const replaceContent = () => {
            const links = widget.shadowRoot.querySelectorAll('a[href*="elevenlabs.io"], [class*="powered"]');
            links.forEach(link => {
                if(link.innerHTML.includes('text-align: right')) return;
                
                link.innerHTML = `
                  <div style="text-align: right; padding: 4px 10px 4px 4px; width: 100%; box-sizing: border-box;">
                    <span style="font-weight: 500; color: inherit; font-size: 11px; opacity: 0.6;">Powered by Nextverse AI</span>
                  </div>
                `;
                
                // Remove pointer events so it's just text
                link.style.textDecoration = 'none';
                link.style.pointerEvents = 'none';
                link.style.display = 'block';
                link.style.width = '100%';
            });
        };
        
        replaceContent();
        
        const shadowObserver = new MutationObserver(() => {
          replaceContent();
        });
        shadowObserver.observe(widget.shadowRoot, { childList: true, subtree: true });
        
        observer.disconnect();
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  });
</script>"""

def replace_branding_script(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                if old_script in content:
                    content = content.replace(old_script, new_script)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated script in {file_path}")

if __name__ == '__main__':
    root_dir = r"E:\01_Nextverse\Nextverse Website"
    replace_branding_script(root_dir)
