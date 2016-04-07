import csv





def main():
	fulldata = open('qcdata.csv', "r")
	filereader = csv.reader(fulldata)

	#majority vote 1
	votes = {}
	
	b = True
	for row in filereader:
		if b:
			b = False
			continue
		if row[0] not in votes:
			votes[row[0]] = []
			for i in range 10:
				votes[row[0]].append(row[i + 3])
	vals = {}
	for id in votes:
		print(id + "\t" + avg(votes[id]))


def avg(input):
	sum = 0
	for i in input:
		sum += i
	return sum / len(input)
	return result


if __name__ == '__main__' : 
	main()