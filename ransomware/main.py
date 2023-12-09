import sys

if len(sys.argv) == 2:

	script_name = sys.argv[0]

	operation = sys.argv[1]

	if operation.lower() == "encrypt":
		print("operation : encrypt")
	elif operation.lower() == "decrypt":
		print("operation : decrypt")
	else:
		print("Invalid operation. Please use 'encrypt' or 'decrypt'.")
else:
	print("Please provide exactly one command line argument.")
