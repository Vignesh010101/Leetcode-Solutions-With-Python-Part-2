class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        # [0,1] - Север, [1,0] - Восток, [0, -1] - Юг, [-1, 0] - Запад
        vision = [[0,1], [1,0], [0, -1], [-1, 0]]
        I = 0
        go_to = vision[I]
        print(x, y)
        k = 0
        while k < 4:
            for move in instructions:
                if move == "G":
                    x += go_to[0]
                    y += go_to[1]
                    print(x, y)
                elif  move == "L":
                    if go_to == vision[0]:
                        go_to = vision[3]
                        I = 3
                    else:
                        I = I - 1
                        go_to = vision[I]
                elif  move == "R":
                    if go_to == vision[3]:
                        go_to = vision[0]
                        I = 0
                    else:
                        I = I + 1
                        go_to = vision[I]
            k += 1
        if x == 0 and y == 0:
            return True
        else:
            return False

