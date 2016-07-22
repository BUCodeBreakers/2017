# Name:
# Exercise: 
# Date: 

import os # we type this so that we can use a function called os.urandom(n)
#NOTE: os.urandom(n) will produce n random bytes

###### PROBLEM 1

# Question: What is a byte?  Write your answer as a comment.
#
# Answer:

###### PROBLEM 2

# PART A: Using the Python library function "bytes", encode the
# following strings into ASCII.  Here's an example to get you started:
# example: bytes("this is a string", "ascii")

"asdf"
"the secret is 22"
"p455w0rd"

# PART B: What do you get when you print these ASCII encodings?
#
# Answer: 

# PART C: Write a function to turn any string into its ascii encoding.
# Make sure it returns (not prints) the answer.
def stringToAscii(string):
	return # replace this!

###### PROBLEM 3

# PART A:
# Question: What type is the output of your stringToAscii(string) function?
#
# Answer:

# PART B: Write a function that turns the ascii encoding back to a string, using
# the library function "str", which works sort of the same way as "bytes".
# Check it by making sure that asciiToString( stringToAscii("apple") ) = "apple"

def asciiToString(ascii):
	return # replace this!

###### PROBLEM 4

# PART A:
a = bytes("asdf", "ascii")
# Question: What is a[0]?  What is a[1]?  What about a[2] and a[3]?

# Answer:

# PART B:
# Question: Why did you get what you did for part A?  (Remember the binary
# lesson last Thursday)
#
# Answer:

# PART C:
# Question: Write out "a" in binary, and "d" in binary, then do the XOR
# operation to them and write out the answer in binary.  What is the 
# *decimal number* that corresponds to this binary number?
#
# Answer:

# PART D:
# Run the following function and see what it prints.  Why did you get
# your answer?
def compareaandd():
	a = bytes("asdf", "ascii")
	aandd = a[0] ^ a[2]
	return aandd

##### PROBLEM 5

# Write a function that uses a for loop to XOR (^) every element of
# bytes objects ascii1 and ascii2, puts the result in a new list,
# then returns the result.
def xor(ascii1, ascii2):
	return # replace this!

print("Problem 5: these should be True")
print(xor(stringToAscii('asdf'), stringToAscii('1234')) == b'PAWR')
print(xor(stringToAscii("sixteen-byte msg"), stringToAscii("16-byte string!!!")) == b'B_U\x16\x1c\x11\x0b\r\x11\r\x06\x0cN\nRF')

###### PROBLEM 6

# Using this function will get you a random bytes object that is 
# n bytes long.  Try it with a few different numbers!
def getKey(n):
	return os.urandom(n)

###### PROBLEM 7

# Write the functions encrypt and decrypt.  Encrypt will convert the message from a
# string to ascii, then XOR it with the key and return the result.  Decrypt will
# XOR the ciphertext with the key, convert the result from ascii to a string,
# then return the result.

def encrypt(message, key):
	return # replace this!

def decrypt(ciphertext, key):
	return # replace this!

key = getKey(16)
message = "sixteen-byte msg"
ciphertext = encrypt(message, key)
print("Problem 7: This should look like gibberish:")
print(ciphertext)
print("Problem 7: This should be True:")
print(decrypt(ciphertext, key) == message)
