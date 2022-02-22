rectangles = [[5,8],[1,9],[3,7],[2,5]]




s= [ min(x,y) for x,y in rectangles]
 
x=s.count((max(s)))    
print(x)