#Part 1: AES Confidentiality

# In your Ubuntu VM, load "Terminal".  Type in:
python3

# Enter the following into the shell (terminal):

from Crypto.Cipher import AES

# Come up with a 16-character key and share it with someone.
key = 'ilikethiskey1234' # change this!

# Come up with a message that is as long as a multiple of 16 (16 characters,
# 32 characters, 48 characters....)
# DO NOT share the message with your friend!
message1 = 'sixteen-char msg'
message2 = 'this message has 0032 characters'


# Define a cipher object by doing this:
cipher = AES.new(key)

# Calculate the ciphertext and share it with the friend you gave the key.
ciphertext1 = cipher.encrypt(message)
print(list(ciphertext1)) # this will look like gibberish!

# Have your friend give you a new ciphertext called ciphertext2, encrypted with
# the same key.
ciphertext2 = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) #whatever your friend gives you...

# Then decrypt it!
cipher.decrypt(ciphertext2) # at the end of the decryption, you'll see
                            # your friend's original message!
