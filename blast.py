from Bio.Blast import NCBIWWW

result_handle = NCBIWWW.qblast("blastn", "nt", 'Example of a single sequence in FASTA/Pearson format:\n\n\n> sequence A\nggtaagtcctctagtacaaacacccccaatattgtgatataattaaaatt atattcatat\ntctgttgccagaaaaaacacttttaggctatattagagccatcttctttg aagcgttgtc\n\n')