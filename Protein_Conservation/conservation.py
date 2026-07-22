from Bio import AlignIO
from collections import Counter
import matplotlib.pyplot as plt

align = AlignIO.read("aligned.fasta", "fasta")