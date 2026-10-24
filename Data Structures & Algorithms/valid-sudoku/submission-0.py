class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Creates a list of 9 independent, empty sets
        rowSets = [set() for _ in range(9)]

        # Creates a list of 9 independent, empty sets
        colSets = [set() for _ in range(9)]

        # Creates a list of 9 independent, empty sets
        boxSets = [set() for _ in range(9)]

        #box left

        for i in range(0, len(board)): #outer loop(iterating through rows)
            for j in range(0, len(board[0])): #inner loop(iterating through columns)
                if board[i][j] == ".":
                    continue
                boxNumber = i//3 * 3 + j//3
                lenBox = len(boxSets[boxNumber])
                boxSets[boxNumber].add(board[i][j])
                if lenBox == len(boxSets[boxNumber]):
                    return False
                lenRow = len(rowSets[i])
                lenCol = len(colSets[j])
                rowSets[i].add(board[i][j])
                colSets[j].add(board[i][j])
                if (lenRow == len(rowSets[i])) or (lenCol == len(colSets[j])):
                    return False #length didnt change so the value was already there
        return True




