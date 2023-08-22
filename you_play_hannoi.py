#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import signal
import sys
import string

class IllegalMove(Exception):
    pass

class Towers(object):
    # This class will keep the state of the towers.
    # This is not the game class.
    # These methods will be public:
    # move(src_tower, dest_tower) - move the top disk from src_tower to dest_tower
    # print() - print the state of the towers
    # get_number_of_moves() - return the number of moves
    # is_game_over() - return True if the game is over, False otherwise
    # computer_solve() - solve the game using the computer
    # These methods will be private:
    # __init__(number_of_disks, number_of_towers) - initialize the towers
    # __str__() - return a string representation of the towers
    # __repr__() - return a string representation of the towers as visual plot
    
    def __init__(self, number_of_disks, number_of_towers=3):
        self.number_of_disks = number_of_disks
        self.number_of_towers = number_of_towers
        self.number_of_moves = 0
        self.towers = {}
        for i in zip(string.ascii_uppercase, range(number_of_towers)):
            if i[1] == 0:
                self.towers[i[0]] = list(range(number_of_disks, 0, -1))
            else:
                self.towers[i[0]] = []
            
        
    def __str__(self):
        return str(self.towers)
    
    def __repr__(self) -> str:
        # This method will return a string representation of the towers as visual plot.
        self.visual_plot = np.zeros((self.number_of_disks, self.number_of_towers))
        # print(self.visual_plot)
          
    def move(self, src_tower, dest_tower):
        # This method will move the top disk from src_tower to dest_tower.
        # src_tower and dest_tower are strings and will be sanitized to upper case.
        # It will check if the move is legal.
        # It will raise an IllegalMove exception if the move is illegal.
        # It will increment the number of moves.
        # It will return a tuple of if the game is over and the number of moves.
        
        if src_tower == dest_tower:
            raise IllegalMove('Source tower and destination tower are the same!')
        src_tower = src_tower.upper()
        dest_tower = dest_tower.upper()
        
        if src_tower not in self.towers.keys() or dest_tower not in self.towers.keys():
            raise IllegalMove('Tower does not exist!')
        if len(self.towers[src_tower]) == 0:
            raise IllegalMove('Source tower is empty!')
        if len(self.towers[dest_tower]) != 0 and self.towers[src_tower][-1] > self.towers[dest_tower][-1]:
            raise IllegalMove('Source disk is larger than destination disk!')
        #if len(self.towers[dest_tower]) == 0:  # this condition is not necessary.  Copilot put it in.
        #    self.towers[dest_tower].append(self.towers[src_tower].pop())
        #    self.number_of_moves += 1
        else:
            self.towers[dest_tower].append(self.towers[src_tower].pop())
            self.number_of_moves += 1
        return self.is_game_over(), self.number_of_moves
    
    def print(self):
        # This method will print the state of the towers.
        print(f'{self.towers} --- Number of moves: {self.number_of_moves}')
        
    def get_number_of_moves(self):
        # This method will return the number of moves.
        print(self.number_of_moves)
        return self.number_of_moves
        
    def is_game_over(self):
        # This method will return True if the game is over, False otherwise.   NOTE: the below comment wrote the correct code.  Before it did not have the list() around the keys() method.
        # If the length of the last tower is equal to the number of disks, then the game is over.
        if len(self.towers[list(self.towers.keys())[-1]]) == self.number_of_disks:
            return True
        else:
            return False
         
def signal_handler(sig, frame):
    # This function will trap control-c and exit with a message saying "Thanks for playing!"
    print(f'\n\nThanks for playing!')
    sys.exit(0)
         
def main(number_of_disks, number_of_towers):
    # This is the main program that will run when you execute this file.
    # It will ask the user for the number of disks and the number of towers.
    # It will create a Towers object.
    # It will print the state of the towers.
    # Inside a while loop:
    # It will ask the user for a source tower and a destination tower.
    # It will move the top disk from the source tower to the destination tower.
    # It will print the state of the towers and number of moves in an attractive way.
    # check to see if the game is over
    # If game is over, it will print the number of moves and a congratulatory message.
    # It will ask the user if they want to play again.  If yes, it will reset the game.
    # If no, it will exit the program.
    # Main function will trap control-c and exit with a message saying "Thanks for playing!" # NOTE: this is a late comment.  Copilot was smart enough to know I didn't want to use a big try/except block.
    # If the user enters an invalid input, it will ask the user to enter a valid input.
    # If the user enters an illegal move, it will ask the user to enter a legal move.
    # If the user enters an illegal tower, it will ask the user to enter a legal tower.
    # If the user enters an illegal number of disks, it will ask the user to enter a legal number of disks.
    # If the user enters an illegal number of towers, it will ask the user to enter a legal number of towers.
    
    
    # Create a Towers object.
    towers = Towers(number_of_disks, number_of_towers)
    
    # Inside a while loop:
    while True:
        # Ask the user for a source tower and a destination tower.
        while True:
            print(f'Towers: {towers} --- Number of moves: {towers.number_of_moves}')
            try:
                src_tower = input('Enter the source tower: ')
                dest_tower = input('Enter the destination tower: ')
                print(f'\n')
                break
            except ValueError:
                print('Please enter a valid tower!')
        # Move the top disk from the source tower to the destination tower.
        try:
            towers.move(src_tower, dest_tower)
        except IllegalMove as e:
            print(e)
        # Print the state of the towers and number of moves in an attractive way.
        # check to see if the game is over
        # If game is over, it will print the number of moves and a congratulatory message.
        if towers.is_game_over():
            print(f'Congratulations! You won in {towers.number_of_moves} moves!')
            break
       
        # If the user enters an illegal move, it will ask the user to enter a legal move.
        # If the user enters an illegal tower, it will ask the user to enter a legal tower.
        # If the user enters an illegal number of disks, it will ask the user to enter a legal number of disks.
        # If the user enters an illegal number of towers, it will ask the user to enter a legal number of towers.
    
# Call the main function.
if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)
    
    # Ask the user for the number of towers.
    while True:
        try:
            number_of_towers = int(input('Enter the number of towers: '))
            break
        except ValueError:
            print('Please enter an integer!')
    # Ask the user for the number of disks.
    while True:
        try:
            number_of_disks = int(input('Enter the number of disks: '))
            break
        except ValueError:
            print('Please enter an integer!')
    
    main(number_of_disks, number_of_towers)