from pathlib import Path

filename = 'RNU6_269P.txt'
file_contents = Path(filename).read_text()
header = file_contents.split('\n')
print('First line of the RNU6_269P.txt file: \n', header[0])
