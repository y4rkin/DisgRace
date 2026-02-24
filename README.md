# DisgRace

DisgRace is a 2D vertical scrolling racing game developed in Python using the Pygame library. The player controls a vehicle to navigate through an infinite stream of obstacles. The objective is to survive as long as possible while the game's difficulty progressively increases.

## Game Mechanics

The gameplay loop is infinite and terminates only upon collision. As the session progresses, the game dynamically adjusts difficulty by increasing the vertical speed of the obstacles and the horizontal sensitivity of the player's car. The system tracks the current score in real-time and maintains the highest score achieved during the active session.

## Installation and Execution

Requires Python 3.
1.  **Install Dependencies**
    ~~~bash
    pip install pygame
    ~~~

2.  **Clone the Repository**
    ~~~bash
    git clone https://github.com/y4rkin/DisgRace.git
    cd DisgRace
    ~~~

3.  **Run the Game**
    ~~~bash
    python DisgRace.py
    ~~~

## Controls

| Key | Action |
| :--- | :--- |
| **Left Arrow** | Move Car Left |
| **Right Arrow** | Move Car Right |
| **P** or **ESC** | Pause / Unpause Game |


## License and Acknowledgements

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2020 y4rkin
