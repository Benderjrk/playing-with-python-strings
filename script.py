favorite_word = "Skydiving"
print(favorite_word)

my_name = "Justin"

first_initial = my_name[0]

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  new_account = first_name[:3] + last_name[:3]
  return new_account

new_account = account_generator(first_name, last_name)
print(new_account)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  new_name = first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]
  return new_name

temp_password = password_generator(first_name, last_name)

print(temp_password)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

final_word = company_motto[-4:]

first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R"+first_name[1:]

password = "theycallme\"crazy\"91"

def get_length(string):
  length = 0
  for letter in string:
    length += 1
  return length

def letter_check(word, letter):
  for character in word:
    if character == letter:
      print(character)
      return True
  return False
    
print(letter_check("strawberry", "o"))


def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False
  
def common_letters(string_one, string_two):
    common_lst = []
    for character in string_one:
      if character in string_two and character not in common_lst:
        common_lst.append(character)
    return common_lst
print(common_letters("banana", "cream"))

def username_generator(first_name, last_name):
  username = ""
  if len(last_name) > 4 and len(first_name) > 3:
    username = first_name[:3] + last_name[:4]
  elif len(first_name) <= 3 and len(last_name) > 4:
    username = first_name + last_name[:4]
  elif len(last_name) <= 4 and len(first_name) > 3:
    username = first_name[:3] + last_name
  else:
    username = first_name + last_name
    
  return username

print(username_generator("Zoe", "Lee"))

def password_generator(username):
  password = ""
  previous_letter = ""
  for character in username:
  
    if password == "":
      password = password + username[-1:]
      previous_letter = character
    elif password != "":
      password = password + previous_letter
      previous_letter = character
  return password

password_generator(username_generator("Zoe", "Lee"))