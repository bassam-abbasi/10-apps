

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
        
    def __repr__(self):
        return self.name
    
    
    def attack(self, creature: Creature):
        print('The wizard {} attacks {}'.format(self.name, creature.name))
        

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def __repr__(self):
        return self.name
        