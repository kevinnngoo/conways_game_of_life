import random
import time
import os

# Game of Life - by Kevin Ngo

# Step 1: The ultimate goal of the first milestone is 
# to create a function called random_state. This function will take in 2 arguments - your board’s width and its height.
# It will return a board state in which every cell has been randomly initialized to either ALIVE (represented by a 1) 
# or DEAD (represented by a 0). In Life these random patterns are known as “Soups”, 
# and they are the quickest way for us to start producing interesting output.

def dead_state(width, height):
    # nested list comprehension to run a for loop for the height of the board and width of each row
    return [[0 for _ in range(width)] for _ in range(height)]

def random_state(width, height):
    # Create a dead board and randomize each cell to either 0 or 1 using random.randint
    state = dead_state(width, height)
    for row in range(height):
        for col in range(width):
            state[row][col] = random.randint(0, 1)
    return state

# Step 2: Print the board to the terminal.
# Write a render function that takes in 1 argument: a board state. 
# This will format the board state and print it to the terminal visually.

def render(board_state):
    print('-' * (len(board_state[0]) + 2))  # top border
    for row in board_state:
        line = '|'
        for cell in row:
            if cell == 1:
                line += "#"
            else:
                line += ' '
        line += '|'
        print(line)

# Step 3: Calculating the next state of the board
# If any live cell has 0 or 1 live neighbors, it becomes dead, because of underpopulation.
# Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right.
# Any live cell with more than 3 live neighbors becomes dead, because of overpopulation.
# Any dead cell with exactly 3 live neighbors becomes alive, by reproduction.

def next_board_state(board_state):  # Calculates the next state of the board based on the Game of Life rules. 
    rows, cols = len(board_state), len(board_state[0])
    new_board = [[0] * cols for _ in range(rows)]  # Create a new board for the next state

    for x in range(rows):
        for y in range(cols):
            cell = board_state[x][y]
            neighbors = get_neighbors(x, y, board_state)
            live_neighbors = sum(neighbors)

            if cell == 1 and (live_neighbors == 2 or live_neighbors == 3):
                new_board[x][y] = 1  # Cell stays alive
            elif cell == 0 and live_neighbors == 3:
                new_board[x][y] = 1  # Cell becomes alive
            else:
                new_board[x][y] = 0  # Cell dies or stays dead

    return new_board  # Return the updated board

# Helper function to get the neighbors of a cell
# This function will return a list of the neighbors of a given cell in the board state.
# It checks all 8 adjacent positions, but skips the center cell itself and avoids going out of bounds.

def get_neighbors(row, col, board_state):
    num_rows, num_cols = len(board_state), len(board_state[0])
    neighbors = []

    for d_row in [-1, 0, 1]:  # change in row
        for d_col in [-1, 0, 1]:  # change in column
            if d_row == 0 and d_col == 0:
                continue  # Skip the current cell itself
            neighbor_row = row + d_row
            neighbor_col = col + d_col
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                neighbors.append(board_state[neighbor_row][neighbor_col])

    return neighbors

# Step 4: Run Life forever
# 1. Initialize the starting board state using random_state or another function.
# 2. Use an infinite loop (while True) to repeatedly:
#    - Pass the current board into next_board_state to calculate the next generation.
#    - Render the new board to the terminal using the render function.
#    - Optionally add a short delay (e.g., with time.sleep) between frames.
#    - Update the current board with the new state for the next loop.

if __name__ == "__main__":
    width = 20
    height = 20
    starting_board_state = random_state(width, height)

    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear terminal for animation
        render(starting_board_state)
        starting_board_state = next_board_state(starting_board_state)
        time.sleep(0.1)  # Pause between frames to simulate motion
