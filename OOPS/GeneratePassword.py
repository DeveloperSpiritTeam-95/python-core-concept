import random
import string

def generate_password(min_length,numbers = True,special_character = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_character:
        characters += special
    
    pwd = ""
    
    meet_criteria = False
    has_number = False
    has_special = False
    
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_character:
            meet_criteria = meet_criteria and has_special
    return pwd



min_length = int(input("Enter the minimum length:"))
has_numbers = input("Do you want to have numbers (y/n)?").lower() == "y"
has_special = input("Do you want to have special character (y/n)?").lower() == "y"

password = generate_password(min_length,has_numbers,has_special)
print("The Generated Password is:",password)