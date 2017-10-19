__author__ = 'QSG'
import time
class queen:
    def __init__(self,row,column,size):
        self.size=size
        self.row=row
        self.column=column
        self.domain=range(size)
        self.conflict_pos=[]

def solve (size=9):
    free_queens=[queen(None,i,size) for i in range(size)]
    set_queens=[]

    i=0

    while len(free_queens)>0:     #if unlabelled is {},then return labelled
        print '==loop start:',i
        selectedQueen=select_queen(free_queens,set_queens)    #pick first queen from unlabelled
        print '--current queen:', (selectedQueen.row,selectedQueen.column)


        #select a row from the queen's domain,if the queen's domain is empty,return false, or return true, and assign the
        #first element to selected queen's row.
        success_set_selected_queen_row=select_row(selectedQueen)
        print 'select a queen:', (selectedQueen.row,selectedQueen.column)

        if not success_set_selected_queen_row:
            print '-->start back track',len(free_queens),len(set_queens) #****add jumping method here, need to know how much to jump back
            reset_queen(free_queens,set_queens,2)
            print '-->after back track',len(free_queens),len(set_queens)
            print 'domain of queen is empty'

        #If current board is dead end, back track.
        print 'seletcted queens',[(q.row,q.column) for q in set_queens ]
        if len(set_queens)>0:
            is_dead_end=dead_end(set_queens)
            if is_dead_end:
                reset_queen(free_queens,set_queens,1)
                continue

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

def dead_end(set_queens):

    all_conflict_pos=[]
    for q in set_queens:
        # print (q.row,q.column),' : ',q.conflict_pos
        all_conflict_pos += q.conflict_pos

    #Eliminate the repeated items in all_conflict_pos
    all_conflict_pos=list(set(all_conflict_pos))
    # print 'set queens in dead end',set_queens
    size=set_queens[len(set_queens)-1].size
    cur_col=set_queens[-1].column
    for col in range(cur_col+1,size):
        conflict_num=0
        for pos in all_conflict_pos:
            if col==pos[1]:
                conflict_num+=1
        if conflict_num==size:
            # print '===dead end==='
            # for q in set_queens:
            #     print (q.row,q.column),' : ',q.conflict_pos
            # print "found dead end, at column:",col,'size:',size,'cur col:',cur_col,'conflict is:', all_conflict_pos
            return True
    return False

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

    #set the queen's conflict postions
    r=queen.row
    c=queen.column
    conf_row=[(r,col)for col in range(c+1,queen.size) ]
    conf_slash=[(row,col)for row in range(queen.size) for col in range(c+1,queen.size) if (row+col)==(r+c) or (col-row)==(c-r) ]
    queen.conflict_pos=conf_row+conf_slash
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

