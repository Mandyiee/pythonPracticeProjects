import random
def checkResult(board):
  global winner
  if board['top-L'] == board['top-M'] and board['top-L'] == board['top-R'] and board['top-L'] != ' ':
    winner = board['top-L'] 
    return True
  elif board['mid-L'] == board['mid-M'] and board['mid-L'] == board['mid-R'] and board['mid-L'] != ' ':
    winner = board['mid-L']
    return True
  elif board['low-L'] == board['low-M'] and board['low-L'] == board['low-R'] and board['low-L'] != ' ':
    winner = board['low-L']
    return True
  elif board['top-L'] == board['mid-L'] and board['top-L'] == board['low-L'] and board['top-L'] != ' ':
    winner = board['top-L']
    return True
  elif board['top-M'] == board['mid-M'] and board['top-M'] == board['low-M'] and board['top-M'] != ' ':
    winner = board['top-M']
    return True
  elif board['top-R'] == board['mid-R'] and board['top-R'] == board['low-R'] and board['top-R'] != ' ':
    winner = board['top-R']
    return True
  elif board['top-R'] == board['mid-M'] and board['top-R'] == board['low-L'] and board['top-R'] != ' ':
    winner = board['top-R']
    return True
  elif board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R'] and board['top-L'] != ' ':
    winner = board['top-L']
    return True
  else:
    return False
    

theBoardO = {
'top-L':'1','top-M':'2','top-R':'3',
'mid-L':'4','mid-M':'5','mid-R':'6',
'low-L':'7','low-M':'8','low-R':'9'
}


theBoard = {
'top-L':' ','top-M':' ','top-R':' ',
'mid-L':' ','mid-M':' ','mid-R':' ',
'low-L':' ','low-M':' ','low-R':' '
}


theBoardMoves = {
'1':'top-L','2':'top-M','3':'top-R',
'4':'mid-L','5':'mid-M','6':'mid-R',
'7':'low-L','8':'low-M','9':'low-R'
}

def printBoard(board):
  print(board['top-L'] + '  |  ' + board['top-M'] +
 '  |  ' + board['top-R'])
  print('---+-----+---')
  print(board['mid-L'] + '  |  ' + board['mid-M']
 + '  |  ' + board['mid-R'])
  print('---+-----+---')
  print(board['low-L'] + '  |  ' + board['low-M'] +
 '  |  ' + board['low-R'])

while True:
 print('X or O?')
 player = input()
 if player == 'X' or player == 'O':
  print('you have chosen player ' + player)
  print('\n')
  if player == 'X':
   comp = "O"
  else:
   comp = "X"
  break
 else:
  print('invalid selection')
  print('\n')
  continue

count = 0
selection = ['1','2','3','4','5','6','7','8','9']

printBoard(theBoardO)
print('\n')
print('Use the numbers as directions. That is,to go the top middle column, press 3')
print('\n')

for i in range(9):
  
  if comp == 'X':
    count+= 1
    while True:
      print('\n')
      print('Turn for player ' + player +
        '.Move to which space')
      print('\n')
      playerChoice = input()
      if playerChoice in selection:
        playerMove = theBoardMoves[playerChoice]
        theBoard[playerMove] = player
        selection.remove(playerChoice)
        break
      else:
        print('Already been selected')
        print('\n')
        continue
    if count >= 3:
      if checkResult(theBoard):
        if winner == comp:
          print('computer wins')
          print('\n')
          break
        else:
          print('player ' + winner + ' wins')
          print('\n')
          break
    if count >= 5:
      break
    choice = str(random.choice(selection))
    move = theBoardMoves[choice]
    theBoard[move] = comp
    selection.remove(choice)
    printBoard(theBoard)
    if count >= 3:
      if checkResult(theBoard):
        if winner == comp:
          print('computer wins')
          print('\n')
          break
        else:
          print('player ' + winner + ' wins')
          print('\n')
          break
  else:
    count += 1
    choice = str(random.choice(selection))
    move = theBoardMoves[choice]
    theBoard[move] = comp
    selection.remove(choice)
    printBoard(theBoard)
    if count >= 3:
      if checkResult(theBoard):
        if winner == comp:
          print('computer wins')
          print('\n')
          break
        else:
          print('player ' + winner + ' wins')
          print('\n')
          break
    if count >= 5:
      break
    while True:
      print('\n')
      print('Turn for player ' + player +
        '.Move to which space')
      playerChoice = input()
      if playerChoice in selection:
        playerMove = theBoardMoves[playerChoice]
        theBoard[playerMove] = player
        selection.remove(playerChoice)
        break
      else:
        print('Already been selected')
        print('\n')
        continue
    if count >= 3:
      if checkResult(theBoard):
        if winner == comp:
          print('computer wins')
          print('\n')
          break
        else:
          print('player ' + winner + ' wins')
          print('\n')
          break
  
printBoard(theBoard)
