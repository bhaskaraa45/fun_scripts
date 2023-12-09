import os
from cryptography.fernet import Fernet

def encrypt_specific_file(file,key):
	with open(file, "rb") as specifiedFile:
		data = specifiedFile.read()
	encrypted_data = Fernet(key).encrypt(data)

	with open(file, "wb") as encryptedFile:
		encryptedFile.write(encrypted_data)




def encrypt_directory(path, key):
	for root, dirs, files in os.walk(path):
		for file in files:
			file_path = os.path.join(root, file)
			encrypt_specific_file(file_path, key)





