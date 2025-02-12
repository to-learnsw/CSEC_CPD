n = int(input())
wires = list(map(int, input().split()))
m = int(input())
 
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  # Adjust to 0-based indexing
    y -= 1
 
    if x < 0 or x >= n or y < 0 or y >= wires[x]:
      continue
 
    left_birds = y
    right_birds = wires[x] - y - 1
    wires[x] = 0
 
    if x > 0:
        wires[x - 1] += left_birds
    if x < n - 1:
        wires[x + 1] += right_birds
 
for birds in wires:
    print(birds)
