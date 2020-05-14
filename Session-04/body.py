from pathlib import Path

filename = 'U5.txt'
file_contents = Path(filename).read_text()
header = file_contents.split('\n')[0]
body = file_contents.strip(header)
print('Body of the U5.txt file: ', body)
