message = input(">")
words = message.split(" ")

emogis = {
  ":)": "😀", # press ctrl + cmd + space to get emogi picker
  ":(": "🙁",
  ":*": "😘"
}

output = ""

for word in words:
  output += emogis.get(word, word) + " "

print(output)
