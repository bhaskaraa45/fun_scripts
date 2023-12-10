import sys
from cryptography.fernet import Fernet

#total argument should be two , scrpit_name + one argument
if len(sys.argv) == 2:
	script_name = sys.argv[0]
	operation = sys.argv[1]

	if operation.lower() == "encrypt":
		print("operation : encrypt")
	elif operation.lower() == "decrypt":
		with open("encrytion_key.key" , "rb") as keyFile:
			key = keyFile.read()
		decryptDir("../target_dir",key)
		print("operation : decrypt")
	else:
		print("Invalid operation. Please use 'encrypt' or 'decrypt'.")
else:
	print("Please provide exactly one command line argument.")


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
