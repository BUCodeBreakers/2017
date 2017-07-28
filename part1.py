from Crypto.PublicKey import RSA
#from Crypto.Hash import SHA
from Crypto.Hash import SHA256
import tools

# set the security parameter:
secparam = 2048

# generate an RSA key:
key = RSA.generate(secparam)
public_key = key.publickey()

# save the public and private keys to files and read them back:
open('key.pub', 'w').write(public_key.exportKey())
open('key.priv', 'w').write(key.exportKey())
# read the public key in:
recovered_public_key = RSA.importKey(open('key.pub', 'r').read())
assert recovered_public_key == public_key
# read the private key in:
recovered_key = RSA.importKey(open('key.priv', 'r').read())
assert recovered_key == key

# use the PUBLIC KEY to encrypt a message:
message = "I ATE SOME PIE"
message_int = tools.text_to_int(message)
ciphertext = public_key.encrypt(message_int, None)

# save the ciphertext to a file and read it back:
open('ciphertext', 'w').write(str(ciphertext))
recovered_ciphertext = eval(open('ciphertext', 'r').read())
assert recovered_ciphertext == ciphertext

# use the PRIVATE KEY to decrypt the message:
recovered_message_int = int(key.decrypt(ciphertext))
assert recovered_message_int == message_int

# use the PRIVATE KEY to sign a hash of the message:
hash = SHA256.new(message).digest()
signature = key.sign(hash, None)

# save the signature to a file and read it back:
open('signature', 'w').write(str(signature))
recovered_signature = eval(open('signature', 'r').read())
assert recovered_signature == signature

# use the PUBLIC KEY to verify the signature:
hash = SHA256.new(message).digest()
assert public_key.verify(hash, signature)

# We can also use math operations in Python to explore RSA signatures and ciphertexts.
# For instance, you can manually verify the signature.
# The modulus can be accessed as public_key.n, and the public exponent can be accessed as public_key.e.

print "%0128x" % pow(signature[0], public_key.e, public_key.n)

# The suffix of the signature^e mod n should be:

print SHA256.new(message).hexdigest()
