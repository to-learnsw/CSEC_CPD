n =int(input())
sums=0
for i in range(n):
     x,y,z=list(map(int,input().split()))
     if x+y+z>=2:
        sums+=1 
                   
print(sums)
