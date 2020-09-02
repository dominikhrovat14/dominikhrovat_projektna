import bottle
from bottle import route, static_file, template, post, get, request, redirect, error
import os
import Gamelogic as GL

my_dir = os.getcwd()

@route('/static/<filepath:path>')
def serve_static_content(filepath):
    pot = os.path.join(my_dir, 'static')
    return static_file(filepath, root=pot)


@get('/')
def zacetna_stran():
    return template('zacetna_stran.html',
                    place_1=str(GL.board[0]),
                    place_2=str(GL.board[1]),
                    place_3=str(GL.board[2]),
                    place_4=str(GL.board[3]),
                    place_5=str(GL.board[4]),
                    place_6=str(GL.board[5]),
                    place_7=str(GL.board[6]),
                    place_8=str(GL.board[7]),
                    place_9=str(GL.board[8]),
                    place_10="")

@post('/Turn')
def Turn():
    def winner(player):
        set_winner = GL.game_loop(player)
        if GL.winner() == "O":
            return None
            
            
    winner(int(float(request.forms.get('myTurn'))))

    winner(None)

    redirect('/', code=None)


@get('/Reset')
def reset_values():
    GL.board = [' ' for x in range(9)]
    GL.turn = 0
    GL.congrats = ""
    GL.moznosti = [x for x in range(9)]
    GL.moje_poteze = []
    GL.variable = 2
    return template('zacetna_stran.html',
                    place_1=str(GL.board[0]),
                    place_2=str(GL.board[1]),
                    place_3=str(GL.board[2]),
                    place_4=str(GL.board[3]),
                    place_5=str(GL.board[4]),
                    place_6=str(GL.board[5]),
                    place_7=str(GL.board[6]),
                    place_8=str(GL.board[7]),
                    place_9=str(GL.board[8]),
                    place_10="")

@get('/Konec')
def konec():
    if GL.check_win(GL.board) == "X":
        return template('zacetna_stran',
            place_1=str(GL.board[0]),
            place_2=str(GL.board[1]),
            place_3=str(GL.board[2]),
            place_4=str(GL.board[3]),
            place_5=str(GL.board[4]),
            place_6=str(GL.board[5]),
            place_7=str(GL.board[6]),
            place_8=str(GL.board[7]),
            place_9=str(GL.board[8]),
            place_10="Bravo! Zmagovalec si!")
    elif GL.check_win(GL.board) == "O":
        return template('zacetna_stran',
            place_1=str(GL.board[0]),
            place_2=str(GL.board[1]),
            place_3=str(GL.board[2]),
            place_4=str(GL.board[3]),
            place_5=str(GL.board[4]),
            place_6=str(GL.board[5]),
            place_7=str(GL.board[6]),
            place_8=str(GL.board[7]),
            place_9=str(GL.board[8]),
            place_10="Smola. Poskusi ponovno?")
    elif GL.check_win(GL.board) == "remi":
        return template('zacetna_stran',
            place_1=str(GL.board[0]),
            place_2=str(GL.board[1]),
            place_3=str(GL.board[2]),
            place_4=str(GL.board[3]),
            place_5=str(GL.board[4]),
            place_6=str(GL.board[5]),
            place_7=str(GL.board[6]),
            place_8=str(GL.board[7]),
            place_9=str(GL.board[8]),
            place_10="Izenačeno. Poskusi ponovno!")


bottle.run()
