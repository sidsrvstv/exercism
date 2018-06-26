def to_rna(dna_strand):
    rnaEquiv = {'G':'C','C':'G','T':'A','A':'U'}
    res = []
    for nucl in dna_strand:
        try:
            res.append(rnaEquiv[nucl])
        except KeyError:
            print("Illegal nucleotide ", nucl)
    return ''.join(res)
    
