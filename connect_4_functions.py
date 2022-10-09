def make_board(rows, columns):
    board = []
    for i in range(rows):
      board.append([])
      for j in range(columns):
        board[i].append('.')
    return board

def print_board(board):
  for i in board:
    final = ''
    for j in i:
      final += j
    print(final)

def make_move(token_color, column, board):
    row = len(board)
    col = len(board[0]) - 1
    if (column < 0 or column > col) or board[0][column] != '.':
      raise Exception('illegal move')
    else:
      for i in range(len(board)-1,-1,-1):
        if board[i][column] == '.':
          board[i][column] = token_color
          break
    return board

def evaluate_board(board):
  count_r = 0
  count_y = 0
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 'R':
        count_r += 1
      else:
        count_r = 0
      if board[i][j] == 'Y':
        count_y += 1
      else:
        count_y = 0
      if count_r == 4:
        return 'R'
      elif count_y == 4:
        return "Y"
  count_r = 0
  count_y = 0
  for i in range(len(board[0])):
    for j in range(len(board)):
      if board[j][i] == 'R':
         count_r += 1
      else:
        count_r = 0
      if board[j][i] == 'Y':
        count_y += 1
      else:
        count_y = 0
      if count_r == 4:
        return 'R'
      elif count_y == 4:
        return 'Y'
    
    for k in range(len(board)):
      for l in range(len(board[0])):
        if board[k][l] == "R":
          if k + 3 < len(board[0]) and l + 3 < len(board):
            if board[k+1][l+1] == 'R' and board[k+2][l+2] == 'R' and board[k+3][l+3] == 'R':
              return "R"
        if board[k][l] == "Y":
          if k + 3 < len(board[0]) and l + 3 < len(board):
            if board[k+1][l+1] == 'Y' and board[k+2][l+2] == 'Y' and board[k+3][l+3] == 'Y':
              return "Y"

    for k in range(len(board)-1,-1,-1):
      for l in range(len(board[0])-1,-1,-1):
        if board[k][l] == "R":
          if k + 3 < len(board):
            if board[k+1][l-1] == 'R' and board[k+2][l-2] == 'R' and board[k+3][l-3] == 'R':
              return "R"
        if board[k][l] == "Y":
          if k + 3 < len(board):
            if board[k+1][l-1] == 'Y' and board[k+2][l-2] == 'Y' and board[k+3][l-3] == 'Y':
              return "Y" 
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == ".":
          return '.'
    return 'T'

