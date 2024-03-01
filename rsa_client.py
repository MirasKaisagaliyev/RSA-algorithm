from rsa_final import RSA
import pickle

import os

def encrypt_decrypt_cycle(encryptor, decryptor):

	print("Public Key encryptor ", encryptor.public_key)
	print("Private Key encryptor ", encryptor.private_key)
	print("Friends Key encryptor ", encryptor.friend_Key)	
	print("Friends Key decryptor ", decryptor.friend_Key)
	print("Public Key decryptor ", decryptor.public_key)
	print("Private Key decryptor ", decryptor.private_key)
		
	file_path = input(" - Enter the path to the file to encrypt with your public key: ")	
	file_dir, file_name = os.path.split(file_path)
	encrypted_file_path = os.path.join(file_dir, "encrypted_" + file_name)
	encrypted_data = encryptor.encrypt_file(file_path)

	with open(encrypted_file_path, 'wb') as f:
		pickle.dump(encrypted_data, f)

	print(" - Your file has been encrypted and saved as:", encrypted_file_path)

	decryption_choice = input(" - Do you want to decrypt the file? (yes/no): ").lower()
	if decryption_choice == "yes":
		with open(encrypted_file_path, 'rb') as f:
			encrypted_data = pickle.load(f)
		decrypted_data = decryptor.decrypt_file(encrypted_data)
		decrypted_file_path = input(" - Enter the path to save the decrypted file: ")

		with open(decrypted_file_path, 'wb') as f:
			for byte in decrypted_data:
				f.write(byte.to_bytes(1, byteorder='big'))

		print(" - Your file has been decrypted and saved as:", decrypted_file_path)
	else:
		print(" - Thank you. Exiting...")

	print(" ")
	print("============================================ END ==========================================================")
	print("===========================================================================================================")



def Main():

	encryptor = RSA(17, 19)
	decryptor= RSA(17, 23)

	decryptor.friend_Key = encryptor.public_key
	encryptor.friend_Key = decryptor.public_key


	encrypt_decrypt_cycle(encryptor, decryptor)


Main()