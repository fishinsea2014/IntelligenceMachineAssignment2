class queen:
    def __init__ (self, row, column, size):
        self.size = size
        self.row = row
        self.column = column
        self.domain = range(size)

def solve(size = 8):
    free_queens = [queen(None, i, size) for i in range(size)]
    set_queens = []
    
    while len(free_queens) > 0:
        if not select_row(select_queen(free_queens, set_queens)):
            reset_queen(free_queens, set_queens, 2)
        if not safe_board(set_queens):
            reset_queen(free_queens, set_queens, 1)
                
    return set_queens  

def select_queen(free_queens, set_queens):
    set_queens.append(free_queens.pop(0))
    return set_queens[len(set_queens) - 1]

def select_row(queen):
    if len(queen.domain) == 0:
        queen.row = None
        queen.domain = range(queen.size)
        return False
    queen.row = queen.domain.pop(0)
    return True

def reset_queen(free_queens, set_queens, num_of_queens):
    for i in range(num_of_queens):
        free_queens.insert(0, set_queens.pop())

def safe_board(queens):
    return [safe_queens(queens[len(queens) - 1], queens[i]) for i in range(len(queens) - 1)].count(False) == 0

def safe_queens(queen1, queen2):
    return (queen1.row != queen2.row and
            queen1.row + queen1.column != queen2.row + queen2.column and
            queen1.row + queen2.column != queen2.row + queen1.column)

n=15

board = solve(size = n)


# result_queen_pos=[]
for i in range(len(board)):
    print 'Row:', board[i].row, '  Column', board[i].column, '  Domain:', board[i].domain
    # result_queen_pos.append([])
#Print board
# for i in range(n):

# display_board_=[[0 for _ in range(n)] for _ in range (n)]
