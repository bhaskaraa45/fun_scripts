import sys
from encrypt import encrypt_specific_file as fileEncription
from cryptography.fernet import Fernet
from encrypt import encrypt_directory as encryptDir
from decrypt import decrypt_directory as decryptDir

#total argument should be two , scrpit_name + one argument
if len(sys.argv) == 2:
	script_name = sys.argv[0]
	operation = sys.argv[1]

	if operation.lower() == "encrypt":

		key = Fernet.generate_key()

		with open("encrytion_key.key" , "wb") as keyFile:
			keyFile.write(key)

		encryptDir("../target_dir", key)
		#fileEncription("./test.txt",key)
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
