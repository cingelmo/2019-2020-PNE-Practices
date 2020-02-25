from pathlib import Path

filename = 'ADA.txt'
file_contents = Path(filename). read_text()
header = file_contents.split('\n')[0]
file_clean = file_contents.strip(header).replace('\n','')
counter = 0

print(file_clean)
for element in file_clean:
    counter += 1
print(counter)