import random
class RandomizedSet:
    
    def __init__(self):
        self.container = []

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False
        else:
            self.container.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.container:
            return False
        else:
            self.container.remove(val)
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.container)
    

randomizedSet = RandomizedSet();
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())