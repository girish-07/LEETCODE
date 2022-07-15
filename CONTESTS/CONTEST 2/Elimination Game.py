class Solution:
    def lastRemaining(self, n: int) -> int:
        head=1
        step=1
        dir=True
        while(n>1):
            if(dir):
                head+=step
            else:
                if(n%2==0):
                    head=head
                else:
                    head=head+step
            n = n//2
            dir=not dir
            step*=2
        return head
            
