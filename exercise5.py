# Name:
# Exercise: 
# Date: 


###### PROBLEM 1

# Write a function to turn any string into its ascii encoding.
# Make sure it returns (not prints) a list of ascii number for each character of the string
# What does ord() function do?
def stringToAscii(string):
	return # replace this!

print("Problem 1: These should return True")
print(stringToAscii("trees") == [116, 114, 101, 101, 115])
print(stringToAscii("1%9 '") == [49, 37, 57, 32, 39])

###### PROBLEM 2

# PART A:
# Question: What type is the output of your stringToAscii(string) function?
#
# Answer:

# PART B: Write a function that turns the ascii encoding back to a string, using
# the library function "chr", which reverses "ord".

def asciiToString(ascii):
	return # replace this!

print("Problem 2: These should return True")
print(asciiToString(stringToAscii("apple")) == "apple")
print(asciiToString([116, 114, 101, 101, 115]) == "trees")

###### PROBLEM 3

# PART A:
# Question: Write out the ascii encoding of "a" in binary, and 
# the ascii encoding of "d" in binary, then do the XOR
# operation to them and write out the answer in binary.  What is the 
# *decimal number* that corresponds to this binary number?
#
# Answer: 
'''
	Your Answer
'''

# PART B:
# XOR the characters 'a' and 'd' together using the caret (^) operator
# Make sure you get the same thing as in part A.
'''
	Your Answer
'''

##### PROBLEM 4

# Write a function that uses a for loop to XOR (^) every element of
# lists of ASCII numbers ascii1 and ascii2 (with equal length), puts 
# the result in a new list, and returns it
def xor(ascii1, ascii2):
	return  # replace this!

print("Problem 4: these should be True")
print(xor(stringToAscii('asdf'), stringToAscii('1234')) == [80, 65, 87, 82])
print(xor(stringToAscii("sixteen-byte msg"), stringToAscii("16-byte string!!!")) == 
	[66, 95, 85, 22, 28, 17, 11, 13, 17, 13, 6, 12, 78, 10, 82, 70])



'''
-------------------------------------- Level 2 ---------------------------------------

'''

##### PROBLEM 5

# Write a function that uses loop to convert a string of binary number to decimal
def binary2decimal(bin):
	return  #replace this!

print ("Problem 5: these should be True")
print (binary2decimal(bin(46239)[2:])==46239)	
print (binary2decimal(bin(47)[2:])==47)		


##### PROBLEM 6

# Write a function that uses loop (while) to convert decimal number to string of binary number
def decimal2binary(decimal):
	return #replace this!

print ("Problem 6: these should be True")
print (decimal2binary(46239)==bin(46239)[2:])	
print (decimal2binary(47)==bin(47)[2:])	

