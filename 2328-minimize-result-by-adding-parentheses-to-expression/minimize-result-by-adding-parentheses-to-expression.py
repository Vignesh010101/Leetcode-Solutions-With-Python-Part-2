class Solution:
    def minimizeResult(self, exp: str) -> str:
        x,y=exp.split('+')
        maxx=int(x)+int(y)
        # print(maxx)
        exp=list(exp)
        plus=exp.index('+')
        
        lhs=[]
        ans=''
        for j in range(0,plus):
            if not j:
                left=1
                bleft=int(''.join(exp[:plus]))
            else:
                left=int(''.join(exp[:j]))
                bleft=int(''.join(exp[j:plus]))
            
            lhs.append([left,bleft])   
        # print(lhs)      
        rhs=[]
        for i in range(len(exp)-1,plus,-1):
            if i==len(exp)-1:
                rite=1
                brite=int(''.join(exp[plus+1:]))
            else:
                rite=int(''.join(exp[i+1:]))
                brite=int(''.join(exp[plus+1:i+1]))
            rhs.append([brite,rite])    
        # print(lhs,rhs)   
        
        for idx,i in enumerate(lhs):
            for jdx,j in enumerate(rhs):
                temp=i[0]*(i[1]+j[0])*j[1]
                if temp<maxx:
                    maxx=temp
                    ans=''
                    if idx==0:
                        ans+='('+str(i[1])+'+'
                    else:
                        ans+=str(i[0])+'('+str(i[1])+'+'
                    if jdx==0:
                        ans+=str(j[0])+')'
                    else:
                        ans+=str(j[0])+')'+str(j[1])
        return ans if ans else '('+''.join(exp)+')'              
                
            
            
        