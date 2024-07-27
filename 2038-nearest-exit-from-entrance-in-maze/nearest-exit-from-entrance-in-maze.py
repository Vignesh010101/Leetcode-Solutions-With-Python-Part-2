class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        len_y = len(maze)-1
        len_x = len(maze[0])-1

        if len_x==0 and len_y==0:
                return -1

        queue = collections.deque()


        queue.append((entrance[0],entrance[1]))

        maze[entrance[0]][entrance[1]] = 2
        moves=0
        while queue:

                for i in range(len(queue)):
                        current_y, current_x = queue.popleft()


                        if not (current_x== entrance[1] and current_y== entrance[0]) and (current_y==0 or current_y == len_y or current_x== 0 or current_x ==len_x):
                                return moves


                        #up
                        if current_y-1>=0 and maze[current_y - 1][current_x] == '.':
                                queue.append((current_y-1,current_x))
                                maze[current_y-1][current_x]=2
                        # down
                        if current_y+1 <= len_y and maze[current_y + 1][current_x] == '.':
                                queue.append((current_y + 1, current_x))
                                maze[current_y+1][current_x] = 2
                        #left
                        if current_x-1 >=0 and maze[current_y][current_x-1] == '.':
                                queue.append((current_y, current_x-1))
                                maze[current_y][current_x-1] = 2
                        #right
                        if current_x+1 <=len_x and maze[current_y][current_x+1] == '.':
                                queue.append((current_y, current_x+1))
                                maze[current_y][current_x+1] = 2


                moves+=1

        return -1