import random
from tkinter import*
from tkinter import messagebox as mbox

MAX_BUTTON = 9


def start():
    tk = Tk()
    tk.title('X_vs_0')
    tk.geometry('374x361')
    tk.resizable(False, False)
    tk.config(cursor="target", bg='black')

    menu = Menu(tk)
    game_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Game", menu=game_menu)
    game_menu.add_command(label="Easy level", command=lambda: start_easy(tk))
    game_menu.add_command(label="Hard level", command=lambda: start_hard(tk))
    tk.config(menu=menu)
    tk.mainloop()


def start_easy(tk):
    game_field = [None] * MAX_BUTTON
    game_remains = list(range(9))
    button = create_buttons(tk, lambda x: push_easy(x, game_field, game_remains, button))
    place_buttons(button)


def start_hard(tk):
    game_field = [None] * MAX_BUTTON
    game_remains = list(range(9))
    button = create_buttons(tk, lambda x: push_hard(x, game_field, game_remains, button))
    place_buttons(button)


def create_buttons(tk, command):
    return [Button(tk, width=5, height=2, font=('Arial', 28, 'bold'), bg='black',
            command=lambda x=i: command(x)) for i in range(MAX_BUTTON)]


def place_buttons(button):
    row = 0
    col = 0
    for i in range(MAX_BUTTON):
        button[i].grid(row=row, column=col)
        row += 1
        if row == 3:
            col += 1
            row = 0


def push_easy(num, game_field, game_remains, button):
    player_move(num, 'X', game_field, game_remains, button)
    cpu_move('X', '0', game_field, game_remains, button)


def push_hard(num, game_field, game_remains, button):
    player_move(num, 'X', game_field, game_remains, button)
    cpu_move_hard('X', '0', game_field, game_remains, button)


def player_move(num, symbol, game_field, game_remains, button):
    game_field[num] = symbol
    button[num].config(text=symbol, bg='yellow', fg='black', cursor='pirate', state='disabled')
    game_remains.remove(num)


def cpu_move(player_symbol, cpu_symbol, game_field, game_remains, button):
    if len(game_remains) > 0:
        cpu = random.choice(game_remains)
        game_field[cpu] = cpu_symbol
        button[cpu].config(text=cpu_symbol, bg='green', fg='black', cursor='pirate', state='disabled')
        game_remains.remove(cpu)
        check_result(player_symbol, cpu_symbol, game_field, game_remains, button)


def cpu_move_hard(player_symbol, cpu_symbol, game_field, game_remains, button):
    if len(game_remains) > 0:
        comp_move = best_move(game_field, game_remains)
        game_field[comp_move] = cpu_symbol
        button[comp_move].config(text=cpu_symbol, bg='green', fg='black', cursor='pirate', state='disabled')
        game_remains.remove(comp_move)
        check_result(player_symbol, cpu_symbol, game_field, game_remains, button)
    elif len(game_remains) < 1:
        message("Draw")


def check_result(player_symbol, cpu_symbol, game_field, game_remains, button):
    if win(player_symbol, game_field):
        message("You WIN")
        for k in game_remains:
            button[k].config(fg='black', cursor='pirate', state='disabled')
    elif win(cpu_symbol, game_field):
        message("You LOSE")
        for k in game_remains:
            button[k].config(fg='black', cursor='pirate', state='disabled')


def win(n, game_field):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for condition in win_conditions:
        if game_field[condition[0]] == n and game_field[condition[1]] == n and game_field[condition[2]] == n:
            return True
    return False


def message(choice):
    ask_question = mbox.askquestion(choice, "Repeat?")
    if ask_question == 'no':
        exit()
    else:
        mbox.showinfo("Choose level")


def best_move(game_field, game_remains):
    best_value = float('-inf')
    best_move = None

    for i in range(MAX_BUTTON):
        if game_field[i] is None:
            game_field[i] = '0'
            game_remains.remove(i)
            move_value = minimax(game_field, 0, False, game_remains)
            game_field[i] = None
            game_remains.append(i)
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move


def minimax(board, depth, maximizingPlayer, game_remains):
    if win('X', board):
        return -1
    if win('0', board):
        return 1
    if len(game_remains) == 0:
        return 0

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(MAX_BUTTON):
            if board[i] is None:
                board[i] = '0'
                game_remains.remove(i)
                eval = minimax(board, depth + 1, False, game_remains)
                board[i] = None
                game_remains.append(i)
                maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for i in range(MAX_BUTTON):
            if board[i] is None:
                board[i] = 'X'
                game_remains.remove(i)
                eval = minimax(board, depth + 1, True, game_remains)
                board[i] = None
                game_remains.append(i)
                minEval = min(minEval, eval)
        return minEval


start()
