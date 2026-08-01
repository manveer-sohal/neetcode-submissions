from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        #Instead of checking every cell in every row and then every cell in every coloum then every cell in every square
        #do one pass, and use a set for each row, and each col, and each square, to see if a dupe number appears

        #So row 0 set()
        # row 1 set()
        # row 2 set()
        # row 3 set()
        #ect...
        # col 0 set()
        # col 0 set()

        #To get each sqaure
        # coloum = col % 3
        #|0 |1 | 2|

        dupe = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board[r][c]

                if cell != ".":
                    if cell in dupe[("row",r)] or cell in dupe[("col",c)] or cell in dupe[(r//3,c//3)]:
                   
                       
                        return False
                    
                    dupe[("row",r)].add(cell) 
                    dupe[("col",c)].add(cell) 
                    dupe[(r//3,c//3)].add(cell)
                
               
        return True

                



        