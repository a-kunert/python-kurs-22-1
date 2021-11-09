# Um eine Breite von 15 zu erreichen genügen schon 8 Zeilen
# Da die For-Schleifen, nie bis zur oberen Schranke gehen,
# setzen wir die Zeilenzahl auf 9

number_of_rows = 9

# Hier kommt die Baumkrone
for row in range(1, number_of_rows):
    number_of_stars = 2 * row - 1
    row_string = ""
    # Man braucht erst einige Leerzeichen
    for padding in range(1, number_of_rows - row):
        row_string = " " + row_string
    # Und dann kommen die Sterne
    for star in range(1, number_of_stars + 1):
        row_string = row_string + "*"
    print(row_string)

# Und hier der Stamm
for row in range(1, number_of_rows):
    row_string = ""
    for padding in range(1, number_of_rows - 2):
        row_string = " " + row_string
    row_string = row_string + "|||"
    print(row_string)
