a1,a2,a3,a4=map(int,input().split())
s=input()
calories=0
for char in s:
    if char=='1':
         calories+=a1
    elif char=='2':
           calories+=a2
    elif char=='3':
            calories+=a3
    else:
          calories+=a4
print(calories)
