#Ask the user for a name, an adjective, a verb (past tense) and a place. Print a silly sentence using them.

name = input("Name: ")
adjective = input("Adjective: ")
verb = input("Verb (past tense): ")
place = input("Place: ")

result = f"{name} {adjective} to the {place} with a {adjective} grin."

print(result)