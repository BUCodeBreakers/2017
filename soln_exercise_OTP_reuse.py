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

# 3.1: Reduce search space.  Figure out which words work AT ALL.
reduced_word_list = []

# 3.1.1: Build list of letters that can go in this spot *at all*
valid_letters = []
for i in range(len(letter_pairs)):
    valid_letters = valid_letters + [[]]
    for pair in letter_pairs[i]:
        valid_letters[i] = valid_letters[i] + [pair[0]]

# 3.1.2: Build function to test whether a word is allowed or not
def word_is_okay(word):
    for i in range(len(xored_msgs)):
        if word[i] not in valid_letters[i]:
            return False
    return True

# 3.1.3: Loop over words, only keep words that are allowed
for word in word_list:
    if word_is_okay(word):
        reduced_word_list = reduced_word_list + [word]

# You should have 1354 options left at this point (reduced_word_list should be
# 1354 long)

#print reduced_word_list
#print len(reduced_word_list)

# 3.2: Now do pair checking.  For each word, create its pair word, see if it's
# in the word list.

# 3.2.1: Write a function to compute the paired word, assuming every letter in
# the word has a pair.
def get_pair(word):
    pair_word = ""
    for i in range(len(word)):
        letter = word[i]
        for pair in letter_pairs[i]:
            if pair[0] == letter:
                pair_word = pair_word + pair[1]
    return pair_word

#for word in reduced_word_list:
for word in word_list:
    pair_word = get_pair(word)
    if pair_word in reduced_word_list:
        print "we're done!  words are:"
        print word
        print pair_word



        

