# Instructions
#
# Translate RNA sequences into proteins.
# RNA can be broken into three nucleotide sequences called codons, and then translated to a polypeptide like so:
# RNA: "AUGUUUUCU" => translates to
# Codons: "AUG", "UUU", "UCU" => which become a polypeptide with the following sequence =>
# Protein: "Methionine", "Phenylalanine", "Serine"
# There are 64 codons which in turn correspond to 20 amino acids; however, all of the codon sequences and
# resulting amino acids are not important in this exercise. If it works for one codon, the program should work for
# all of them. However, feel free to expand the list in the test suite to include them all.
#
# There are also three terminating codons (also known as 'STOP' codons); if any of these codons are encountered
# (by the ribosome), all translation ends and the protein is terminated.
#
# All subsequent codons after are ignored, like this:
# RNA: "AUGUUUUCUUAAAUG" =>
# Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>
# Protein: "Methionine", "Phenylalanine", "Serine"
# Note the stop codon "UAA" terminates the translation and the final methionine is not translated into the
# protein sequence.

TRANSLATION = {
	"Methionine": ["AUG"],
	"Phenylalanine": ["UUU", "UUC"],
	"Leucine": ["UUA", "UUG"],
	"Serine": ["UCU", "UCC", "UCA", "UCG"],
	"Tyrosine": ["UAU", "UAC"],
	"Cysteine": ["UGU", "UGC"],
	"Tryptophan": ["UGG"],
	"STOP": ["UAA", "UAG", "UGA"]
}


def proteins(strand):
	result = []
	strand = [strand[i:i + 3] for i in range(0, len(strand), 3)]
	for sequence in strand:
		result += [key for key, value in TRANSLATION.items() if sequence in value]
	if 'STOP' in result:
		result = result[:result.index("STOP")]
	return result


print(proteins("AUGUUUUAA"))