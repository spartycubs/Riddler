years = [i for i in range(1,100)]
months = 12
attacks = [0 for i in range (99)]
longest_gap = current_gap = 0
start_month = gap_month = 0
start_day = gap_day = 0
start_year = gap_year = 0
good_years = []

for k in years:                                                 #For loop to iterate through years
	for i in range(1,months+1):                                 #For loop to iterate through months of each year
		if i == 4 or i == 6 or i == 9 or i == 11:               #30 days hath September...
			days = 30
		elif i == 2:                                            #February
			if k % 4 == 0:                                      #Leap years
				days = 29
			else:                                               #Normal years
				days = 28
		else:                                                   #Other months
			days = 31
		
		for j in range(1,days+1):                               #For loop to iterate through days of each month
			if k == j * i:                                      #Check for an attack (month*day = year?)
				attacks[k-1] += 1
				if current_gap > longest_gap:                   #Is this the longest gap?
					longest_gap = current_gap                   #Store the new longest gap           
					gap_year = k                                #Store the end date of the longest gap
					gap_month = i
					gap_day = j
					longest_gap_month = start_month             #Store the start date of the longest gap
					longest_gap_day = start_day
					longest_gap_year = start_year
				current_gap = 0                                 #Reset current gap counter
			else: 												
				current_gap += 1                                #Add to gap
				if current_gap == 1:                            #Reset gap start counters if there was an attack the day before
					start_day = j
					start_month = i
					start_year = k
	if attacks[k-1] == 0:
		good_years.append("'%s" % years[k-1])
					
print(good_years)
print("There will be %s total attacks between the start of 2001 and the end of 2099" % sum(attacks))
print("The maximum number of attacks will be %s attacks in 20%s" % (max(attacks), years[attacks.index(max(attacks))]))
print("There are %s years with no attacks." % len(good_years))
print("These years are:", *good_years, sep = ", ")
print("The longest gap is %s days from %s/%s/%s - %s/%s/%s" % (longest_gap, longest_gap_month, longest_gap_day, longest_gap_year, gap_month, gap_day, gap_year))