import operator

counts = {}

with open('file.txt', 'r') as file:
	for line in file:
		line = line.rstrip()
		if line in counts:
			counts[line] += 1
		else:
			counts[line] = 1

sorted_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_counts)