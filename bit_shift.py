#Name:
#CodeBreakers 2017
#Bit shift operations

#Define penguin, which is a list of strings with 43 characters each
penguin = [
	"                 .88888888:.               ",
	"                88888888.88888.            ", 
	"              .8888888888888888.           ",
	"              888888888888888888           ", 
	"              88' _`88'_  `88888           ",
	"              88 88 88 88  88888           ",  
	"              88_88_::_88_:88888           ", 
	"              88:::,::,:::::8888           ", 
	"              88`:::::::::'`8888           ",
	"             .88  `::::'    8:88.          ",
	"            8888            `8:888.        ", 
	"          .8888'             `888888.      ", 
	"         .8888:..  .::.  ...:'8888888:.    ", 
	"        .8888.'     :'     `'::`88:88888   ", 
	"       .8888        '         `.888:8888.  ", 
	"      888:8         .           888:88888  ",
	"    .888:88        .:           888:88888: ",  
	"    8888888.       ::           88:888888  ", 
	"    `.::.888.      ::          .88888888   ", 
	"   .::::::.888.    ::         :::`8888'.:. ", 
	"  ::::::::::.888   '         .:::::::::::: ", 
	"  ::::::::::::.8    '      .:8::::::::::::.", 
	" .::::::::::::::.        .:888:::::::::::::", 
	" :::::::::::::::88:.__..:88888:::::::::::' ", 
	"  `'.:::::::::::88888888888.88:::::::::'   ", 
	"        `':::_:' -- '' -'-' `':_::::'`     "
	] 

# ------------------ Coding begins here ----------------------------#

#1. Write a function to print all elements in input list X, No need to return anything here
def print2D(X):
	return #Not needed remove it!

print '\nOriginal Penguin: '
#2. Use previous function to print penguin. Your output should give you 1 penguin


#3. Write a function to shift each character in an string to the left/right by 1 bit
#	Input: in_string: input string, dxn= shift direction which is either left: 'l' or right: 'r'
#									for any other dxn, you should print an error message 'NOT AN OPTION'
#	Output: shifted sting if dxn is either 'l' or 'r', or '' i.e. empty string if dxn is neither
def shift_string(in_string, dxn):
	return 

print '\nShift string tests: '
# Both outputs should be True
print shift_string('42667', 'l')=='hdlln'
print shift_string('hdlln', 'r')=='42667'


#4. Use shift_string function to shift each element of an input list in an input direction
#	Function should return a list of shifted elements	
def shift_list(in_list, dxn):
	return 

print ('\nLeft Shift')
#5. Use shift_list and print2D function to print the penguin shifted to the left


print ('\nRight Shift')
#5. Use shift_list and print2D function to print the penguin shifted to the right


