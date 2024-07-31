class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.perimeter = [("East", [i+1,0]) for i in range(width-1)]
        self.perimeter.extend([("North", [width-1, i+1]) for i in range(height-1)])
        self.perimeter.extend([("West",  [width-2-i, height-1]) for i in range(width-1)])
        self.perimeter.extend([("South", [0, height-2-i]) for i in range(height-1)])
        self.width  = width
        self.height = height
        self.len_perimeter = len(self.perimeter)
        self.moved  = False
        self.steps  = 0
        
    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.steps += num
        self.moved = True
                    

    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.perimeter[(self.steps%self.len_perimeter)-1][1]
        

    def getDir(self):
        """
        :rtype: str
        """
        if not self.moved and self.getPos() == [0,0]:
            return "East"
        return self.perimeter[(self.steps%self.len_perimeter)-1][0]
        

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()