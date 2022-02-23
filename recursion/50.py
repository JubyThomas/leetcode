

    def myPow(x: float, n: int) -> float:
            if x==0:
                return 0
            elif n==0:
                return 1
            elif n>0:
                return Test.helper(x,n)
            elif n<0:
                return 1/Test.helper(x,n) 
            
        
        
    def helper(x,n):
            n=abs(n)
            temp= Test.myPow(x,n//2)
            if(n %2==0):
                return temp*temp
            else:
               return x*temp*temp
      

      

y=Test.myPow(2,7)
print(y)      