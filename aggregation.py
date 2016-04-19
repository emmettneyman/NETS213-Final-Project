import csv





def main():
	#open data from crowd
	fulldata = open('qcdata.csv', "r")
	filereader = csv.reader(fulldata)

	votes = {}
	
	#just filters out the headers
	b = True
	for row in filereader:
		if b:
			#skip headers
			b = False
			continue
		#checks if the current question has been voted on, puts each of its votes into the list
		if row[0] not in votes:
			votes[row[0]] = []
			for i in range 10:
				#appends each value to our list in the dictionary (change the list index as needed)
				votes[row[0]].append(row[i + 3])
	vals = {}
	#print the average value for each question id
	for id in votes:
		print(id + "\t" + avg(votes[id]))

#airthmetic mean of a list of integers
def avg(input):
	sum = 0
	for i in input:
		sum += i
	return sum / len(input)
	return result


if __name__ == '__main__' : 
	main()