#suduko using backtracing



#in matrix 0 will be treated as empty cell
matrix = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]


#for printing sudoku
def print_sudoku():
    for i in matrix:
        print(i)


#for checking if their is any unassigned cell and if their is then this function will automatically change values of row and column        
def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0,9):
        for j in range(0,9):
            if matrix[i][j] == 0:
                 row = i
                 col = j
                 num_unassign = 1
                 a = [row, col, num_unassign]
                 return a
        
           
        
    a = [-1, -1, num_unassign]
    return a

def is_safe(n, r, c):
    for i in range(0,9):
        if matrix[r][i] == n:
            return False
    for i in range(0,9):
        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j] == n:
                return False
    return True


def solve_sudoku():
    row = 0
    col = 0
    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    for i in range(1,10):
        if is_safe(i, row, col):
            matrix[row][col] = i
            if solve_sudoku():
                return True
            matrix[row][col] = 0
    return False

if solve_sudoku():
    print_sudoku()
else:
    print("No problem")        