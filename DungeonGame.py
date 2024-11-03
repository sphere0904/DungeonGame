import random
import time
import os

def create_dungeon(size):
    dungeon = [[" " for _ in range(size)] for _ in range(size)]
    dungeon[0][0] = "P"  # プレイヤーの初期位置
    dungeon[size - 1][size - 1] = "G"  # ゴール

    # 武器と財宝を配置
    def place_item(item):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if dungeon[x][y] == " ":
                dungeon[x][y] = item
                break

    for _ in range(2):
        place_item("W")  # 武器
        place_item("Z")  # 財宝

    # モンスターを配置
    for _ in range(5):
        place_item("M")  # モンスター

    return dungeon

def display_dungeon(dungeon):
    for row in dungeon:
        print(" ".join(row))
    print()

def execute_moves(dungeon, moves, size):
    player_pos = [0, 0]
    path = []
    weapons, treasures_collected = 0, 0

    for move in moves:
        if move == "W" and player_pos[0] > 0: player_pos[0] -= 1
        elif move == "S" and player_pos[0] < size - 1: player_pos[0] += 1
        elif move == "A" and player_pos[1] > 0: player_pos[1] -= 1
        elif move == "D" and player_pos[1] < size - 1: player_pos[1] += 1

        x, y = player_pos
        path.append((x, y))

        encounter = dungeon[x][y]
        if encounter == "W": weapons += 1
        elif encounter == "Z": treasures_collected += 1
        elif encounter == "M":
            if weapons > 0: weapons -= 1
            else: return "ゲームオーバー！モンスターにやられました。", path

        if player_pos == [size - 1, size - 1]:
            return f"おめでとう！財宝を {treasures_collected} 個集めました。", path

    return "残念ながらゴールに到達できませんでした。", path

def clear_screen():
    os.system('clear')

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r残り {i} 秒...", end="")
        time.sleep(1)

def dungeon_game():
    size = 5
    dungeon = create_dungeon(size)

    print("ダンジョン探索へようこそ！マップを記憶してください。\n")
    display_dungeon(dungeon)

    countdown(10)
    clear_screen()

    moves = input("移動コマンドを一列で入力してください（例: WASSD...）: ").upper()
    result, path = execute_moves(dungeon, moves, size)

    # 経路表示のためにダンジョンを更新
    for x, y in path:
        dungeon[x][y] = "X"

    display_dungeon(dungeon)
    print(result)

# ゲームを実行
dungeon_game()
