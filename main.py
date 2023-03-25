from flask import Flask, render_template, request, redirect, url_for
import geister

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    # GET request
    if request.method == 'GET':
        global selecting
        selecting = False
        global board
        board = geister.board
        global range_board
        range_board = geister.init_board
    # POST request
    if request.method == 'POST':
        # selecting
        if not selecting:
            print("selecting place")
            x_place = int(request.form['place'].split('-')[0])
            y_place = int(request.form['place'].split('-')[1])
            global select_place
            select_place = (x_place,y_place)
            print("select_place",select_place)
            global select_color
            global available_place
            global beatable_place
            global unbeatable_place
            range_board,select_color,available_place,beatable_place,unbeatable_place = geister.place_select(board,select_place)
            selecting = True
        # placing
        elif selecting:
            print("deciding place")
            x_place = int(request.form['place'].split('-')[0])
            y_place = int(request.form['place'].split('-')[1])
            output_place = (x_place,y_place)
            print("output_place",output_place)
            board = geister.place_output(board,select_place,output_place,available_place,beatable_place,unbeatable_place,select_color)
            range_board = geister.init_board
            selecting = False
    # turn int into str
    board_str = [list(map(str, row)) for row in board]
    range_board_str = [list(map(str, row)) for row in range_board]
    return render_template('index.html',board=board_str,range_board=range_board_str)



if __name__ == '__main__':
    app.run(port=5000, threaded=True)