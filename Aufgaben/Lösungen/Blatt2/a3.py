word = input("Gib ein Wort an: ")
counter = 0

for letter in word:
    if letter == "a" or letter == "A":
        counter += 1  # shorthand for counter = counter + 1
    if letter == "e" or letter == "E":
        counter += 1
    if letter == "i" or letter == "I":
        counter += 1
    if letter == "o" or letter == "O":
        counter += 1
    if letter == "u" or letter == "U":
        counter += 1

print(f"Das Word {word} enthält {counter} Vokale")
