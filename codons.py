def create_codon_dict(file_path):
   file_path = "data/codons.txt"
   file = open(path)
   rows = file.readlines()
   file.close() 

   codons_dict = {}
   for row in rows:
     row.strip().split('\t')
     codon = row.strip().split('\t')[0]
     amino_acid = row.strip().split('\t')[2]
     codons_dict[codon] = amino_acid

   return codons_dict


