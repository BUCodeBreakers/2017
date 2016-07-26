#Part 1: AES Confidentiality

# In your Ubuntu VM, load "Terminal".  Type in:
python3

# Enter the following into the shell (terminal):

from Crypto.Cipher import AES
import os

# Come up with a 16-character key and share it with someone.
key = 'ilikethiskey1234' # change this!

# Come up with a message that is as long as a multiple of 16 (16 characters,
# 32 characters, 48 characters....)
# DO NOT share the message with your friend!
message1 = 'sixteen-char msg'
message2 = 'this message has 0032 characters'

# We also have to generate a magic random number.  It's okay for us to share it!
# (Unlike a key, which we cannot share.)  We'll call it an IV (short for
# "initialization vector".  Don't worry about what it does,
# just know that it's necessary to make this work.
iv = os.urandom(len(key))

# Define a cipher object by doing this:
cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))

# The way this works, the ciphertext is the IV and the encryption of the message
# stuck together. Again, don't worry too much about what the IV actually is.
# Calculate the ciphertext and share it with the friend you gave the key.
ciphertext1 = iv + cipher.encrypt(message)
print(ciphertext1) # this will look like gibberish!

# Have your friend give you a new ciphertext called ciphertext2, encrypted with
# the same key.
ciphertext2 = #whatever your friend gives you...

# Then decrypt it!
cipher.decrypt(ciphertext2) # at the end of the decryption, you'll see
                            # your friend's original message!
