n=int(input())
s=input()
count=0
if len(s)==n:
    for i in range(n-1):
        if s[i]==s[i+1]:
            count=count+1
    print(count)
