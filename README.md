# Conway's Game of Life with Zombies
This is a Python implementation of Conway's Game of Life with a twist - it introduces zombies into the mix. In Conway's Game of Life, cells evolve based on a set of rules, and in this version, some cells can turn into zombies!

### Overview
Conway's Game of Life is a cellular automaton that simulates the evolution of cells on a grid. In this implementation, cells can be in one of three states in the alteration:

- Dead (0): Represented as empty cells.
- Alive (1): Represented as cells with an "X."
- Zombie (2): Represented as cells with a "Z."

The game evolves over time according to the following rules:

- A live cell with fewer than 2 live neighbors dies due to underpopulation.
- A live cell with more than 3 live neighbors dies due to overpopulation.
- A live cell with 2 or 3 live neighbors survives.
- A dead cell with exactly 3 live neighbors becomes alive through reproduction.
- If a live cell has a zombie neighbor, it turns into a zombie.
### Getting Started

Clone this repository to your local machine.
Make sure you have Python 3.x installed on your system.
Open a terminal and navigate to the repository's directory.
Run the script by executing the following command:

Copy code
python game_of_life.py
You will be prompted to choose one of the following options:

"f" to load a board state from a file.
"r" to create a random initial state for Conway's Game of Life without any alterations.
"z" to create a random initial state with zombies.
Follow the prompts to specify the board size or filename if applicable.

Watch the game evolve with live cells and zombies!

### File Input
If you choose the option to load a board state from a file, make sure your file follows this format:
- Use 0s to represent dead cells.
- Use 1s to represent live cells.
- Use 2s to represent zombie cells.
Example file content for a 3x3 grid with some live cells and zombies:
010
211
100

### Customization
You can customize the behavior of the simulation by modifying the code in the game_of_life.py file. You can change parameters such as the initial state creation, threshold values for randomness, and timing intervals for updates.

### Enjoy the Game!
Have fun!
