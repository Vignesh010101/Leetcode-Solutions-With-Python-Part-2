class Node:
    def __init__(self, v: int = 0):
        self.v = v
        self.children = [] # empty, or 4 children

    def update(self, ur1, ur2, uc1, uc2, uv, nr1, nr2, nc1, nc2) -> None:
        """Updates this node's value/children, spanning nr/nc, with the update ur, uc range"""

        # print(f"update: {ur1, ur2} x {uc1, uc2}, {uv=}: applying to node {nr1, nr2} x {nc1, nc2}")

        if ur1 <= nr1 and nr2 <= ur2 and uc1 <= nc1 and nc2 <= uc2:
            # whole node region is updated
            self.children = [] # prune children
            self.v = uv
            # print(f"  set whole region")
            return

        or1 = max(ur1, nr1)
        or2 = min(ur2, nr2)
        if or1 > or2: 
            # print("  no row overlap")
            return # no row overlap

        oc1 = max(uc1, nc1)
        oc2 = min(uc2, nc2)
        if oc1 > oc2: 
            # print("  no column overlap")
            return

        mr = (nr1+nr2)//2
        mc = (nc1+nc2)//2

        if not self.children:
            self.children = [Node(self.v) for _ in range(4)]

        # 0 1
        # 2 3
        self.children[0].update(ur1, ur2, uc1, uc2, uv, nr1, mr, nc1, mc)
        self.children[1].update(ur1, ur2, uc1, uc2, uv, nr1, mr, mc+1, nc2)
        self.children[2].update(ur1, ur2, uc1, uc2, uv, mr+1, nr2, nc1, mc)
        self.children[3].update(ur1, ur2, uc1, uc2, uv, mr+1, nr2, mc+1, nc2)

        if all(not c.children for c in self.children):
            # all children are leaves
            if all(c.v == self.children[0].v for c in self.children[1:]):
                # all children are the same: prune to make this a leaf
                self.v = self.children[0].v
                self.children = []

    def get(self, r, c, nr1, nr2, nc1, nc2) -> int:
        """PRE: r, c is somewhere in this node"""

        # print(f"get: {r=}, {c=}: current node is {nr1, nr2} x {nc1, nc2}")
        if self.children:
            # print("  not a leaf: getting value from child")
            mr = (nr1+nr2)//2
            mc = (nc1+nc2)//2

            # this would be simpler if nodes stored their own ranges
            i = 0

            if r > mr:
                i += 2
                cr1, cr2 = mr+1, nr2
            else:
                cr1, cr2 = nr1, mr

            if c > mc:
                i += 1
                cc1, cc2 = mc+1, nc2
            else:
                cc1, cc2 = nc1, mc

            return self.children[i].get(r, c, cr1, cr2, cc1, cc2)
        else:
            # print(f"  {self=} is a leaf with {self.v=} and {self.children=}")
            return self.v


class SubrectangleQueries:
    
    def __init__(self, rectangle: List[List[int]]):
        # GO HARD: quad tree
        self.root = Node()
        self.L = max(len(rectangle), len(rectangle[0]))
        
        for r, row in enumerate(rectangle):
            for c, v in enumerate(row):
                self.root.update(r, r, c, c, v, 0, self.L-1, 0, self.L-1)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.root.update(row1, row2, col1, col2, newValue, 0, self.L-1, 0, self.L-1)

    def getValue(self, row: int, col: int) -> int:
        return self.root.get(row, col, 0, self.L-1, 0, self.L-1)

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)