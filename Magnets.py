n=int(input())
magnet=[]
for _ in range (n):
       magnet.append(input())
group=1
for i in range (n-1):
     if magnet[i]!=magnet[i+1]:
           group=group+1
print(group)
