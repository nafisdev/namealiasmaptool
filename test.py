fin = open("variant_noformat.txt", "rt")
fout = open("variant_noformat.txt", "wt")

for line in fin:
    fout.write(' '.join(line.split()))
    fout.write('\n')

fin.close()
fout.close()