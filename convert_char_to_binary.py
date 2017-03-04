###########################################
## Objective: Convert a character to bit ##
###########################################

#Get user input
original_char = input("Type the character (-1 to exit): ")

#Keeps asking for input as is different from -1
while original_char != "-1":
	print(bin(int(original_char, 16))[2:])
	original_char = input("Type the character (-1 to exit): ")