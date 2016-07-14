from Crypto.Cipher import AES
from Crypto import Random

testKey = bytes('1234567890123456', 'ascii')
testMessage = bytes('sixteen-byte msg', 'ascii')
ivLength = AES.block_size

def encrypt(message, key):
	"""plaintext -> iv + ciphertext.  Encrypts using AES CBC mode and returns
	   the iv attached to the ciphertext"""
	iv = Random.new().read(ivLength)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = cipher.encrypt(message)
	return iv + ciphertext

def decrypt(ivAndCiphertext, key):
	"""iv + ciphertext -> plaintext
	   To decrypt something of the form "iv + ciphertext, first get the
	   IV, then use it to decrypt the ciphertext"""
	#TODO 


