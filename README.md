## Overview
This is a Python-based Rock, Paper, Scissors game that supports both single-player (against the computer) and multiplayer modes. Scores are saved locally for future reference, and multiplayer games can be played over a local network.

### Features
- **Single Player Mode:** Play against the computer and have your scores saved locally.
- **Multiplayer Mode:** Create or join a room to play against another player on the same local network.
- **Score Tracking:** Scores are saved for both single and multiplayer modes and are loaded upon starting the game.
- **Config Files:**
  - `.config/local_scores.json`: Stores local player vs computer scores.
  - `.config/multiplayer_scores.json`: Stores multiplayer scores.
  - `.username.rpc`: Stores the player’s username.

### How to Play
1. Run the script.
2. Choose between Single Player, Multiplayer, or viewing scores.
3. For **single-player**, enter your choice (rock, paper, or scissors) to play against the computer.
4. For **multiplayer**, you can either:
   - Create a room and wait for another player to join.
   - Join an existing room by entering the host's IP address.
5. After each round, scores are updated and saved to the relevant file.
6. You can view your scores by selecting the "Scores" option from the main menu.

### Requirements
- Python 3.x
- Standard Python libraries: `random`, `os`, `time`, `json`, `socket`

### Multiplayer Notes
- The multiplayer mode works over a network using sockets. One player needs to host the game by providing their local IP address, and the other player connects to that IP.
- Ensure that your firewall allows the necessary port (`12345` by default) for connections.

### Example

#### Single Player
```bash
1. Single Player
2. Multiplayer
3. Scores
4. Exit
: 1
Enter Rock/Paper/Scissor: rock
You: rock
Computer: paper
You Lose
Play Again? (Y/N): y
```

#### Multiplayer (Host)
```bash
1. Create Room
2. Join Room
: 1
Waiting for player 2 to connect...
Player 2 connected!
Enter Rock/Paper/Scissor: rock
Player 2: paper
You Lose
```

#### Multiplayer (Join)
```bash
1. Create Room
2. Join Room
: 2
Enter host IP address: 192.168.1.2
Connected to player 1!
Enter Rock/Paper/Scissor: scissor
Player 1: rock
You Lose
```

### License
This project is open-source and free to use under the MIT License.

---