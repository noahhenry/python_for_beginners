# note: just learned about python dicionaries...
number_to_word_dictionary = {
  "1": "One ",
  "2": "Two ",
  "3": "Three ",
  "4": "Four ",
  "5": "Five ",
  "6": "Six ",
  "7": "Eight ",
  "9": "Nine ",
  "0": "Zero "
}

user_input = input()
for char in user_input:
  word = number_to_word_dictionary[char]
  print(word)


# challenge: get users phone number and convert input to words
phone = input("Phone: ")

digits_mapping = {
  "1": "One ",
  "2": "Two ",
  "3": "Three ",
  "4": "Four ",
  "5": "Five ",
  "6": "Six ",
  "7": "Eight ",
  "9": "Nine ",
  "0": "Zero "
}

output = ""

for char in phone:
  output += digits_mapping.get(char, "!") + " " # the get() returns a none object if it does not find the lookup... It also allows a default value.

print(output)