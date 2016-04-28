import csv





def main():
	#open data from crowd 0,28
	fulldata = open('f902014.csv', "r")
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
		votes[row[0]].append(row[14])
	vals = {}

	#gets the majority vote for each question
	for vote in votes:
		vals[vote] = maj(votes[vote])

	histogram = {}
	#fill in the frequencies of each value
	for vote in vals:
		if vals[vote] not in histogram:
			histogram[vals[vote]] = 0
		histogram[vals[vote]] = histogram[vals[vote]] + 1
	#print the frequency for each value
	for i in range(0,6):
		print(str(i) + "\t" + str(histogram[str(i)]))

#majority vote of the integers
def maj(input):
	if isinstance(input, int):
		return input
	if len(input) == 1:
		return input[0]
	if len(input) == 2:
		return min(input[0], input[1])
	if input[0] == input[1]:
		return input[0]
	if input[0] == input[2]:
		return input[0]
	if input[1] == input[2]:
		return input[1]
	return 6


if __name__ == '__main__' : 
	main()