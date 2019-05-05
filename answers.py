
'''
Is the way you wrote the second program influenced by writing the first?
The two questions are quite similar, so I could've written one answer function for two questions. However,
The entries in the two questions are still different, for example a number might contain a '*' in one file
but not in the other, so I didn't bother write one single function for both.
the soccer one asks the difference, so I used the absolute value for it.
'''

def parseFile(fname):
	with open(fname) as f:
		content = [x.strip() for x in f if x.strip()]
	res = []
	for line in content:
		res.append(line.split())
	return res
def answer1(file):
	content = parseFile(file)
	minTempSpread = float('inf') #max number
	entries = [] #will contain day number and  MxT - MnT
	for line in content:
		if line[0].isdigit(): #1-30
			spread = int(line[1].replace('*','')) - int(line[2].replace('*',''))
			if spread < minTempSpread:
				minTempSpread = spread
			entries.append([line[0], spread])
	res = []
	for entry in entries:
		if entry[1] == minTempSpread:
			res.append(entry[0])
	return res
def answer2(file):
	content = parseFile(file)
	minDiff = float('inf')
	entries = [] #will contain team name and diff of 'for' and 'agaisnt'
	for line in content:
		if line[0].replace('.','').isdigit(): #1-20
			diff = abs(int(line[6]) - int(line[8]))
			if diff <  minDiff:
				minDiff = diff; res = line[1]
			entries.append([line[1], diff])
	res = []
	for entry in entries:
		if entry[1] == minDiff:
			res.append(entry[0])
	return res

print(answer1('w_data.dat'))
print(answer2('soccer.dat'))
