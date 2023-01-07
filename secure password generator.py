import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# Reading user data
count = int(input("How many passwords to generate for you? "))
lenght = int(input("How many characters should be in one password? "))
numbers = input("Do you include the numbers '0123456789' in your password? y/n ")
low_letters = input("Should lowercase 'abcdefghijklmnopqrstuvwxyz' be included? y/n ")
up_letters = input("Should uppercase 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' be included? y/n ")
punct = input("Should the characters '!#$%&*+-=?@^_' be included? y/n ")

if numbers.lower() == 'y':
    chars += digits
if low_letters.lower() == 'y':
    chars += lowercase_letters
if up_letters.lower() == 'y':
    chars += uppercase_letters
if punct.lower() == 'y':
    chars += punctuation

# Password generation
def generate_password(count, chars, lenght):
    for _ in range(count):
        print(*random.sample(chars, lenght), sep='')

generate_password(count, chars, lenght)