n=int(input())
card=list(map(int,input().split()))
seraja_score=0
dima_score=0
left=0
right=n-1
turn=0
while left<=right:
    if turn==0:
        if card[left]>card[right]:
            seraja_score+=card[left]
            left+=1
        else:
            seraja_score+=card[right]
            right-=1
    else:
            if card[left]>card[right]:
                 dima_score+=card[left]
                 left+=1
            else:
                dima_score+=card[right]
                right-=1
    turn=1-turn
print(seraja_score,dima_score)
