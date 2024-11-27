# Python Snake

Python Snake is a simple terminal-based *Snake* game. The project is evolving, and new mechanics are being added incrementally. Currently, the game supports basic gameplay features such as collision detection and increasing speed.

## Current Features

- **Game Board**:
  - A bordered play area is displayed in the terminal.
  - A snake (`O`) and a food item (`X`) are rendered.

- **Game Mechanics**:
  - The snake moves within the game board.
  - Collisions:
    - Collision with food increases the speed of the snake.
    - Collision with walls or the snake's own body ends the game.
  - Speed Adjustment:
    - The snake's speed dynamically increases when it consumes food.

- **Planned Improvements**:
  - Fully functional gameplay execution.
  - Snake growth when eating food.
  - Scoring system.

## Screenshot
Here is an example of the current game state:


https://github.com/user-attachments/assets/aa2b32ec-5c4b-46d2-b94a-3d4541693144



## Future Vision

- **Separation of Logic and Rendering**: The game's logic will be abstracted into a central module, enabling interaction via an API or function calls for rendering in various interfaces.
- **Game Modes and Extensibility**:
  - Multiple game modes.
  - Customizable settings like board size, initial speed, etc.

## Usage

### Requirements
- Python 3.12 (recommended).

### Setting up the Environment
To ensure a consistent environment, it's recommended to use a virtual environment.

1. Create a virtual environment:
   ```
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
3. Install dependencies from the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

### Running the Game
1. Clone this repository:
   ```
   git clone https://github.com/your_username/python-snake.git
   cd python-snake
   ```
2. Run the main script:
  ```
   python main.py
  ```

   **Note**: Currently, the game cannot be fully executed due to pending implementation of core functionalities.


## Contributions

Contributions are welcome! If you have ideas or improvements, feel free to open an issue or submit a pull request.

## TODOs
- Implement snake growth upon consuming food.
- Allow the game to run seamlessly.
- Add a scoring system based on snake growth and speed.

