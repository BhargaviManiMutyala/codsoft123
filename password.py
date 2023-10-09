import random
import array

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

length = int(input("Enter password length: "))
combined = digits + upper_case + lower_case + special_characters

rand_digit = random.choice(digits)
rand_upper = random.choice(upper_case)
rand_lower = random.choice(lower_case)
rand_symbol = random.choice(special_characters)

temp_password = rand_digit + rand_upper + rand_lower + rand_symbol

for _ in range(length - 4):
    temp_password += random.choice(combined)

temp_pass_list = array.array('u', temp_password)
random.shuffle(temp_pass_list)

password = ""
for char in temp_pass_list:
    password += char

print("Generated Password:", password)