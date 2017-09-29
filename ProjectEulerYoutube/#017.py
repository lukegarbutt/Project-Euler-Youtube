#Number Letter Counts
def main():
	dict_of_units = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
	dict_of_tens = {0:'', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
	dict_of_teens = {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}
	number_as_words = []
	list_of_numbers = []
	for i in range(1,10000):
		list_of_numbers.append(i)
	for i in list_of_numbers:
		number_as_words.append(number_to_letter_converter(i, dict_of_units, dict_of_tens, dict_of_teens))
	total_letter_count = 0
	for i in number_as_words:
		total_letter_count += len(str(i))
	print(total_letter_count)

def number_to_letter_converter(number, dict_of_units, dict_of_tens, dict_of_teens):
	word_of_number = ''
	str_number = str(number)
	while len(str_number) < 4:
		str_number = '0' + str_number
	if int(str_number[0]) != 0:
		word_of_number += dict_of_units[int(str_number[0])]
		word_of_number += 'thousand'
	if int(str_number[1]) != 0:
		word_of_number += dict_of_units[int(str_number[1])]
		word_of_number += 'hundred'
	if int(str_number[2]) != 0:
		if int(str_number[0]) != 0 or int(str_number[1]) != 0:
			word_of_number += 'and'
		if int(str_number[2]) != 1:
			word_of_number += dict_of_tens[int(str_number[2])]
			if int(str_number[3]) != 0:
				word_of_number += dict_of_units[int(str_number[3])]
		else:
			word_of_number += dict_of_teens[int(str_number[3])]
	elif int(str_number[3]) != 0:
		if int(str_number[0]) != 0 or int(str_number[1]) != 0:
			word_of_number += 'and'
		word_of_number += dict_of_units[int(str_number[3])]
	return(word_of_number)

main()