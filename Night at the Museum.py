s=input()
ans=0
cur='a'
for c in s:
    diff=abs(ord(c)-ord(cur))
    ans+=min (diff,26-diff)
    cur=c
print(ans)
