example_list = [2, 7, 5, -1, 4, 12, 3, -19, 16]

# We add all items up, every second item is multiplied by 2 (i.e. weighting)
weighted_sum = 0
length_of_list = len(example_list)

for (index, number) in enumerate(example_list):
    if index % 2 == 0:
        # Remember: The first item in the list has index 0
        weighted_sum += number
    else:
        weighted_sum += 2*number

result = weighted_sum / length_of_list
print(f"Der gewichtete Durchschnitt ist {result}")


