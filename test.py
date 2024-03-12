# animals = ["lapin", "chat", "chien", "elephant", "tortue"]
# definitions = ["mignon", "sympa", "sauter", "lourd"]


# dict_animals_1 = {a : b for a, b in zip(animals, definitions)}


# for element in animals:
# 	print(element)

# print("_"*60)

# for index in range(len(animals)):
# 	print(animals[index])

# print("_"*60)

# for index, animal in enumerate(animals):
# 	print(index)
# 	print(animal)



# dict_animals_2 = {"chat": "mignon", "chien": "sympa", "lapin": "sauter", "éléphant":"lourd"}

# for animal in dict_animals_2.keys():
# 	print(animal)


# for definition in dict_animals_2.values():
# 	print(definition)

# for animal, definition in dict_animals_2.items():
# 	print(animal, definition)

nombres_maisons = 1000
print(f"il y a {nombres_maisons} maison{"s" if nombres_maisons>1 else ''}")