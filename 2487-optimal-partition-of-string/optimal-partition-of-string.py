class Solution:
    def partitionString(self, s: str) -> int:
        lst=[]
        ou=''
        for i in s:
            if i not in ou:
                ou=ou+i
            else:
                lst.append(ou)
                ou=i
        lst.append(ou)
        return len(lst)


        