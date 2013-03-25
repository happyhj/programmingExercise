# 3/19 Programming Practice
# 131024 Kim Hee Jae
import math

# exercise 1
def print_name(name) :

	print 'your name: ', name

def print_rename(firstName, lastName) :

	print_name(firstName);

	print 'he is from', lastName,'family'

print '# exercise 1'
print_rename('Bruce','Lee')


# exercise 2
def getAbsoluteValue(number) :

	if number > 0 :
		return number
	else :
		return number * -1

print '\n# exercise 2'
print '|-1000| =', getAbsoluteValue(-1000)
print '|1000| =', getAbsoluteValue(1000)


# exercise 3
def reverageNumber(number) :

	if number > 0 and number < 10 :
		number = number + 10
	elif number >= 10 and number < 100 :
		number = number * 0.1
	else :
		number = False

	return number

numberEx3 = input("\n# exercise 3\n input number :")
print reverageNumber(numberEx3)


# exercise 4
def getDistance(x1,y1,x2,y2) :

	distanceX = x2 - x1 
	distanceY = y2 - y1 
	distance = math.sqrt(distanceX**2 + distanceY**2)

	return distance

x1,y1,x2,y2 = 1,3,2,6

print '\n# exercise 4'
print 'Distance between ('+str(x1)+','+str(y1)+') and ('+str(x2)+','+str(y2)+')'
print 'is', getDistance(x1,y1,x2,y2)

# exercise 5
message = 'next people'

def countE(message) :
	numOfE = 0
	for char in message :
		if char == 'e' :
			numOfE = numOfE + 1

	return numOfE

print '\n# exercise 5'
print 'Number of \'e\' in \'', message,'\' is', countE(message)

# exercise 6

def isPalindrome(string) :
	numOfChar = len(string)
	for i in range(0,numOfChar/2) :
		if string[i] != string[numOfChar-1-i] :
			print 'different'
			return False
	print 'same'
	return True

inputStrEx6 = raw_input("\n# exercise 6\nPalindrome Test :")
isPalindrome(inputStrEx6)


