Wu Yuan, 72510535, Wuyyyyyyyyyy
Gong Ruifeng,72510824,greaft5
def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win
# test1???
def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            #
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        #i, j = map(int, input().split())
        #这里需要添加输入异常处理
        while True:
            try:
                parts = input("请输入两个整数，用空格分隔：").split()
                if len(parts) != 2:                       # ① 个数不对
                    raise ValueError
                if i <= 0 or j <= 0:
                    raise ValueError
                i, j = map(int, parts)                    # ② 非整数会抛 ValueError
                break                                     # ③ 全部通过，跳出循环
            except ValueError:
                print("输入格式错误！必须恰好是两个整数，用空格分隔。")
            except KeyboardInterrupt:                     # Ctrl-C 退出
                print("\n程序被用户中断。")
                exit()
        
        i -= 1
        j -= 1
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        if is_win(game):
            print("Win!")
            break  # Terminate the game
        if n == 8:  # All cells have been filled
            print("Tie!")
        #改进：正确的游戏结束逻辑
        winner = get_winner(board)
        if winner:
        print(f"玩家 {winner} 获胜！")
        break
        if is_board_full(board):
        print("平局！")
        break
        # Show the game board
        for row in game:
            print(" ".join(row))

if __name__ == "__main__":
    main()
