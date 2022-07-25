output = open ("<List_of_Top_Nodes.txt>", "w")
input1 = open ("<list_of_HCT_samples.txt>", "r")
input = open ("<auspice.json>", "r")

from ete3 import Tree
t = Tree("<tree.nwk>", format=1)

sample = []
scount = 0

for line in input1:
	line = line.strip()
	sample.append(line)
	scount = scount + 1
input1.close()

n = []
con = []
tcount = 0

for line in input:
	line = line.strip()
	if "name" in line:
		line = line.split(" ")
		line[1] = line[1].strip(",")
		line[1] = line[1].strip("\"")
		line[1] = line[1].lstrip("\"")
		n.append(line[1])
		tcount = tcount + 1
	if "confidence" in line:
		line = input.readline()
		line = line.strip()
		line = line.split(" ")
		line[0] = line[0].strip(":")
		line[0] = line[0].strip("\"")
		line[0] = line[0].lstrip("\"")
		line[1] = line[1].strip(",")
		if (line[0] == "no"):
			current = 1 - float(line[1])
		else:
			current = float(line[1])
		con.append(current)
input.close()

for x in range (0, scount):
	top = ""
	node = t.search_nodes(name=sample[x])[0]
	output.write(sample[x])
	output.write("\t")
	while node:
		for y in range (0, tcount):
			if str(node.name) == n[y]:
				if con[y] >= 0.5:
					top = n[y]
		node = node.up
	output.write(top)
	output.write("\n")
	print (x)
output.close()
