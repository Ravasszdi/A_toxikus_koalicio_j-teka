import character

Jonny = character.Character("Jonny Smith", 60.0, 50.0, 100.0, "konyha")
Jonny.add_to_inventory(["kés", "bor"])
print(Jonny.in_inventory("kés"))
Jonny.add_to_inventory("pálinka")
print(Jonny.inventory)