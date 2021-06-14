def maxSatisfied(customers, grumpy, minutes: int) -> int:
        sat_cust=0
        for x in range(len(customers)):
            if(len(customers)-x>minutes and grumpy[x]==0):
               sat_cust+=customers[x]
            elif(len(customers)-x<=minutes):
               print(x)
               sat_cust+=customers[x]
        print(sat_cust)

maxSatisfied([4,10,10],
[1,1,0],
2)          