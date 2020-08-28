from datetime import datetime, date

def subtractYears(todaystring, interval):
	today = todaystring.split('-')
	result = str(int(today[0])-interval)
	result = result + "-" + today[1] + "-" + today[2] 
	return result

def wayback(todayobject, interval):
	today = datetime.strftime(todayobject, "%Y-%m-%d")
	result  = subtractYears(today, interval)
	result = datetime.strptime(result, "%Y-%m-%d")
	return result

intervals = [100,50,25,10,5,1]

today = date.today()

for value in intervals:
	result = wayback(today, value)
	result = result.strftime("%Y-%m-%d")
	print(result)
	result = datetime.strptime(result, "%Y-%m-%d")
	print(result.year, result.month, result.day)
	print(result)

"""
print(today)

print(type(today))
today = datetime.strftime(today, "%Y-%m-%d")
print(today, type(today))
tempToday = today.split('-')
print(tempToday)
centuryAgo = str(int(tempToday[0])-100) +  "-" + tempToday[1] + "-" +  tempToday[2] 
print(centuryAgo)
fiftyAgo = 

"""