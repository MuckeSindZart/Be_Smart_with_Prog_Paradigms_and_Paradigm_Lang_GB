# Функция для создания пустой игровой доски
def create_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

# Функция для отображения текущей доски
def display_board(board):
    
    header_line = "┌───┬───┬───┐"
    center_line = "├───┼───┼───┤"
    footer_line = "└───┴───┴───┘"

    print(header_line)
    for i, row in enumerate(board):
        print("│ " + " │ ".join(row) + " │")
        if i < 2:
            print(center_line)
    print(footer_line)

# Функция для хода игрока
def make_move(board, move, player):
    if move < 1 or move > 9:
        print("Недопустимый ход. Введите число от 1 до 9.")
        return False

    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Эта клетка уже занята. Выберите другую.")
        return False

# Функция для проверки победы
def check_win(board, player):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or \
           board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Основная функция игры
def play_game():
    board = create_board()
    current_player = "X"
    move = 1

    while move <= 9:
        display_board(board)
        print(f"Ход игрока {current_player}")
        input_move = input("Выберите клетку (1-9): ")

        if make_move(board, int(input_move), current_player):
            if check_win(board, current_player):
                display_board(board)
                print(f"Игрок {current_player} победил!")
                break

            move += 1
            current_player = "O" if current_player == "X" else "X"
    else:
        display_board(board)
        print("Ничья!")

# Запуск игры
play_game()

# ~python HMWRK.py 


# Императивное программирование применяется в функциях make_move() и play_game(),
# где выполняются изменения состояния игровой доски и управление ходами игроков,
# что естественно для процедурного программирования.

# Функциональное программирование используется в функции check_win(),
# которая предоставляет результат проверки без изменения состояния игры,
# что характерно для функциональной парадигмы.

# Использование разных парадигм в разных частях кода помогает сделать
# код более чистым и поддерживаемым, и выбор конкретной парадигмы зависит
# от целей и требований каждой функции.
