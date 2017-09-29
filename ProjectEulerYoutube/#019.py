# Counting Sundays

def main():
	days = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	years = []
	for i in range(1901,2001):
		years.append(i)

	list_of_days_passed = []
	list_of_first_of_month_days = []
	is_first_of_month = True
	for year in years:
		for month in months:
			is_first_of_month = True
			for day in range(days_in_month(month, year)):
				if is_first_of_month:
					list_of_first_of_month_days.append(days[0])
					is_first_of_month = False
				list_of_days_passed.append(days[0])
				days.append(days.pop(0))

	count = 0
	for i in list_of_first_of_month_days:
		if i == 'Sunday':
			count += 1
	print(count)
	print(len(list_of_days_passed))

	
def days_in_month(month, year):
	months_of_31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
	months_of_30 = ['Sep', 'Apr', 'Jun', 'Nov']
	months_of_28 = ['Feb']
	if month in months_of_31:
		return(31)
	elif month in months_of_30:
		return(30)
	elif month in months_of_28:
		if year % 400 == 0:
			return(29)
		elif year % 100 == 0:
			return(28)
		elif year % 4 == 0:
			return(29)
		else:
			return(28)

main()
