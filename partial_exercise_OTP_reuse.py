import pprint
pp = pprint.PrettyPrinter(indent=4)

ciphertext1 = [68, 1, 45, 64, 219, 164, 162, 123, 55, 90, 19]
ciphertext2 = [72, 6, 57, 65, 193, 161, 170, 108, 63, 65, 24]

# Part 1: get xored_msgs

xored_msgs = []
for c in range(len(ciphertext1)):
	elem1 = ciphertext1[c]
	elem2 = ciphertext2[c]
	elem_xor = elem1 ^ elem2
	xored_msgs = xored_msgs + [elem_xor]

#print xored_msgs

# xored_msgs = [12, 7, 20, 1, 26, 5, 8, 23, 8, 27, 11]

# Part 2: letter pairs
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letter_pairs = []

for target in xored_msgs:
	pairs_for_target = []
	for letter1 in alphabet:
		for letter2 in alphabet:
			xored_letters = ord(letter1) ^ ord(letter2)
			if xored_letters == target:
				pairs_for_target = pairs_for_target + [(letter1, letter2)]
	# pairs_for_target is now all pairs for target
	letter_pairs = letter_pairs + [pairs_for_target]

pp.pprint(letter_pairs)

# letter_pairs[i] is the list of pairs that lead to xored_msgs[i]


# STEP 3: which words can we make out of these letter pairs?

with open("11letterwords.txt", "r") as f:
	word_list = f.read().split()

#print word_list

# for each word in word_list:
	# create that word's pair_word
	# check and see whether the pair_word is also in word_list
	# there is only one pair of words that works that are both in word_list



