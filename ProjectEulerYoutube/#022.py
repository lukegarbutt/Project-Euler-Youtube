# Names scores
def main():
	with open("names.txt") as file:
		names_file = file
		names_list = []
		for i in names_file:
			names_list.append(i)
	
	new_list = names_list[0].split(',')
	sorted_list = sorted(new_list)
	sum_of_scores = 0
	counter = 1
	for i in sorted_list:
		sum_of_scores += counter * score_name(i)
		counter += 1
	print(sum_of_scores)

def score_name(name):
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	score = 0
	for i in name:
		counter = 1
		for j in alphabet:
			if j == i:
				score += counter
			else:
				counter += 1
	return(score)




main()
