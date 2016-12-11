def count_dna_nucleotides(dna):
    counter = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in dna:
        counter[nucleotide] += 1
    return " ".join([str(counter["A"]), str(counter["C"]), str(counter["T"]), str(counter["G"])])
