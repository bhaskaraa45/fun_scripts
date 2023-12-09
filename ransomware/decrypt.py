import os
from cryptography.fernet import Fernet

def decrypt_specific_file(file,key):
	with open(file, "rb") as specifiedFile:
		data = specifiedFile.read()
	decrypted_data = Fernet(key).decrypt(data)

	with open(file, "wb") as encryptedFile:
		encryptedFile.write(decrypted_data)

def decrypt_directory(path,key):
	for root, dirs, files in os.walk(path):
		for file in files:
			file_path = os.path.join(root,file)
			decrypt_specific_file(file_path,key)
