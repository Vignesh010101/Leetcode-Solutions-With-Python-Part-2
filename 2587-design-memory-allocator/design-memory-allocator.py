import heapq
class Allocator:

    def __init__(self, n: int):
        self.ht={}
        self.freeMemeory=[[0, n]]

    def allocate(self, size: int, mID: int) -> int:
        if self.freeMemeory:
            self.refreshMemeory()
        val = self.giveFreeMemeory(size)
        if not val:
            return -1
        # one mID can have multiple occurrences, so need to keep track of all occurrences.
        if mID in self.ht:
            self.ht[mID].append(val)
        else:
            self.ht[mID]=[val]
        return val[0]
        

    def free(self, mID: int) -> int:
        if self.freeMemeory:
            self.refreshMemeory()
        if mID not in self.ht or not self.ht[mID]:
            return 0
        size=0
        # suppose we have multiple occurrences of 1 then in that case we need to remove all the occurrences and return the total size.
        for ids in self.ht[mID]:
            size+=ids[1]-ids[0]
            heapq.heappush(self.freeMemeory,ids)
        # need to reset the HashTable, once every occurrences are removed
        self.ht[mID]=[]
        return size

    # giveFreeMemeory is to return FIRST FREE MEMORY which comes in the range of size.
    def giveFreeMemeory(self, size):
        temp=[]
        send=[]
        while self.freeMemeory:
            start, end = heapq.heappop(self.freeMemeory)
            if (end-start)>=size:
                if (end-start)>size:
                    heapq.heappush(self.freeMemeory,[start+size, end])
                send=[start, start+size]
                break
            else:
                temp.append([start, end])
        if temp:
            for i in range(len(temp)):
                heapq.heappush(self.freeMemeory,temp[i])
        if not send:
            return 0
        return send

    # refreshMemeory function helps us to refactor the memory, suppose we have [[40,50], [12,40]] so this is nothing but [[12,50]], our refreshMemory function will help us do the same.
    def refreshMemeory(self):
        start, end = heapq.heappop(self.freeMemeory)
        temp=[[start, end]]
        while self.freeMemeory:
            newStart, newEnd = heapq.heappop(self.freeMemeory)
            if end==newStart:
                temp.pop()
                end=newEnd
            else:
                start=newStart
                end=newEnd
            temp.append([start, end])
        if temp:
            for i in range(len(temp)):
                heapq.heappush(self.freeMemeory,temp[i])
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)