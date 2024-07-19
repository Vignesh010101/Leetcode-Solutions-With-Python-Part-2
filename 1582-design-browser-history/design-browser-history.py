class BrowserHistory:
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.end = 0
        self.currWebsite = 0 

    def visit(self, url: str) -> None:
        if self.currWebsite == self.end : 
            if self.end == len(self.arr)-1 :
                self.arr.append(url)
            else :
                self.arr[self.end+1] = url
            self.end+=1
            self.currWebsite = self.end 
        else : 
            self.arr[self.currWebsite+1] = url
            self.currWebsite += 1
            self.end = self.currWebsite

    def back(self, steps: int) -> str:
        if self.currWebsite-steps >= 0 :
            self.currWebsite -= steps
            return self.arr[self.currWebsite]
        else :
            self.currWebsite = 0
            return self.arr[0]

    def forward(self, steps: int) -> str:
        if self.currWebsite + steps <= self.end :
            self.currWebsite += steps
            return self.arr[self.currWebsite]
        else :
            self.currWebsite = self.end
            return self.arr[self.end]  

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)