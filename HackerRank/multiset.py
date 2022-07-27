class Multiset:
    
    def __init__(self) -> list:
        self.multiset = []
    
    def add(self, val):
        return self.multiset.append(val)

    def remove(self, val):
        if val in self.multiset:
            self.multiset.remove(val)
        else:
            False

    def __contains__(self, val):
        if val in self.multiset:
            return True
        else:
            return False
    
    def __len__(self):
        return len(self.multiset)


multiset1 = Multiset()
multiset1.add(2)
multiset1.add(2)
multiset1.add(2)
multiset1.__len__

