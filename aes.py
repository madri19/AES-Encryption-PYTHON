from Crypto.Cipher import AES 
import binascii           
from Crypto import Random 

#use this given key
keyHex = b'\x2B\x7E\x15\x16\x28\xAE\xD2\xA6\xAB\xF7\x15\x88\x09\xCF\x4F\x3C'   
key = binascii.hexlify(keyHex).decode('ascii')                   
print("Key: " + key)      

#generate a random value for the vector
iv = Random.new().read(AES.block_size)           
print("Initialization Vector: " + iv)   

#generate your cipher with CFB and IV
cipher = AES.new(key, AES.MODE_CFB, iv)      

#use this given plaintext
plaintext = 'Iaintgoingdownforthis.Youainttakinmealive'          
print("Plaintext: " + plaintext) 

#generate the ciphertext with the cipher
msg = cipher.encrypt(plaintext)         
print("Ciphertext: " + msg.encode("hex")) 
