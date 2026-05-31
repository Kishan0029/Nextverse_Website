import os

old_script = """<script>
  document.addEventListener("DOMContentLoaded", () => {
    const observer = new MutationObserver(() => {
      const widget = document.querySelector('elevenlabs-convai');
      if (widget && widget.shadowRoot) {
        const style = document.createElement('style');
        // Hide the original elements completely
        style.textContent = `
          a[href*="elevenlabs.io"], .powered-by, [class*="footer"], [class*="powered"], [class*="watermark"] { 
            display: none !important; 
          }
        `;
        widget.shadowRoot.appendChild(style);
        
        // Add our own "Powered by Nextverse AI" text at the bottom
        // We will append a new element inside the widget's container
        // Wait for the inner container to be available
        const addCustomBranding = () => {
            const container = widget.shadowRoot.querySelector('div') || widget.shadowRoot;
            if (!widget.shadowRoot.querySelector('.custom-branding')) {
                const branding = document.createElement('div');
                branding.className = 'custom-branding';
                branding.style.cssText = 'text-align: center; font-size: 11px; color: rgba(0, 0, 0, 0.4); padding: 8px; font-family: inherit; position: absolute; bottom: 0; left: 0; width: 100%; pointer-events: none; z-index: 999;';
                branding.textContent = 'Powered by Nextverse AI';
                container.appendChild(branding);
                
                // Ensure the container has padding at the bottom so it doesn't overlap
                const mainApp = widget.shadowRoot.querySelector('[class*="app"], [class*="container"], [class*="main"], main') || container;
                if(mainApp && mainApp.style) {
                    mainApp.style.paddingBottom = '30px';
                }
            }
        };
        
        // Try immediately
        addCustomBranding();
        
        // And observe for changes in case the UI renders later
        const shadowObserver = new MutationObserver(() => {
          addCustomBranding();
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
        
        // Remove custom branding if it was previously added (just in case)
        const customBranding = widget.shadowRoot.querySelector('.custom-branding');
        if (customBranding) customBranding.remove();

        const style = document.createElement('style');
        // Hide the ElevenLabs logo/SVG, but keep the text visible
        style.textContent = `
          a[href*="elevenlabs.io"] svg, a[href*="elevenlabs.io"] img { 
            display: none !important; 
          }
          a[href*="elevenlabs.io"] {
            text-decoration: none !important;
            pointer-events: none !important;
          }
        `;
        widget.shadowRoot.appendChild(style);
        
        // Function to find and replace text inside the widget's shadow DOM
        const replaceText = () => {
            const links = widget.shadowRoot.querySelectorAll('a[href*="elevenlabs.io"], [class*="powered"], [class*="footer"]');
            links.forEach(link => {
                const walk = document.createTreeWalker(link, NodeFilter.SHOW_TEXT, null, false);
                let node;
                while(node = walk.nextNode()) {
                    if (node.nodeValue.includes('Powered by') && !node.nodeValue.includes('Nextverse AI')) {
                        node.nodeValue = 'Powered by Nextverse AI';
                    }
                }
            });
        };
        
        replaceText();
        
        // Observe for dynamic re-renders inside the shadow DOM
        const shadowObserver = new MutationObserver(() => {
          replaceText();
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
