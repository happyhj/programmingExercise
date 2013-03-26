# 3/26 Programming Practice
# 131024 Kim Hee Jae

## exercise 1 
# Sort Names By Age Gap

age = {'minsu' : 43 , 'jisu':33 , 'john' : 21 , 'david' : 33, 'hary':36, 'messi' :33, 'ronaldo' : 27}

result = dict()

for key_name in age :

	key_ageGap = (age[key_name]/10)*10

	if key_ageGap in result :

		result[key_ageGap].append(key_name)

	else :

		result[key_ageGap] = [key_name]

print result 	
# {40: ['minsu'], 20: ['ronaldo', 'john'], 30: ['messi', 'david', 'jisu', 'hary']}

## Print, sort by age

keylist = result.keys()
keylist.sort()

for ageGap in keylist :
	print ageGap,
	print result[ageGap],

# 20 ['ronaldo', 'john'] 30 ['messi', 'david', 'jisu', 'hary'] 40 ['minsu']