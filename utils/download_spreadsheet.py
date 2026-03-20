from urllib.request import urlopen
from pathlib import Path

with urlopen("https://docs.google.com/spreadsheets/d/1V8TNWd33-PuOggIC3dM186NVpuf4b0cIPDVTpwXlohQ/export?format=xlsx") as response:
    Path("iRNHO's Spreadsheet.xlsx").write_bytes(response.read())
