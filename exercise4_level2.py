'''
    Week 1, Day 3: Exercise IV
    Python I, II, III, IV
    Name: 
'''

'''Import required module/function'''

''' Problem 1
    Write a function to return list of k random elements from a list/string x
    Input:  x-> list/string; k-> integer
    Output: list of exactly k random elements of x

    Note:   You don't have to implement types validity checking here
            Elements do not have to be unique   
'''

def randomKelements(x, k):
    #Keep picking random elements from x until you have k elements?
    #Hint: How to append to a list? OR maybe start with list of any k elements and keep 
    #replacing each element with a random element from x?
    return 

print "\n------------------------ Problem 1 ----------------------------"
print "\nrandomKelements([2,4,8,-1,-2], 3)"
print randomKelements([2,4,8,-1,-2], 3)
print "\nrandomKelements([2,4,8,-1,-2], 3)"
print randomKelements([2,4,8,-1,-2], 3)
print "\nrandomKelements('Code-Breakers', 3)"
print randomKelements('Code-Breakers', 3)
print "\nrandomKelements('Code-Breakers', 20)"
print randomKelements('Code-Breakers', 20)

#Add 2 more tests here:

print "---------------------------------------------------------------" 


''' Problem 2
    Write a function to count the number of random guesses needed to predict a user input integer
    Input:  No input, ask user for a number
    Output: Number of random predictions you made until you predicted x

    Note:   You can assume that x can only have integer values from 0 to 99 
'''     

def randomGuesses():
    # Do you know the exact number of iterations you have to do here?
    # What's the stopping condition of the loop?
    return    

print "\n------------------------ Problem 2 ----------------------------"
print "\nrandomGuesses()"
print randomGuesses()
print "\nrandomGuesses()"
print randomGuesses()

#Add 2 more tests here:

print "---------------------------------------------------------------" 


''' Problem 3
    Write a function that asks the user for a string and shuffles around its characters
    to make a new string. Feel free to shuffle as much as you'd like
    Input:  No input, ask user for it
    Output: shuffled string from user input

    Note: you're not allowed to use shuffle() function in random module
'''
def shuffleString(my_string):
    #Strings are immutable but lists aren't..how can you shuffle around elements of a list?
    return   

print "\n------------------------ Problem 3 ----------------------------"
print "\nshuffleString('Everyday I\'m shuffling')"
print shuffleString('Everyday I\'m shuffling')
print "\nshuffleString('Everyday I\'m shuffling')"
print shuffleString('Everyday I\'m shuffling')

#Add 2 more tests here:

print "---------------------------------------------------------------" 



''' Problem 4
    Without using math module, write a function to return factorial of an input n
    Input:  n
    Output: factorial of n, or -1 if input (n) is not a +ve integer 

    Use conditionals to print 'Invalid Input' if the input (n) is not a +ve integer

    Hints:  How to use type() to check if (n) is not an integer? How to check if (n) is +ve?

    Note: factorial(3) = 3 * 2 * 1 = 6
'''
def fac(n):
    return    

print "\n------------------------ Problem 4 ----------------------------"
print "\nfac(0): should be: 1"
print fac(0)
print "\nfac(5): should be: 120"
print fac(5)
print "\nfac(-1): should be: -1 with Invalid Input"
print fac(-1)
print "\nfac([1,2,3]): should be: -1 with Invalid Input"
print fac([1,2,3])

#Add 2 more tests here:

print "---------------------------------------------------------------"



''' Problem 5
    Write a function to print the sum of all even indexed elements in a list
    Input:  x; x should be a list of numbers, any other types of inputs are considered to be Invalid
    Output: sum of even indexed elements of x, or None if input (x) is invalid
    
    Use conditionals and type-checking to print 'Invalid Input' if the input is not a list of numbers

    Hints:  How to use type() to check if all elements in input list are numbers? i.e. are either integers 
    or floats?  What does range(start, stop, step) do?

    Note: evenSums([3, 2, 1]) = 3 + 1 = 4
'''

def evenSums(x):    
    return 

print "\n------------------------ Problem 5 ----------------------------"
print "\nevenSums([2,4,8,-1,-2]): should be: 8"
print evenSums([2,4,8,-1,-2])
print "\nevenSums([]): should be: None with Invalid Input"
print evenSums([])
print "\nevenSums([1, 'hi']): should be: None with Invalid Input"
print evenSums([1, 'hi'])
print "\nevenSums('who'): should be: None with Invalid Input"
print evenSums('who')

#Add 2 more tests here:

print "---------------------------------------------------------------"             