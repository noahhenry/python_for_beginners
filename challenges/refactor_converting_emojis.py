# refactor the "converting_emojis.py" into a reusable function
emogis = {
  ":)": "😀", # press ctrl + cmd + space to get emogi picker
  ":(": "🙁",
  ":*": "😘"
}

def convert_special_characters_to_emojis(message):
  words = message.split(" ")

  output = ""

  for word in words:
    output += emogis.get(word, word) + " "

  return output


print(convert_special_characters_to_emojis(message=input(">")))
