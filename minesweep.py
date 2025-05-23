import random

SIZE = 5  # 5x5 board
BOMBS = 5

# Create a board with bombs
def create_board(size, bombs):
    board = [['0' for _ in range(size)] for _ in range(size)]

    # Place bombs
    bomb_positions = set()
    while len(bomb_positions) < bombs:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        bomb_positions.add((x, y))

    for x, y in bomb_positions:
        board[x][y] = 'B'

    # Fill in numbers
    for x in range(size):
        for y in range(size):
            if board[x][y] == 'B':
                continue
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x+i < size and 0 <= y+j < size and board[x+i][y+j] == 'B':
                        count += 1
            board[x][y] = str(count)

    return board, bomb_positions

# Display function
def print_board(visible, revealed):
    print("   " + " ".join(str(i) for i in range(SIZE)))
    for i in range(SIZE):
        row = [visible[i][j] if revealed[i][j] else '#' for j in range(SIZE)]
        print(f"{i}  " + " ".join(row))

# Game loop
def play():
    board, bombs = create_board(SIZE, BOMBS)
    revealed = [[False]*SIZE for _ in range(SIZE)]

    while True:
        print_board(board, revealed)
        try:
            x = int(input("Enter row (0-4): "))
            y = int(input("Enter column (0-4): "))
        except ValueError:
            print("Invalid input.")
            continue

        if not (0 <= x < SIZE and 0 <= y < SIZE):
            print("Out of bounds!")
            continue

        if (x, y) in bombs:
            print("💥 BOOM! You hit a bomb.")
            print_board(board, [[True]*SIZE for _ in range(SIZE)])
            break
        else:
            revealed[x][y] = True
            # Optional: implement reveal of adjacent empty cells here
            if all(revealed[i][j] or board[i][j] == 'B' for i in range(SIZE) for j in range(SIZE)):
                print("🎉 You win!")
                print_board(board, [[True]*SIZE for _ in range(SIZE)])
                break

play()
