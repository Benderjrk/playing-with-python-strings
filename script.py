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

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = "spring storm".title()
print(poem_title_fixed)

poem_author_fixed = "William Carlos Williams".upper()

print(poem_author_fixed)

line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

print(spring_storm_lines)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

print(reapers_line_one_words)

reapers_line_one = " ".join(reapers_line_one_words)

print(reapers_line_one)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  cleaned_line = line.strip()
  love_maybe_lines_stripped.append(cleaned_line)

print(love_maybe_lines_stripped)
print('')

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

print(toomer_bio_fixed)

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")

print(disown_placement)
print(god_wills_it_line_one[disown_placement:disown_placement+6])

def poem_title_card(poet, title):
  return 'The poem "{}" is written by {}.'.format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

.upper(), .title(), and .lower() adjust the casing of your string.
.split() takes a string and creates a list of substrings.
.join() takes a list of strings and creates a string.
.strip() cleans off whitespace, or other noise from the beginning and end of a string.
.replace() replaces all instances of a character/string in a string with another character/string.
.find() searches a string for a character/string and returns the index value that character/string is found at.
.format() and f-strings allow you to interpolate a string with variables.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print('')
# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  cleaned_poem = poem.strip()
  highlighted_poems_stripped.append(cleaned_poem)

# print('Lol')
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  poem_lst = poem.split(":")
  highlighted_poems_details.append(poem_lst)

# print(highlighted_poems_details)

titles, poets, dates = [], [], []

for details in highlighted_poems_details:
  titles.append(details[0])
  poets.append(details[1])
  dates.append(details[2])

# print('titles', titles)
# print('')
# print('poets', poets)
# print('')
# print('dates', dates)
for i in range(len(titles)):
  poem_description_string = "The poem {title} was published by {poet} in {date}".format(poet=poets[i],title=titles[i],date=dates[i])
  print(poem_description_string)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

# Uncomment these function calls to test your tip function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Write your count_char_x function here:
def count_char_x(word, x):
  number = word.count(x)
  return number
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
  	return(word[start_ind+1:end_ind])
  return word

# Uncomment these function calls to test your tip function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(' ')
  for word in words:
    if len(word) < x:
      return False
  return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


def word_lowercase(word):
  return word.lower()

def check_for_name(sentence, name):
  sanitazed_sentence = word_lowercase(sentence)
  sanitazed_name = word_lowercase(name)
  if sanitazed_name in sanitazed_sentence:
    return True
  else: 
    return False


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# Write your reverse_string function here:d
def reverse_string(word):
  new_word = ""
  for i in range(len(word) -1, -1, -1):
    new_word += word[i]
  return new_word
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  save_word_1 = word1
  save_word_2 = word2
  new_word_1 = save_word_1.replace(save_word_1[0],save_word_2[0])
  new_word_2 = save_word_2.replace(save_word_2[0],save_word_1[0])
  return "{word1} {word2}".format(word1=new_word_1, word2=new_word_2)
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Write your add_exclamation function here:
def add_exclamation(word):
  while len(word) < 20:
    word += "!"
  else:
    return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

