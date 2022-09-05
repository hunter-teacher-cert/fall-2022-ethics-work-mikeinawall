# gol.py
# Michael Randazzo
# CSCI 77800 Fall 2022
# collaborators: None
# consulted: ThinkJava

dead = "-"
alive = "X"
board = []

#Function to create a new board
def createNewBoard( rows, cols):
  board = [dead] * rows
  for i in range(rows):
    board[i] = [dead] * cols
  return board
  
  
#Function to print a board
def printBoard(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      print( board[i][j] , end = " ")
    print()

#function to set a cell
def setCell(board, r, c, val):
  board[r][c] = val

#Function to count neighbors
def countNeighbors(board, r, c):
  live_neighbors = 0
  def get(r, c):
      return 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c]
      
  if get(r, c-1) == alive:
      live_neighbors += 1
  if get(r-1, c) == alive:
      live_neighbors += 1
  if get(r-1, c+1) == alive:
      live_neighbors += 1
  if get(r, c-1) == alive:
      live_neighbors += 1
  if get(r, c+1) == alive:
      live_neighbors += 1
  if get(r+1, c-1) == alive:
      live_neighbors += 1
  if get(r+1, c) == alive:
      live_neighbors += 1
  if get(r+1, c+1) == alive:
    live_neighbors += 1

  return live_neighbors
    

#Function that determines state of cell in next gen based on the number from countNeighbors
def getNextGenCell(board, r, c):
  numN = countNeighbors(board, r, c)
  if board[r][c] is alive:
    if numN == 2 or numN == 3:
      return alive
    else:
      return dead
  else:
    if numN == 3:
      return alive
    else:
      return dead
    
#Function that generates the full next gen board
def generateNextBoard(board):
  newBoard = createNewBoard(len(board),len(board[0]))
  for i in range(len(board)):
    for j in range(len(board[0])):
      newBoard[i][j] = getNextGenCell(board, i, j)
  return newBoard
      


#Main
Board = createNewBoard(4,6)
#print(Board)
printBoard(Board)

print(" ")

setCell(Board, 1,2, alive)
setCell(Board, 1,1, alive)
setCell(Board, 2,2, alive)
setCell(Board, 2, 4, alive)
printBoard(Board)

#print(countNeighbors(Board, 1,1))
#print(countNeighbors(Board, 2, 5))
print("????????????")
NewBoard = generateNextBoard(Board)
printBoard(NewBoard)
