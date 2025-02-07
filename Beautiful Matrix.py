matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))
for r in range (5):
        for c in range(5):
            if matrix[r][c]==1:
                row_moves=abs(r-2)
                col_moves=abs(c-2)
                moves=row_moves+col_moves
                print (moves)
             
