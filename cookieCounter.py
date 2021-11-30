"""
NAKHUL KISAN (NK)
QUANTCAST INTERVIEW 2021
SOFTWARE ENGINEER –– AUDIENCE SIGNALS ROLE
"""
import sys
import csv


# converts string date (YYYY-MM-DD) to integer
def toInt(string):
	return int(string.translate({ord('-'): None}))



# binary search to find index range of a target date
	# array must be of format dates (YYYY-MM-DD) of type string
class Search:
    def __init__(self, array):
        self.array = array

    def left(self, lo, hi, target):
        if(lo == hi and toInt(self.array[lo][:10]) == target):
            return lo
        # return -1 if binary searched end of search but target non-existent
        if(lo  == hi):
            return -1

        mid = lo + int((hi - lo) / 2)

        if(toInt(self.array[mid][:10]) > target):
            return self.left(mid + 1, hi, target)
        else:
            return self.left(lo, mid, target)
    

    def right(self,  lo, hi, target):
        if (lo == hi):
            return lo

        mid = lo + int((hi - lo) / 2) +1

        if (toInt(self.array[mid][:10]) < target):
            return self.right(lo, mid - 1, target)
        else:
            return self.right(mid, hi, target)





# main cookie parser
class CookieCounter:
	def __init__(self, file):
		# READ CSV file to list (index 0 is header so don't include)
			# FUTURE QUESTION: if csv file ever turns out to be too large for memory, read in chunks via pandas
		self.cookies = list(csv.reader(open(file)))[1:]
		# filter missing values from CSV file
		self.cookies = list(filter(lambda val: val !=  [], self.cookies))

	# finds all mode cookies, given some range
	def mostInstances(self, start, end):
		# build hashmap with value of instances
		instances = {}
		for i in range(start, end+1):
			if self.cookies[i][0] in instances: 
				instances[self.cookies[i][0]] +=1
			else: 
				instances.update({self.cookies[i][0] : 1})


		# determine keys with highest values
		itemMaxValue = max(instances.items(), key=lambda x: x[1])

		listOfKeys = []
		# Iterate over all the items in dictionary to find keys with max value
		for key, value in instances.items():
		    if value == itemMaxValue[1]: 
		    	listOfKeys.append(key)

		return listOfKeys



	# prints most active cookies, given a date
	def printMostActive(self, date):
		# EDGE CASES (date out of range)
			# convert string date into int  --  int(cookie[1][:10].translate({ord('-'): None}))
		targetDate = toInt(date)
		last, first = toInt(self.cookies[0][1][:10]),  toInt(self.cookies[len(self.cookies)-1][1][:10])

		if(first > targetDate or targetDate > last):
			print('You entered ', date, ' This date is an invalid/unrecorded in our log\nPlease enter a valid date :-)')
			return


		# BINARY SEARCH -- to determine date range of interest
		findRange  =  Search([date[1] for date in self.cookies])
		start = findRange.left(0, len(self.cookies) - 1, targetDate)

		if(start == -1):
			print('There were no active cookies for this date\nPlease try another date')
			return

		end = findRange.right(0, len(self.cookies) - 1, targetDate)


		# GET MOST ACTIVE COOKIES
		listOfKeys = self.mostInstances(start, end)
		

		# PRINT most active
		for i in listOfKeys: 
			print(i)
		return



if  __name__  ==  '__main__':
	# check if bash arguments are in formate [csv_file_name], [date]
	if(len(sys.argv) == 3 and sys.argv[1][-3:] == 'csv'):
		# pass in csv filename and date in question from bash
		file, date = sys.argv[1:]


		counter =  CookieCounter(file)
		if(counter.cookies != []):
			counter.printMostActive(date)
		else:
			print('There are no active cookies recorded in the log!')
	else:
		print('You are missing an argument!')



