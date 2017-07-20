import pprint
pp = pprint.PrettyPrinter(indent=4)

ciphertext1 = [68, 1, 45, 64, 219, 164, 162, 123, 55, 90, 19]
ciphertext2 = [72, 6, 57, 65, 193, 161, 170, 108, 63, 65, 24]

# PART 1: Get xored messages

xored_msgs = []
for i in range(len(ciphertext1)):
    xored_msgs = xored_msgs + [ciphertext1[i] ^ ciphertext2[i]]

print xored_msgs

# PART 2: Get letter pairs

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

letter_pairs = []

for i in range(len(xored_msgs)):
    letter_pairs = letter_pairs + [[]]
    for letter1 in alphabet:
        for letter2 in alphabet:
            if ord(letter1) ^ ord(letter2) == xored_msgs[i]:
                letter_pairs[i] = letter_pairs[i] + [(letter1, letter2)]

pp.pprint(letter_pairs)

# PART 3: Find valid words
with open("11letterwords.txt", "r") as f:
    word_list = f.read().split()

# 3.1: Do pair checking.  For each word, create its pair word, see if it's
# in the word list.

# 3.2.1: Write a function to compute the paired word, assuming every letter in
# the word has a pair.
def get_pair(word):
    # return the pair of this word
    return ""

# 3.2.2: Loop over the words and see if any of them have a valid pair
for word in word_list:
    # change this so it checks if the pair word is in the list
    []
        

