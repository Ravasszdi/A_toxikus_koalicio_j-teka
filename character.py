class Character:
    def __init__(self, NAME, ORIGIN_WEIGHT, hunger, MAX_HUNGER, map):
        self.NAME = str(NAME)
        self.ORIGIN_WEIGHT = float(ORIGIN_WEIGHT)
        self.hunger = float(hunger)
        self.MAX_HUNGER = float(MAX_HUNGER)
        self.inventory = []        # <-- fixed
        self.map = str(map)

    def hunger_increase(self, amount: float = 1.0):
        self.hunger += amount
        
    def hunger_decrease(self, amount: float = 1.0):
        self.hunger -= amount
        
    def get_weight(self):
        return (self.hunger / 10) + self.ORIGIN_WEIGHT
    
    def get_MAX_WEIGHT(self):
        return (self.MAX_HUNGER / 10) + self.ORIGIN_WEIGHT
    
    def in_inventory(self, item: str) -> bool:
        return item in self.inventory
    
    def add_to_inventory(self, item = str):
            if isinstance(item, list)==False :
                self.inventory.append(item)
            else:
                for i in item:
                    self.inventory.append(i)