# File 		: flames.py
# Objective 	: Finds the relationship between two names
# Written by 	: vasanthfriend.raju@gmail.com
# Date 		: 25-Jan-2019

# START OF CODE
#!/usr/bin/python

# creates a relationship list
r_l = ['friend', 'love', 'affection', 'marriage', 'enemy', 'sibling']

# assigns the pair names
str1d = "jack"
str2d = "rose dawson"

# clears all the spaces and unwanted characters in the names
str1 = "".join(str1d.split())
str2 = "".join(str2d.split())

# creates two dictionaries to map character and count in the names
str1_d = {}
str2_d = {}

# fills the dictionaries
for i in str1:
    if i.lower() in str1_d.keys():
        str1_d[i.lower()] += 1
    else:
        str1_d[i.lower()] = 1
		
for i in str2:
    if i.lower() in str2_d.keys():
        str2_d[i.lower()] += 1
    else:
        str2_d[i.lower()] = 1
		

# removes the common characters
var  = 0
for key in str1_d.keys():
    if key in str2_d.keys():
        if str1_d[key] == str2_d[key]:
            str1_d[key] = 0
            str2_d[key] = 0
        else:
            mini = min(str1_d[key], str2_d[key])
            str1_d[key] -= mini
            str2_d[key] -= mini
            
# calculates the final count of remaining characters
var = sum(str1_d.values())
var += sum(str2_d.values())

# finding the relation for the names
new_l = []
count = len(r_l)

while count > 1:
    div = var / count 
    remain = var % count
    if remain == 0:
        for i in range(0, count-1):
            new_l.append(r_l[i])
        del r_l[-1]
        count = len(r_l)	    
    elif remain == 1:
        for i in range(1, count):
            new_l.append(r_l[i])
        del r_l[0]
        count = len(r_l)
    else:		
        for i in range(remain, count):
            new_l.append(r_l[i])
        for i in range(0, remain-1):
            new_l.append(r_l[i])
        del r_l[remain]
        count = len(r_l)
    r_l = new_l
    new_l = []
	    
# prints the relation status of the names	    
print("\nThe relation between "+str1d+" and "+str2d+" is "+r_l[0]+".\n")
    
# END OF CODE
