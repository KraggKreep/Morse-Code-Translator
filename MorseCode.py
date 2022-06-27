myList = list("Use the Force Luke")
print(myList)

def morseAlphabet(letter):
  if letter == "a":
    return ".-"
  elif letter == "b":
    return "-..."
  elif letter == "c":
    return ".. ."
  elif letter == "d":
    return "-.."
  elif letter == "e":
    return "."
  elif letter == "f":
    return ".-."
  elif letter == "g":
    return "--."
  elif letter == "h":
    return "...."
  elif letter == "i":
    return ".."
  elif letter == "j":
    return "-.-."
  elif letter == "k":
    return "-.-"
  elif letter == "l":
    return "--"
  elif letter == "m":
    return "- -"
  elif letter == "n":
    return "-."
  elif letter == "o":
    return ". ."
  elif letter == "p":
    return "....."
  elif letter == "q":
    return "..-."
  elif letter == "r":
    return ". .."
  elif letter == "s":
    return "..."
  elif letter == "t":
    return "-"
  elif letter == "u":
    return "..-"
  elif letter == "v":
    return "...-"
  elif letter == "w":
    return ".--"
  elif letter == "x":
    return ".-.."
  elif letter == "y":
    return ".. .."
  elif letter == "z":
    return "... ."
  elif letter == " ":
    return "   "

def LettersToMorse(letters):
  for char in letters:
    lowerChar = char.lower()
    print(morseAlphabet(lowerChar))

LettersToMorse(myList)



