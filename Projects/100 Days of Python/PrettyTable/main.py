from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"], "l")
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"], "c")
print(table)