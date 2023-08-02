
hanoi_towers = {
    'A': [3, 2, 1],
    'B': [],
    'C': []   
}

def hanoi(n, a, b, c):
    if n == 1:
        hanoi_towers[c].append(hanoi_towers[a].pop())
        print(hanoi_towers)
    else:
        hanoi(n-1, a, c, b)
        hanoi_towers[c].append(hanoi_towers[a].pop())
        print(hanoi_towers)
        hanoi(n-1, b, a, c)
  
print(hanoi_towers)        
hanoi(3, 'A', 'B', 'C')