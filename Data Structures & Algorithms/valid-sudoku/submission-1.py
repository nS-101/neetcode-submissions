class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Creates a list of 9 independent, empty sets
        rowSets = [set() for _ in range(9)]

        # Creates a list of 9 independent, empty sets
        colSets = [set() for _ in range(9)]

        # Creates a list of 9 independent, empty sets
        boxSets = [set() for _ in range(9)]

       

        for i in range(0, len(board)): #outer loop(iterating through rows)
            for j in range(0, len(board[0])): #inner loop(iterating through columns)
                if board[i][j] == ".":
                    continue

                boxNumber = i//3 * 3 + j//3
                if board[i][j] in boxSets[boxNumber]:
                    return False
                boxSets[boxNumber].add(board[i][j])

                if board[i][j] in rowSets[i]:
                    return False
                rowSets[i].add(board[i][j])

                if board[i][j] in colSets[j]:
                    return False
                colSets[j].add(board[i][j])

        return True




