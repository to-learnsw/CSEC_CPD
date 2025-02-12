n=int(input())
team=[]
for _ in range(n):
      team.append(list(map(int,input().split())))
count=0
for j in range (n):
      for i in range(n):
            if i!=j and team[i][0]==team[j][1]:
                  count+=1
print(count)
