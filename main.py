from flask import Flask, render_template, request, redirect, url_for
import requests
import geister
import time


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


#! 単一のurlが一人のみに適用されるわけではないから意味がない気がする、、、
#! 根本的にコードを変える必要がありそう
@app.route('/match/<url>',methods=['GET','POST'])
def match(url):
    global handheld_blue
    global selecting
    global board
    global range_board
    global handheld_red
    global select_place
    global select_color
    global available_place
    global beatable_place
    global unbeatable_place
    global wait
    # WAIT
    try:
        if wait and request.method == 'GET':
            time.sleep(2)
            return render_template('match.html',board=board_str,range_board=range_board_str,
                handheld_blue=len(handheld_blue),handheld_red=len(handheld_red))
        elif wait and request.method == 'POST':
            time.sleep(2)
            if 'opponent' in request.form['place']:
                wait = False
                raise ValueError
            return render_template('match.html',board=board_str,range_board=range_board_str,
                handheld_blue=len(handheld_blue),handheld_red=len(handheld_red),wait=wait,url=url)
    except:
        print("First GET or Error")
    # GET request
    if request.method == 'GET':
        selecting = False
        board = geister.board
        range_board = geister.init_board
        # in order not to update the list
        try:
            handheld_blue = handheld_blue
        except:
            handheld_blue = []
        try:
            handheld_red = handheld_red
        except:
            handheld_red= []
        wait = False
    # POST request (my turn)
    elif request.method == 'POST' and not 'opponent' in request.form['place']:
        # selecting
        if not selecting:
            print("selecting place")
            x_place = int(request.form['place'].split('-')[0])
            y_place = int(request.form['place'].split('-')[1])
            select_place = (x_place,y_place)
            print("select_place",select_place)
            range_board,select_color,available_place,beatable_place,unbeatable_place = geister.place_select(board,select_place)
            selecting = True
        # placing
        elif selecting:
            print("deciding place")
            x_place = int(request.form['place'].split('-')[0])
            y_place = int(request.form['place'].split('-')[1])
            output_place = (x_place,y_place)
            print("output_place",output_place)
            board,blue,red,place = geister.place_output(board,select_place,output_place,
                available_place,beatable_place,unbeatable_place,select_color)
            handheld_blue += blue
            handheld_red += red
            range_board = geister.init_board
            selecting = False
            # post
            if place:
                my_select_place = str(7-int(select_place[0])) + str(select_place[1])
                my_output_place = str(7-int(output_place[0])) + str(output_place[1])
                my_select_color = select_color + 2
                data = {'place':'opponent','select_place':my_select_place,
                    'output_place':my_output_place,'select_color':my_select_color}
                requests.post("http://127.0.0.1:2000", data=data)
                print(my_select_place,'→',my_output_place)
                wait = True
    # POST request (opponent's turn)
    elif request.method == 'POST' and 'opponent' in request.form['place']:
        opponent_select_place = request.form['select_place']
        opponent_output_place = request.form['output_place']
        opponent_select_color = int(request.form['select_color'])
        board = geister.opponent(board,opponent_select_place,
            opponent_output_place,opponent_select_color)
    # turn int into str
    board_str = [list(map(str, row)) for row in board]
    range_board_str = [list(map(str, row)) for row in range_board]
    return render_template('match.html',board=board_str,range_board=range_board_str,
        handheld_blue=len(handheld_blue),handheld_red=len(handheld_red),wait=wait,url=url)



if __name__ == '__main__':
    app.run(port=3000, threaded=True)