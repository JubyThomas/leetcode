"""
program to print a number pattern like
1
121
12321
"""

s=""
for i in range(1,4):
    s+=str(i)
    if i==1:
        print(i)
    else:
       strlen=len(s)
       revers=s[0:strlen-1]
       print(s+revers[::-1])
             