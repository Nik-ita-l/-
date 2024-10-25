import random

def create_board(size=8, num_chips=15):
    """
    Создаю игровое поле размером size x size с случайно размещенными фишками.

    :param size: Размер игрового поля (по умолчанию 8x8).
    :param num_chips: Количество фишек, которые нужно разместить на поле.
    :return: Двумерный список, представляющий игровое поле.
    """
    board = [[0 for _ in range(size)] for _ in range(size)]
    for _ in range(num_chips):
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        while board[x][y] == 1:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        board[x][y] = 1
    return board

def print_board(board):
    """
    Отображает текущее состояние игрового поля в консоли.

    :param board: Двумерный список, представляющий игровое поле.
    """
    print("  " + " ".join(str(i) for i in ['0','1','2','3','4','5','6','7']))
    for row_num, row in enumerate(board):
        print(str(row_num) + " " + " ".join('•' if cell == 1 else ' ' for cell in row))

def is_game_over(board):
    """
    Проверяет, закончилась ли игра (на поле нет фишек).

    :param board: Двумерный список, представляющий игровое поле.
    :return: True, если на поле нет фишек, иначе False.
    """
    return all(cell == 0 for row in board for cell in row)

def remove_chips(board, row=None, col=None):
    """
    Убирает все фишки с указанной строки или столбца.

    :param board: Двумерный список, представляющий игровое поле.
    :param row: Индекс строки, с которой убрать фишки (если указан).
    :param col: Индекс столбца, с которого убрать фишки (если указан).
    """
    if row is not None:
        for j in range(len(board[row])):
            board[row][j] = 0
    elif col is not None:
        for i in range(len(board)):
            board[i][col] = 0

def get_valid_input(board):
    """
    Получает и проверяет ввод пользователя на корректность.

    :param board: Двумерный список, представляющий игровое поле.
    :return: Кортеж с типом действия ('row' или 'col') и индексом (строки или столбца).
    """
    while True:
        try:
            action = input("Введите 'row' для удаления строки или 'col' для удаления столбца: ").strip().lower()
            if action not in ('row', 'col'):
                print("Ошибка ввода! Введите 'row' или 'col'.")
                continue

            index = int(input(f"Введите индекс {action}: ").strip())
            if action == 'row' and (0 <= index < len(board)) and any(board[index][j] == 1 for j in range(len(board))):
                return ('row', index)
            elif action == 'col' and (0 <= index < len(board)) and any(board[i][index] == 1 for i in range(len(board))):
                return ('col', index)
            else:
                print("Некорректный индекс или выбранная строка/столбец пуст. Попробуйте снова.")
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вы вводите целое число.")

def play_game():
    """
    Основная функция для запуска игры. Организует игровой процесс и взаимодействие с игроками.
    """
    board = create_board()
    current_player = 1

    print("Добро пожаловать в игру 'Супер ним'!")
    print_board(board)

    while not is_game_over(board):
        print(f"\nХодит игрок {current_player}.")
        action, index = get_valid_input(board)
        
        if action == 'row':
            remove_chips(board, row=index)
        elif action == 'col':
            remove_chips(board, col=index)
        
        print_board(board)
        
        if is_game_over(board):
            print(f"Игра окончена! Победил игрок {current_player}!")
            break
        
        # Меняем текущего игрока
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play_game()
