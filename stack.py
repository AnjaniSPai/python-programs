'''stack is linear data structure where insertion happens from one end and deletion from other end.
it is LIFO.'''
'''implementation of stack
l=[1,2,3,4,5]
l.append(9)
l.pop()'''
class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for i in s:
            if len(st)==0:
                st.append(i)
            elif st[-1]=='A' and i=='B':
                st.pop()
            elif st[-1]=='C' and i=='D':
                st.pop()
        return  len(st)
