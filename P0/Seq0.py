from pathlib import Path


def seq_ping():
    return 'OK'


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    header = file_contents.split('\n')[0]
    file_clean = file_contents.strip(header).replace('\n', '')[0:20]
    return file_clean

