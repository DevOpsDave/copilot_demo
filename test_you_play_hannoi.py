import you_play_hannoi
from unittest.mock import MagicMock
from unittest import TestCase

def correct_moves_helper(towers_object):
    towers_object.move('A', 'C')
    towers_object.move('A', 'B')
    towers_object.move('C', 'B')
    towers_object.move('A', 'C')
    towers_object.move('B', 'A')
    towers_object.move('B', 'C')
    towers_object.move('A', 'C')

# All tests should pass.
class TestTowers(TestCase):
    
    def test_init_towers(self):
        t = you_play_hannoi.Towers(3, 3)
        t.print()
        assert t.towers == {'A': [3, 2, 1], 'B': [], 'C': []}
        
    def test_move(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        assert t.towers == {'A': [3, 2], 'B': [1], 'C': []}
        
    def test_move_illegal(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        with self.assertRaises(you_play_hannoi.IllegalMove):
            t.move('A', 'B')
            
    def test_is_game_over(self):
        # NOTE: This was not working correctly.  I had to help define the correct moves.
        # game is over when all disks are on the last tower,
        # and the last tower is in the correct order
        t = you_play_hannoi.Towers(3, 3)
        correct_moves_helper(t)
        assert t.is_game_over() == True
        
    def test_is_game_over_false(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        t.move('A', 'C')
        t.move('B', 'C')
        t.move('A', 'B')
        t.move('C', 'A')
        t.move('C', 'B')
        assert t.is_game_over() == False
        
    def test_get_number_of_moves(self):
        t = you_play_hannoi.Towers(3, 3)
        print(f'Starting towers: {t.towers}')
        correct_moves_helper(t)
        print(f'Number of moves: {t.get_number_of_moves()}')
        assert t.get_number_of_moves() == 7
        
    def test_get_number_of_moves_zero(self):
        t = you_play_hannoi.Towers(3, 3)
        assert t.get_number_of_moves() == 0
        
    def test_get_number_of_moves_one(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        assert t.get_number_of_moves() == 1
        
    def test_get_number_of_moves_two(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        t.move('A', 'C')
        assert t.get_number_of_moves() == 2

    def test_get_number_of_moves_three(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        t.move('A', 'C')
        t.move('B', 'C')
        assert t.get_number_of_moves() == 3
        
    def test_get_number_of_moves_four(self):
        t = you_play_hannoi.Towers(3, 3)
        t.move('A', 'B')
        t.move('A', 'C')
        t.move('B', 'C')
        t.move('A', 'B')
        assert t.get_number_of_moves() == 4

    
        
        
    

    
#class TestMain(TestCase):
    
#    def test_main(self):
#        you_play_hannoi.main(3, 3)
#        assert True

    
#if __name__ == '__main__':
#    TestTowers.
#    print('Test passed!')