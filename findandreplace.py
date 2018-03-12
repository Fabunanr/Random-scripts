## This was made to rename taxon labels in a phylogeny and fasta files
## needs a fasta file, a phylogenetic tree file
## and a tab delimited file with names in the fasta and tree file and 

## input files
MT_CHL = open(insertfilehere,'r')
MT_CHL_fasta = open(insertfastafilehere,'r')

## to read the files
mc_read = MT_CHL.read()
mc_fasta_read = MT_CHL_fasta.read()

## creating a dictionary
d = {}

## function for writing to the dictionary
## given information from a tab delimited text file
with open('dictfornewnames.txt') as f:
    for line in f:
        elements = line.rstrip('\n').split('\t')
        d[elements[0]] = elements[1:]

## cleaning up the dictionary
for k, v in d.items():
    d[k] = str(v).strip('[')
for k, v in d.items():
    d[k] = str(v).strip(']')
for k, v in d.items():
    d[k] = str(v).strip("''")

## function to replace stings matching dictionary values
## and replacing them with the key
def replace_all(text,dic):
    for i, j in dic.items():
        text = text.replace(i,j)
    return text

## Call and print the new text files
## in terminal would call the script
## ex: python findandreplacy.py > nameofnewfile.txt
txt = replace_all(mc_read,d)
print(txt)



MT_CHL.close()
# MT_CHL_new.close()
