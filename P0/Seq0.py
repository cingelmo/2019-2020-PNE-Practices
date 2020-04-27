from pathlib import Path


def seq_ping():
    return 'OK'


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text().split('\n')[1:]
    sequence = "".join(file_contents)
    return sequence


def seq_len(sequence):
    return len(sequence)


def seq_count_base(sequence, base):
    return sequence.count(base)


def seq_count(sequence):
    d = {'A': seq_count_base(sequence, 'A'), 'C': seq_count_base(sequence, 'C'),
         'T': seq_count_base(sequence, 'T'), 'G': seq_count_base(sequence, 'G')}
    return d


def seq_reverse(sequence):
    return sequence[::-1]


def seq_complement(sequence):
    bases = ['A', 'C', 'T', 'G']
    complement_bases = ['T', 'G', 'A', 'C']
    d = dict(zip(bases, complement_bases))
    complement_seq = ''
    for bases in sequence:
        for base, complement in d.items():
            if bases == base:
                complement_seq += complement
    return complement_seq
