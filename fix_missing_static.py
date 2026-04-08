import os
import re
import subprocess

STATIC_DIR = os.path.join(os.getcwd(), "Static")  # path to your static folder

# Characters not allowed in Windows filenames
INVALID_CHARS = r'<>:"/\|?*[],'

def sanitize_filename(filename):
    """Replace invalid Windows filename characters with underscores"""
    return ''.join(c if c not in INVALID_CHARS else '_' for c in filename)

# Patterns to find referenced files in CSS/JS
patterns = [
    r'url\(["\']?(.*?)["\']?\)',           # CSS url()
    r'/\*# sourceMappingURL=(.*?) \*/'     # JS/CSS source map
]

def create_missing_files():
    """Scan all CSS/JS files and create empty placeholders for missing referenced files"""
    for root, dirs, files in os.walk(STATIC_DIR):
        for file in files:
            if file.endswith((".css", ".js")):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for pattern in patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        # Skip external URLs
                        if match.startswith("http") or match.startswith("data:"):
                            continue

                        # Remove query strings or fragments
                        clean_match = match.split("?")[0].split("#")[0]

                        # Sanitize invalid characters
                        clean_match = sanitize_filename(clean_match)

                        ref_path = os.path.normpath(os.path.join(root, clean_match.replace("/", os.sep)))
                        ref_dir = os.path.dirname(ref_path)
                        if not os.path.exists(ref_dir):
                            os.makedirs(ref_dir)
                        if not os.path.exists(ref_path):
                            with open(ref_path, "w") as f:
                                f.write("")
                            print(f"Created missing file: {ref_path}")

def run_collectstatic():
    """Run Django collectstatic command"""
    print("\nRunning collectstatic...")
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)
    print("\n✅ collectstatic finished successfully!")

if __name__ == "__main__":
    print("Fixing missing static files...")
    create_missing_files()
    run_collectstatic()