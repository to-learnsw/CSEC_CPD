k,r=map(int,input().split())
for i in range(1,11):
    cost=k*i
    if cost%10==r or cost%10==0:
        print(i)
        break
