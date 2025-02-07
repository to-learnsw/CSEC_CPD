n,h=list(map(int,input().split()))
while True:
       freind_heights=list(map(int,input().split()))
       if not len(freind_heights)==n:
               break
       width=0
       for height in freind_heights:
             if (1<=height<=2*h):
                       if(height>h):
                                width=width+2
                       else:
                               width=width+1
       print(width)
       break
