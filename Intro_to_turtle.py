import turtle
import random

# Constants
WIDTH = 300
HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE

# Tetromino colors
TETROMINO_COLORS = {
    "I": "cyan",
    "O": "yellow",
    "T": "purple",
    "L": "orange",
    "J": "blue",
    "S": "green",
    "Z": "red"
}

# Set up the screen
screen = turtle.Screen()
screen.title("Tetris")
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)  # Disable automatic screen updates

# Set up the turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Initialize the grid (list of lists)
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Tetromino shapes (as relative coordinates)
tetrominoes = {
    "I": [[(0, 1), (0, 0), (0, -1), (0, -2)]],  # Vertical line
    "O": [[(0, 1), (1, 1), (0, 0), (1, 0)]],  # Square
    "T": [[(0, 1), (0, 0), (1, 0), (-1, 0)]],  # T-shape
    "L": [[(0, 1), (0, 0), (0, -1), (1, -1)]],  # L-shape
    "J": [[(0, 1), (0, 0), (0, -1), (-1, -1)]],  # Reverse L-shape
    "S": [[(0, 1), (1, 0), (0, 0), (-1, -1)]],  # S-shape
    "Z": [[(0, 1), (1, 0), (0, 0), (-1, 1)]],  # Z-shape
}

# Current Tetromino (randomly selected)
current_tetromino = random.choice(list(tetrominoes.keys()))
current_shape = tetrominoes[current_tetromino][0]
current_position = [GRID_HEIGHT-1, GRID_WIDTH//2]

def draw_grid():
    """Draw the grid for the Tetris game."""
    pen.penup()
    pen.pensize(1)
    pen.color("gray")
    
    # Draw horizontal lines
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pen.setpos(-WIDTH//2, HEIGHT//2 - y)
        pen.pendown()
        pen.forward(WIDTH)
        pen.penup()

    pen.setheading(90)
    # Draw vertical lines
    for x in range(0, WIDTH, BLOCK_SIZE):
        pen.setpos(-WIDTH//2 + x, HEIGHT//2)
        pen.pendown()
        pen.forward(HEIGHT)
        pen.penup()

def draw_tetromino():
    """Draw the current tetromino at its current position."""
    pen.penup()
    pen.color(TETROMINO_COLORS[current_tetromino])  # Use the tetromino's color
    
    for block in current_shape:
        x_offset, y_offset = block
        x_pos = current_position[1] * BLOCK_SIZE + x_offset * BLOCK_SIZE
        y_pos = HEIGHT//2 - current_position[0] * BLOCK_SIZE - y_offset * BLOCK_SIZE
        pen.setpos(x_pos, y_pos)
        pen.pendown()
        pen.begin_fill()
        for _ in range(4):
            pen.forward(BLOCK_SIZE)
            pen.right(90)
        pen.end_fill()
        pen.penup()

def move_tetromino():
    """Move the tetromino down."""
    current_position[0] -= 1  # Move down by one row

    # Check for collisions with the grid boundaries or filled blocks
    for block in current_shape:
        x_offset, y_offset = block
        x_pos = current_position[1] + x_offset
        y_pos = current_position[0] + y_offset

        if y_pos < 0 or x_pos < 0 or x_pos >= GRID_WIDTH or grid[y_pos][x_pos] is not None:
            current_position[0] += 1  # Undo the move if there's a collision
            place_tetromino()
            return False  # Tetromino has landed

    return True  # Tetromino can still move down

def place_tetromino():
    """Place the tetromino on the grid."""
    for block in current_shape:
        x_offset, y_offset = block
        x_pos = current_position[1] + x_offset
        y_pos = current_position[0] + y_offset
        grid[y_pos][x_pos] = TETROMINO_COLORS[current_tetromino]  # Store the color of the block

    clear_lines()
    new_tetromino()

def clear_lines():
    """Clear any full lines on the grid."""
    global grid
    for row in range(GRID_HEIGHT):
        if None not in grid[row]:
            # This row is full, clear it
            grid.pop(row)
            grid.insert(0, [None] * GRID_WIDTH)  # Insert an empty row at the top

def new_tetromino():
    """Generate a new tetromino and reset its position."""
    global current_tetromino, current_shape, current_position
    current_tetromino = random.choice(list(tetrominoes.keys()))
    current_shape = tetrominoes[current_tetromino][0]
    current_position = [GRID_HEIGHT-1, GRID_WIDTH//2]

def rotate_tetromino():
    """Rotate the current tetromino."""
    global current_shape
    # Rotate the coordinates of the tetromino
    current_shape = [(y, -x) for x, y in current_shape]

    # Check for collisions after rotation
    for block in current_shape:
        x_offset, y_offset = block
        x_pos = current_position[1] + x_offset
        y_pos = current_position[0] + y_offset
        if x_pos < 0 or x_pos >= GRID_WIDTH or y_pos < 0 or grid[y_pos][x_pos] is not None:
            # If collision, revert rotation
            current_shape = [(y, -x) for x, y in current_shape]  # Undo the rotation
            break

def game_loop():
    """The main game loop."""
    if move_tetromino():
        pen.clear()
        draw_grid()
        draw_tetromino()
        screen.update()
        screen.ontimer(game_loop, 500)  # Continue the game every 500 ms
    else:
        print("Game Over!")

# Start the game loop
game_loop()

# Listen to key presses for controls
screen.listen()
screen.onkey(lambda: current_position.__setitem__(1, current_position[1] - 1), "Left")  # Move left
screen.onkey(lambda: current_position.__setitem__(1, current_position[1] + 1), "Right")  # Move right
screen.onkey(lambda: current_position.__setitem__(0, current_position[0] - 1), "Down")  # Move down
screen.onkey(rotate_tetromino, "Up")  # Rotate

# Start the screen
screen.mainloop()
