n = int(input("Enter Size of Board (N): "))  # Get N from user

# Function to Initialize board (2D List) with dimensions N row N with all values as 0
def init_board(n):
	board = [[0 for row in range(n)] for col in range(n)] 	
	return board	
	
# Function to print N row N board
def print_board(board,n):
	for i in range(n):
		for j in range(n):
			print(board[i][j],end=" ") 
		print (" ")	
	print ("")	
			
board = init_board(n)	#Initialize the board
print_board(board,n)	#Print Initial board config	

# Function will find and print all solutions for input board size (N)
def nQueens(board,n):
    count=0 # Keep count of Solutions
    row =[] # This list will store the row index of the queen to be placed on board. 
    col =[]	# This list will store the column index of the queen to be placed on board.
    # For example - If row[2]=2 and col[2]=3, it means the 3rd queen(index 2 refers to 3rd queen) is placed at position (2,3) on board 
    i=0
    j=0
    #Start from 0,0
    while i<n:
        while j<n:
            if(canPlace(i, j, row, col)):   #Check if new queen can be placed at current position(i,j) based on all previous queen positions (in row and col).
                board[i][j]=1    # If queen can be placed, change value to 1.
                row.insert(i,i)  # Insert this position indexes in row and col list.
                col.insert(i,j)
                if(i==n-1):      # If this is the last row of board, print solution
                    count=count+1
                    print ("Solution Number : %s" %(count))
                    print_board(board,n)
                    #When a solution is done, we will increment i and do j=0. Program will try to place queen at i=N and j=(0 to N-1) but always fail and backtrack until i=0.
                    #Next it will try to place queen at i=0 and j > last queen position at i=0 and thus find the next solution
                i+=1   # Increment i to place queen in next row.
                j=0   
            elif(j==n-1):   # If queen cant be placed and we reach the end of the row, algorithm will backtrack to previous queen position(in previous row) and try to place at previous queen's column +1
                i-=1   # i = previous row
                j=col[i]+1   # j will be column index of queen placed in previous row + 1. As placing queen in this position did not work, we will try placing in the next position.
                board[row[i]][col[i]]=0   #Previously placed queen will be removed
                del row[i]   # Delete its position index from row and col
                del col[i]
                if(j==n):   # If j goes beyond board size, it means we checked every column and cannot place our queen anywhere in the row.
                    if(i==0):   # If algorithm backtracks to the first row, and we cannot place queen anywhere, exit the program. We have no more solutions.
                        return 0
                    # Else, use same logic as above and backtrack to previous row.
                    i -= 1
                    j = col[i]+1
                    board[row[i]][col[i]]=0
                    del row[i]
                    del col[i]		
            else:      #Else increment j and try to place queen
                j += 1    
				
				
def canPlace(i,j,row,col):
	for k in range(i):
		if((j>col[k])and((row[k]-col[k])==(i-j))):#Check If current queen is in the diagonal of previously placed queens when column index of curent queen > column index of previous queens
			return False
		if(j==col[k]):    # Check if current queen to be placed is in the same column as previous queens
			return False
		if(j<col[k]):
			if((row[k]+col[k])==(i+j)):    #Check If current queen is in the diagonal of previously placed queens when column index of curent queen < column index of previous queens
				return False
		
	return True;
	
nQueens(board,n)
