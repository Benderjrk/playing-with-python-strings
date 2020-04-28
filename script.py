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