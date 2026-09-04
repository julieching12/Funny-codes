def is_valid_sudoku(): # method: what scenarios return "No", then other else returns "Yes"
    # first, build the board and input all testing data into it
    board = []   # 9 rows input will become 9 lists inside a whole list
    for i in range(9):
        row = input().strip()  # input in a form of 9 lines, then each i get one line
        if len(row) != 9 or not row.isdigit(): # each row must contain 9 digits, and each must be digit
            print("No")
            return

        board.append([int(ch) for ch in row])

    # second, create a valid set which is standard for compare
    valid_set = set(range(1,10))
    print(f"check standard: {valid_set}")   #{1, 2, 3, 4, 5, 6, 7, 8, 9}

    # third, check row
    for r in range(9):
        if set(board[r]) != valid_set:
            print("No")
            return

    # fourth, check column
    for c in range(9):
        col = {board[r][c] for r in range(9)} # {} created a set from a list "object" and sort it
        if col != valid_set:
            print("No")
            return

    # fifth, check 3x3 sub-squares * these are fixed, only 9 sub-squares; no rotate/movable blocks
    for br in range(0, 9, 3):  # br only takes three values: 0, 3, 6
        for bc in range(0, 9, 3):  # bc only takes three values: 0, 3, 6
            sub_square = set()
            sub_square_stg = ''  #check how it looks
            for r in range(br, br + 3): # r: range(0, 3), range(3, 6), range(6, 9)
                for c in range(bc, bc + 3): # c: range(0, 3), range(3, 6), range(6, 9)
                    sub_square_stg += str(board[r][c])
                    sub_square.add(board[r][c])  # add() add value to set, and becomes a sorted set
            if sub_square != valid_set:
                print("No")
                return

    print("Yes")

is_valid_sudoku()

# #1st sample input data:
# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
# #2nd sample input data:
# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671
