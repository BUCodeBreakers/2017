#Name:
#Exercise: 4
#Date: 
#Collaborators:
#Lists and For Loops

##########################################
# (A)
##########################################

#Write a for loop that prints out each individual letter of the following string on a new line.
#Remember to use len() to find the length of the string

word = "cryptography"

def print_elements(x):
    for i in x:
        print i

print_elements(word)        

##########################################
# (B)
##########################################

#Write a Python program that reverses the following word. Print the whole reversed word together.
word2 = "cybersecurity"






##########################################
# Lists
##########################################

#Here are some lists that you will use below. Do not change them.
a = [1,2,3,4,5,6,7,8,9,10]
b = [100,90,80,70,60,50,40,30,20,10]
c = [20,103,14,34,47,19,52,146,33,89]
d = [10,1,9,2,8,3,7,4,6,5]


##########################################
# (C)
##########################################

#Using loops, write a python function to sum all the items in a list. Do not use the sum() function.

def sum_of_list(list1):
    #write code here
    return # make sure you return something

    
#Tester
print(sum_of_list(a) == sum(a))
print(sum_of_list(b) == sum(b))
print(sum_of_list(c) == sum(c))
print(sum_of_list(d) == sum(d))
print("All should be True")


##########################################
# (D)
##########################################

#Using loops, write a python function to find the largest number in a list. Do not use the max() function

def max_num_in_list(list1):
    #write code here
    return #make sure you return something


print("")
print("Largest Number:")

#Tester
print(max_num_in_list(a) == max(a))
print(max_num_in_list(b) == max(b))
print(max_num_in_list(c) == max(c))
print(max_num_in_list(d) == max(d))
print("All should be True")


##########################################
# (E)
##########################################

#Write a Python function that takes two lists and returns True if they have at least one common member

def common_list(list1, list2):
    #write code here
    return #make sure you return something
    
print("")
print("Common Number:")

    
#Tester
print(common_list(a,b) == True)
print(common_list(a,c) == False)
print(common_list(a,d) == True)
print(common_list(b,c) == True)
print(common_list(b,d) == True)
print(common_list(c,d) == False)
print("All should be True")


##########################################
# (F)
##########################################

#Write a Python function to find the index of an item of a specified list
#If the item is not in the list, return a string that says so
def find_index(list1,item):
    #write code here
    return #make sure you return something

#Write some tester code for find_index   
    
    
##########################################
# Bonus 1
##########################################

#Write a Python program to get the difference between the sum of two lists
#You may call other previously written functions (Hint: (C))
def find_diff(list1,list2):
    #write code here
    return #make sure you return something

#Write some tester code for find_diff   


