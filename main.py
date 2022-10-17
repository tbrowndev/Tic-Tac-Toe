import os
import time

class TicTacToe(object):
  def __init__(self) -> None:
    self.players = ['X', 'O']
    self.player_turn = 1
    self.spots = ['1','2','3','4','5','6','7','8','9']
    self.wins = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]
    
  
  def _markBoard(self, spot):
    '''
    Add player mark to board according to space selected.
    TODO: Check for valid space input
    '''
    while True:
      if self.spots[int(spot)-1]  == spot:
        self.spots[int(spot)-1] = self.players[self.player_turn]
        break
      else:
        selected_spot = input('Spot is taken choose another: ')
        spot = selected_spot
    

  def _setPlayerTurn(self):
    '''
    Set the next players turn
    '''
    if self.player_turn == 0:
      self.player_turn = 1
    else:
      self.player_turn = 0
    print(f'Player {self.players[self.player_turn]}\'s turn')
    
    
  def _checkWinner(self):
    '''
    Check for three of the same player marks in a row 
    '''
    for i in self.wins:
      if self.spots[i[0]] == self.spots[i[1]] == self.spots[i[2]]:
        os.system('clear')
        self._getBoard()
        print(f'Game over! Player {self.players[self.player_turn]} wins!')
        return True
    return False
    
  def _getBoard(self):
    '''
    Displays the board with (if any) player marks
    '''
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(self.spots[0], self.spots[1], self.spots[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(self.spots[3], self.spots[4], self.spots[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(self.spots[6], self.spots[7], self.spots[8]))
    print("\t     |     |")
    print()
    
  def playGame(self):
    '''
    Start the game
    '''
    print('Lets play a game of Tic Tac Toe!')
    print('Players ready? ')
    prog = 0
    while prog <=100:
      print("\r [{0}] {1}%".format('#'*(prog//10), prog), end='')
      prog += 1
      time.sleep(.1)
    print('\nLet\'s Begin!')
    time.sleep(1)
    
    while True:
      os.system('clear')
      self._setPlayerTurn()
      self._getBoard()
      player_selection = input(f'Select a spot to place {self.players[self.player_turn]} and press ENTER: ')
      self._markBoard(player_selection)
      if self._checkWinner():
        break
      
game = TicTacToe()
game.playGame()
