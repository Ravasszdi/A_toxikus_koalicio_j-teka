class character:
    def __init__(name ,hunger, inventory, map):
        self.name = str(name)
        self.hunger = float(hunger)
        self.inventory = list(str(inventory))
        self.map = str(map)

    def hunger_increase(self ,amount = int):
        self.hunger += amount
        
    def hunger_decrease(self ,amount = int):
        self.hunger -= amount