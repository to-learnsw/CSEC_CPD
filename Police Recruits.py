n=int(input())
events=list(map(int,input().split()))
avaliable_officer=0
untreated_crime=0
for event in events:
    if event>0:
        avaliable_officer+=event
    else:
         if avaliable_officer>0:
                 avaliable_officer+=event
         else:
              untreated_crime+=1
print(untreated_crime)
