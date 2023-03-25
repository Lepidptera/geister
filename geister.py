#column 0 1 2 3 4 5 6 7
row0 = [0,0,0,0,0,0,0,0]
row1 = [0,0,0,0,0,0,0,0]
row2 = [0,0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0,0]
row4 = [0,0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0,0]
row6 = [0,0,0,0,0,0,0,0]
row7 = [0,0,0,0,0,0,0,0]

init_board = [row0,row1,row2,row3,row4,row5,row6,row7]

#column 0 1 2 3 4 5 6 7
row0 = [0,0,0,0,0,0,0,0]
row1 = [0,0,3,4,4,4,0,0]
row2 = [0,0,4,3,3,3,0,0]
row3 = [0,0,0,0,0,0,0,0]
row4 = [0,0,0,0,0,0,0,0]
row5 = [0,0,1,1,2,2,0,0]
row6 = [0,0,2,2,1,1,0,0]
row7 = [0,0,0,0,0,0,0,0]

board = [row0,row1,row2,row3,row4,row5,row6,row7]

#select_place = (5,2)

def place_select(board,select_place):

    #column 0 1 2 3 4 5 6 7
    row0 = [0,0,0,0,0,0,0,0]
    row1 = [0,0,0,0,0,0,0,0]
    row2 = [0,0,0,0,0,0,0,0]
    row3 = [0,0,0,0,0,0,0,0]
    row4 = [0,0,0,0,0,0,0,0]
    row5 = [0,0,0,0,0,0,0,0]
    row6 = [0,0,0,0,0,0,0,0]
    row7 = [0,0,0,0,0,0,0,0]

    range_board = [row0,row1,row2,row3,row4,row5,row6,row7]

    vectors = [(0,-1),(1,-1),(1,0),(-1,1),(0,1),(1,1),(-1,0),(-1,-1)]

    select_color = board[select_place[0]][select_place[1]]
    # 1 is my blue, 2 is my red, 3 is opponent's blue, 4 is opponent's red
    print("select_color",select_color)
    available_place = []
    beatable_place = []
    unbeatable_place = []
    for vector in vectors:
        row = select_place[0] + vector[0]
        column = select_place[1] + vector[1]
        if board[row][column] == 0:
            available_place.append((row,column))
        if board[row][column] == 3:
            beatable_place.append((row,column))
        if board[row][column] == 4:
            unbeatable_place.append((row,column))

    # range_board
    for range_place in available_place + beatable_place + unbeatable_place:
        range_board[range_place[0]][range_place[1]] = 1

    print(available_place,"available_place")
    print(beatable_place,"beatable_place")
    print(unbeatable_place,"unbeatable_place")

    print(row0)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)

    return range_board,select_color,available_place,beatable_place,unbeatable_place

#output_place = (4,3)

def place_output(board,select_place,output_place,
                available_place,beatable_place,unbeatable_place,select_color):

    handheld = []

    # escape
    if output_place[0] == 0:
        board[select_place[0]][select_place[1]] = 0
        print("congratulate")
    # available
    elif output_place in available_place:
        board[output_place[0]][output_place[1]] = select_color
        board[select_place[0]][select_place[1]] = 0
        print("available")
    # beatable
    elif output_place in beatable_place:
        board[output_place[0]][output_place[1]] = select_color
        board[select_place[0]][select_place[1]] = 0
        handheld.append(3)
        print("beated")
    # unbeatable
    elif output_place in unbeatable_place:
        board[output_place[0]][output_place[1]] = select_color
        board[select_place[0]][select_place[1]] = 0
        handheld.append(4)
        print("unbeated")
    # unavailable
    else:
        print("unavailable")

    print("#",row0)
    print("#",row1)
    print("#",row2)
    print("#",row3)
    print("#",row4)
    print("#",row5)
    print("#",row6)
    print("#",row7)

    return board