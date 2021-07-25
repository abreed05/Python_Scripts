#!/usr/bin/python
import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--passwordLength', type=int, required=True, help="Number of digits to generate for password. Must be a number")
args = parser.parse_args()


all_lowercase_chars = string.ascii_lowercase
all_uppercase_chars = string.ascii_uppercase
all_digits = string.digits
all_symbols = "~`!@#$%^&*()_-+=|\{\}\\[]/?.>,<"


# Creates a random password based on length and the 4 criteria lowercase, uppercase, numbers, and symbols. 
def createRandomPass():
    # pass_length = int(input("Please enter the number of characters for your password: "))
    create_password_list = random.sample(all_lowercase_chars + all_uppercase_chars + all_digits + all_symbols, args.passwordLength)
    convert_password_list_to_string = [str(x) for x in create_password_list]
    create_random_password = ''.join(convert_password_list_to_string)
    print(create_random_password)

createRandomPass()
