from connect_4_functions import *
row = int(input("enter board row size. "))
column = int(input("enter board column size. "))
board = make_board(row,column)
print(print_board(board))
score = "."
while score == '.':
    c = int(input('R move: which column? '))
    make_move('R', c, board)
    print_board(board)
    score = evaluate_board(board)
    if score == '.':
      c = int(input('Y move: which column? '))
      make_move('Y', c, board)
      print_board(board)
      score = evaluate_board(board)
    
if score == 'R':
    print('R wins')
elif score == 'Y':
    print('Y wins')
elif score == 'T':
    print('tie game')