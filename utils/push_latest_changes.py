import json
import subprocess
import urllib.request

from pathlib import Path

try:
    data = urllib.request.urlopen("https://api.github.com/repos/iRNHO/damage-calculator-data/releases/latest").read()
    print(f"Latest release: {json.loads(data)["tag_name"]}")

except Exception:
    print("Failed to fetch latest release information.")

new_version = input("Enter new release version (e.g. '1.2.0'): ").strip()
commit_message = input("Enter commit message: ").strip()

Path("version.txt").write_text(new_version)

for args in [
    ["add", "-A"],
    ["commit", "-m", commit_message],
    ["push", "origin", "main"],
    ["tag", "-f", f"v{new_version}"],
    ["push", "-f", "origin", f"v{new_version}"],
]:
    subprocess.run(["git", *args])
