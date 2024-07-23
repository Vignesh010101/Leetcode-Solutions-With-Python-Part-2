class Solution:
    def minimumTeachings(self, n, languages, friendships):
        l = list(map(set,languages))
        users = set(chain(*((i-1,j-1) for i,j in 
                       friendships if not l[i-1]&l[j-1])))  
        if not users: return 0

        ctr = Counter(chain(*[languages[i] for i in users])) 
        return len(users) - max(ctr.values())                