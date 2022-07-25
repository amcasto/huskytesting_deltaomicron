input1 = open ("<input_alignment.fasta>", "r")
output = open ("<pairwise_distances.txt>", "w")

name = []
seq = []
current = ""

line = input1.readline()
line = line.strip()
line = line.strip(">")
name.append(line)
count1 = 1

for line in input1:
	line = line.strip()
	if ">" in line:
		line = line.strip(">")
		name.append(line)
		seq.append(current)
		current = ""
		count1 = count1 + 1
	else:
		current = current + line
seq.append(current)
input1.close()

for x in range (0, count1):
	n1 = name[x]
	seq1 = seq[x]
	for y in range (x + 1, count1):
		n2 = name[y]
		seq2 = seq[y]
		output.write(n1)
		output.write("\t")
		output.write(n2)
		output.write("\t")
		l = len(seq2)
		d = 0
		for z in range (0, l):
			if (seq1[z] == "A" or seq1[z] == "C" or seq1[z] == "G" or seq1[z] == "T") and (seq2[z] == "A" or seq2[z] == "C" or seq2[z] == "G" or seq2[z] == "T") and (seq1[z] != seq2[z]):
				d = d + 1
		output.write(str(d))
		output.write("\n")
	print (x)
output.close()
 					
