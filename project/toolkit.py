import pyfiglet
import os

ascii_banner = pyfiglet.figlet_format("Hello There!")
print(ascii_banner)

print("What can I do for you today?")
print("[1] Encrypt a file")
print("[2] Decrypt a file")
print("[3] Crack an MD5 Hash")
choice = int(input('Enter your choice: '))

ascii_banner = pyfiglet.figlet_format("-------------")
print(ascii_banner)

if choice == 1:
	inp_file = str(input('Enter the name/path of the file to encrypt: '))
	enc_method = str(input('Enter the cipher type: '))

	check1 = False
	form = open("formats.txt").read()
	formats = form.splitlines()
	for i in formats:
		if enc_method == i.strip(' '):
			check1 = True
	if check1 == 1:
		key = input('Enter the key you want to use for encryption: ')
		out_file = input('Enter the name/path of the ciphertext (output) file: ')
		command = "openssl enc " + enc_method + " -e -in " + inp_file + " -out " + out_file + " -k " + key
		os.system(command)
		print("[+] Encryption complete")

	else:
		print("[-] Enter a valid cipher... Below is the list of valid ciphers")
		os.system("openssl enc -list")
		print("quiting...")
		exit(1)
elif choice == 2:
	inp_file = str(input('Enter the name/path of the file to decrypt: '))
	enc_method = str(input('Enter the cipher type: '))

	check1 = False
	form = open("formats.txt").read()
	formats = form.splitlines()
	for i in formats:
		if enc_method == i.strip(' '):
			check1 = True
	if check1 == 1:
		key = input('Enter the key you want to use for decryption: ')
		out_file = input('Enter the name/path of the plaintext (output) file: ')
		command = "openssl enc " + enc_method + " -d -in " + inp_file + " -out " + out_file + " -k " + key
		os.system(command)
		print("[+] Decryption complete")
	else:
		print("[-] Enter a valid cipher... Below is the list of valid formats")
		os.system("openssl enc -list")
		print("quiting...")
		exit(1)
elif choice == 3:
	os.system("python3 hash_cracker.py")
else:
	print("[-] Enter a valid choice... quiting..")
	exit(1)

