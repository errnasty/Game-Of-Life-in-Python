# import
import random
import time
# width = 5
# height = 5

# DeadState


def dead_state(width, height):
    return [[0 for x in range(width)] for y in range(height)]

# RandomState


def random_state(width, height):
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            random_number = random.random()
            # changable threshold
            if random_number >= 0.5:
                state = 1
            else:
                state = 0
            row.append(state)
        result.append(row)
    return result

    # return [[random.randint(0,1) for x in range(width)] for y in range(height)]


def render(board_state):
    result = []
    for row in board_state:
        new_row = []
        for cell in row:
            if cell == 1:
                state = "X"
            elif cell == 0:
                state = " "
            elif cell == 2:
                state = "\033[91mZ\033[0m"
            new_row.append(state)
        result.append("|" + " ".join(new_row) + " |")

    horizontal_line = "-" * (len(board_state[0]) * 2 + 3)
    result.insert(0, horizontal_line)
    result.append(horizontal_line)

    return "\n".join(result)


def count_live_neighbors(board, x, y):
    #Count the number of live neighbors around a cell at position (x, y) in the board.
    live_neighbors = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
            live_neighbors += 1

    return live_neighbors


def next_board_state(board):
    #Calculate the next board state based on the rules of Conway's Game of Life.
    next_state = [[0] * len(board[0]) for _ in range(len(board))]

    for x in range(len(board)):
        for y in range(len(board[0])):
            live_neighbors = count_live_neighbors(board, x, y)
            if board[x][y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    # Cell dies due to underpopulation or overpopulation
                    next_state[x][y] = 0
                else:
                    # Cell survives
                    next_state[x][y] = 1  
            elif board[x][y] == 0:
                if live_neighbors == 3:
                    # Cell becomes alive through reproduction
                    next_state[x][y] = 1

    return next_state

def random_state_zombies(width, height):
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            random_number = random.random()
            # changable threshold
            if random_number >= 0.3:
                state = 1
                random_number2 = random.random()
                #20% chance of zombie
                if random_number2 >= 0.9:
                    state = 2
            else:
                state = 0
            row.append(state)
        result.append(row)
    return result


def count_live_neighbors_and_zombies(board, x, y):
    #Count the number of live neighbors around a cell at position (x, y) in the board.
    live_neighbors = 0
    zombies = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
            live_neighbors += 1
        elif 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 2:
            zombies += 1
    return live_neighbors,zombies


def next_board_state_zombies(board):
    #Calculate the next board state based on the rules of Conway's Game of Life.
    next_state = [[0] * len(board[0]) for _ in range(len(board))]

    for x in range(len(board)):
        for y in range(len(board[0])):
            live_neighbors, zombies = count_live_neighbors_and_zombies(board, x, y)
            if board[x][y] == 1:
                if live_neighbors < 2:
                    # Cell dies due to underpopulation or overpopulation
                    next_state[x][y] = 0
                elif zombies >= 1:
                    #turns cell into zombie if there is a zombie next to it
                    next_state[x][y] = 2
                else:
                    # Cell survives
                    next_state[x][y] = 1  
            elif board[x][y] == 2:
                if live_neighbors == 0:
                    # Zombies die as there are no cells to eat
                    next_state[x][y] = 0
                elif live_neighbors >= 3:
                    # Zombies die as there are muliplte cells to kill it
                    next_state[x][y] = 0
                else:
                    # Zombie survives
                    next_state[x][y] = 2
            elif board[x][y] == 0:
                if live_neighbors == 3 and live_neighbors == 2:
                    # Cell becomes alive through reproduction
                    next_state[x][y] = 1

    return next_state


def load_board_state(filename):
    board_state = []
    with open(filename, "r") as open_file:
        lines = open_file.readlines()

    for line in lines:
        line = line.strip()
        row = []
        for cell in line:
            row.append(int(cell))

        board_state.append(row)
    return board_state



def main():
    ans = input("file/random/zombie? (f/r/z) ")
    if ans == "f":
        filename = input("Enter filename: ")
        initial_state = load_board_state(filename)
        while True: 
            next_state = next_board_state_zombies(initial_state)
            rendered_state = render(next_state)
            print(rendered_state)

            time.sleep(1)

            initial_state = next_state
    elif ans == "r":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        # Initialize the initial state (you can use your random_state function)
        initial_state = random_state(width, height)
        while True: 
            next_state = next_board_state(initial_state)
            rendered_state = render(next_state)
            print(rendered_state)

            time.sleep(0.15)

            initial_state = next_state
    elif ans == "z":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        # Initialize the initial state (you can use your random_state function)
        initial_state = random_state_zombies(width, height)
        while True: 
            next_state = next_board_state_zombies(initial_state)
            rendered_state = render(next_state)
            print(rendered_state)

            time.sleep(1)

            initial_state = next_state

    

if __name__ == "__main__":
    main()