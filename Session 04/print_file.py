from pathlib import Path

filename = "RNU6_269P.txt"
file_contents = Path(filename).read_text()

print(file_contents)
