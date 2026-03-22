import json
import subprocess

from urllib.request import urlopen

try:
    release_data = urlopen("https://api.github.com/repos/iRNHO/damage-calculator-data/releases/latest").read()
    print(f"Latest release: {json.loads(release_data)["tag_name"]}")

except Exception:
    print("Failed to fetch latest release information.")

new_version = input("Enter new release version (e.g. 'v1.2.3'): v").strip()
commit_message = input("Enter commit message: ").strip()

for args in [
    ["add", "-A"],
    ["commit", "-m", commit_message],
    ["push", "origin", "main"],
    ["tag", "-f", f"v{new_version}"],
    ["push", "-f", "origin", f"v{new_version}"],
]:
    subprocess.run(["git"] + args)
