class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = set()
        self.family = {kingName:[]}
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)
        self.family[childName] = []
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        self.order = []

        def getOrder(person):
            if person not in self.dead:
                self.order.append(person)
            for child in self.family[person]:
                    getOrder(child)

        getOrder(self.king)    
        return self.order

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()