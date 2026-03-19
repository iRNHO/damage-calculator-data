import json
import subprocess
import urllib.request


REPO = "iRNHO/damage-calculator-data"


def get_latest():
    try:
        data = urllib.request.urlopen(
            f"https://api.github.com/repos/{REPO}/releases/latest"
        ).read()
        return json.loads(data)["tag_name"]
    except Exception:
        return None


latest = get_latest()
print(f"Latest release: {latest}")

new_tag = input("Enter new release version (e.g. 1.2.0): ").strip()
commit_message = input("Enter commit message: ").strip()

if not new_tag.startswith("v"):
    new_tag = "v" + new_tag

# 🔥 Write version.txt automatically
with open("version.txt", "w") as f:
    f.write(new_tag.lstrip("v"))

commands = [
    ["git", "add", "-A"],
    ["git", "commit", "-m", commit_message],
    ["git", "push", "origin", "main"],
    ["git", "tag", "-f", new_tag],
    ["git", "push", "-f", "origin", new_tag],
]

for command in commands:
    subprocess.run(command)