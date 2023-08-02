#!/usr/bin/env python

# This is the towers of hanoi game.

class Towers(object):
    
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.towers = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }
        
    def __str__(self):
        return str(self.towers)
    
    # This is the recursive function that moves the disks.
    # It is called by the play() method.
    # It is a recursive function because it calls itself.
    # It is a helper function because it is not called by the user.    
    def move(self, n, a, b, c):
        if n == 1:
            self.towers[c].append(self.towers[a].pop())
            self.count += 1
            print(self)
        else:
            self.move(n-1, a, c, b)
            self.towers[c].append(self.towers[a].pop())
            self.count += 1
            print(self)
            self.move(n-1, b, a, c)  
            
    def play(self):
        print(self)
        self.move(self.n, 'A', 'B', 'C')
        
if __name__ == '__main__':
    # User input
    print('Welcome to the Towers of Hanoi game!')
    print('How many disks do you want to play with?')
    disks = int(input())
     
    t = Towers(disks)
    t.play()
    
    print('You won in', t.count, 'moves!')