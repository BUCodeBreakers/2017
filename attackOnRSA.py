import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Hash import SHA256
import tools

''' ------------------------------------- helpful tools ---------------------------------- '''
#read the file part1.py for more understanding of what all of these predefined things do. 
#text_to_int: takes in a string and returns an integer which can be used in RSA.
#int_to_text: takes in an integer and returns the corresponding string

''' ------------------------------------- Don't change this section ---------------------------------- '''
secparam = 2048

cipherTextMalland = sys.argv[2]
possibleMessages = sys.argv[3]
public = sys.argv[1]
pk = open(public, 'r')
publicKey = pk.read()
public_key = RSA.importKey(publicKey)

''' ------------------------------------- Editing begins here ---------------------------------- '''
#hint: use the helper functions up top! 
# use the PUBLIC KEY to encrypt 
f = open(possibleMessages)
lines=f.readlines()
message1 = lines[0]

#print "the first possibilitiy: ", ciphertext1

f=open(possibleMessages)
lines=f.readlines()
message2 = lines[1]

#print 'the second possibility: ', ciphertext2

f=open(possibleMessages)
lines=f.readlines()
message3 = lines[2]

#print "the third possibility: ", ciphertext3



''' ------------------------------------- Don't Change this ---------------------------------- '''
cipherFile = open(sys.argv[2], 'r').read()
cipherFile = cipherFile.strip()

''' ------------------------------------- Editing here ---------------------------------- '''

#what can we use to check if our encryption matches the cipher text?



''' ------------------------------------- to run your program, enter the following in terminal ---------------------------------- '''
#python2 part2.py part2_key.pub part2_ctext part2_messagespace
