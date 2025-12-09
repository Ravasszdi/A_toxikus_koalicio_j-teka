class Character:
    def __init__(self, NAME, ORIGIN_WEIGHT, hunger, MAX_HUNGER, map):
        self.NAME = str(NAME)
        self.ORIGIN_WEIGHT = float(ORIGIN_WEIGHT)
        self.hunger = float(hunger)
        self.MAX_HUNGER = float(MAX_HUNGER)
        self.inventory = []
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
                    
    def privat_find_item(self, item = str) -> int:
        item_index = 0
        for i in range(len(self.inventory)):
            if self.inventory[i]==item:
                item_index = i
        return item_index

    def use_and_remove_item(self, item = str)->bool:
        if self.in_inventory(item):
            item_index = self.privat_find_item(item)
            self.inventory.pop(int(item_index))
            return True
        else:
            return False