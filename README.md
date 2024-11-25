# Python Snake

Python Snake is a simple terminal-based *Snake* game. Currently, it displays a game board, a snake, and an apple, but its mechanics are still under development. The long-term goal is to create a modular system where the game logic is fully decoupled from the interface, enabling other applications to interact with the game and render its states independently.

## Current Features

- Move snake over the table
- Generates a game board with defined borders.
- Displays a snake (`O`) and an apple (`X`).
- Basic rendering of the game's state.

### Current Limitations
- No interaction between the snake and the apple.
- No collision detection or growth mechanics.

## Screenshot
Here is an example of the current game state:


[Demo](https://github.com/user-attachments/assets/2bdc3838-84d0-4017-a220-825d36cada4a
)

## Future Vision

- **Separation of Logic and Rendering**: The game logic will be moved to a central module that allows interaction via an API or function calls. This will enable:
  - Rendering the game in various interfaces (e.g., graphical, web, apps).
  - Integration of the game with other applications.
- **Game Mechanics**:
  - Snake movement.
  - Snake growth when eating the apple.
  - Collision detection with walls or the snake itself.
  - A scoring system.
- **Extensibility**:
  - Multiple game modes.
  - Support for customizable settings.

## Usage

### Requirements
- Python 3.12 (recommended).

### Setting up the environment
It's recommended to use a virtual environment for this project. You can set it up as follows:

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
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

### Instructions
1. Clone this repository:
   ```
   git clone https://github.com/your_username/python-snake.git
   cd python-snake
   ```
2. Run the main script:
   ```
   python main.py
   ```
