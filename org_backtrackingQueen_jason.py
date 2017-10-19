__author__ = 'QSG'
import time
class queen:
    def __init__(self,row,column,size):
        self.size=size
        self.row=row
        self.column=column
        self.domain=range(size)

def solve (size=9):
    free_queens=[queen(None,i,size) for i in range(size)]
    set_queens=[]

    i=0

    while len(free_queens)>0:     #if unlabelled is {},then return labelled
        print '==loop start:',i
        selectedQueen=select_queen(free_queens,set_queens)    #pick first queen from unlabelled
        print '--current queen:', (selectedQueen.row,selectedQueen.column)
        print 'select a queen:', (selectedQueen.row,selectedQueen.column)

        #select a row from the queen's domain,if the queen's domain is empty,return false, or return true, and assign the
        #first element to selected queen's row.
        success_set_selected_queen_row=select_row(selectedQueen)
        if not success_set_selected_queen_row:
            print '-->start back track',len(free_queens),len(set_queens) #****add jumping method here, need to know how much to jump back
            reset_queen(free_queens,set_queens,2)
            print '-->after back track',len(free_queens),len(set_queens)
            print 'domain of queen is empty'

        #check whether the current queens is safe
        isSafe=safe_board(set_queens)
        if not isSafe:
            reset_queen(free_queens,set_queens,1)
            print 'this queen has conflict'
        i=i+1
        print 'left free queens: ', len(free_queens),'-->',[((x.row,x.column),x.domain) for x in free_queens]
        print 'set queens',len(set_queens),'-->',[((x.row,x.column),x.domain) for x in set_queens]
        print '==============='

    return set_queens

def select_queen(free_queens,set_queens):
    set_queens.append(free_queens.pop(0)) #Take a free queen from the free queen list, and append it to the list of queens being set.
    return set_queens[len(set_queens)-1] # Return the select queen for this round.

#Queen's domain has the row number of a queen, take a row number from the domain
def select_row(queen):
    # If queen's domain is empty,then set the queen's row number to None
    # and  reset the queen's domain to original list.
    # Then return false
    if len(queen.domain) == 0:
        queen.row=None
        queen.domain=range(queen.size)
        return False

    #If queen's domain is not empty, then take the first number and assign it to a queen as its row number.
    queen.row=queen.domain.pop(0)
    return True

#Take one or two queens from set_queens list and insert them into the free_queens list.
#e.g. let number=2,free_queens=[], set_queens=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     when reset_queen(free_queens,set_queens,2)
#     then free_queens=[8, 9]
#          set_queens=[0, 1, 2, 3, 4, 5, 6, 7]
def reset_queen(free_queens,set_queens,number_of_queens):
    for i in range (number_of_queens):
        free_queens.insert(0,set_queens.pop())


#Estimate whether two queens are conflict
def safe_queens(queen1,queen2):
    return(queen1.row != queen2.row and
            queen1.row+queen1.column != queen2.row+queen2.column and
            queen1.row+queen2.column != queen2.row+queen1.column)


def safe_board(queens):
    #queens[len(queens)-1] is the last queens,compare with other queens
    return [safe_queens(queens[len(queens)-1],queens[i]) for i in range(len(queens)-1)].count(False)==0

n=15
time_start=time.time()
board=solve(size=n)
time_end=time.time()
runTime=time_end-time_start
print 'Run time: ',runTime, ' seconds'
# print board

for i in range(len(board)):
    print 'Row: ',board[i].row,'column',board[i].column,'Domain: ',board[i].domain

