# Number Guessing Game

A simple Python game where players try to guess a randomly generated number within a specified range. The game provides feedback on whether the guessed number is too high or too low, helping the player reach the correct answer.

## How It Works
1. The player sets the upper limit of the number range.
2. A random number is generated between 0 and the chosen upper limit.
3. The player attempts to guess the number.
   - If the guess is too low, the game informs the player and allows another attempt.
   - If the guess is too high, the game provides similar feedback.
4. The game continues until the player guesses the correct number.
5. The total number of attempts is displayed upon successful completion.

## Features
- Dynamic number range defined by the player.
- Real-time feedback for each guess.
- Tracks the number of attempts taken to guess the number correctly.

## Example Gameplay
```
Enter the top range you would like for this game. 
50
Enter a number
25
The number entered is smaller than the generated number
Enter a number
35
The number entered is larger than the generated number
Enter a number
30
Congratulations! You guessed the correct number.
You got the correct number in 3 tries.
```

## Getting Started
### Prerequisites
- Python 3.x installed on your system.

### Running the Game
1. Clone the repository or download the script file.
2. Open a terminal or command prompt.
3. Run the script using the following command:
   ```
   python number_guessing_game.py
   ```

### Code Explanation
- **`random.randint(0, top_range)`**: Generates a random number between 0 and the specified upper limit.
- **`while` loop**: Continues until the guessed number matches the generated number.
- **`if` statements**: Provides feedback to the player based on whether their guess is too low or too high.

## Contributions
Feel free to fork this repository, make changes, and submit pull requests. Suggestions for enhancements are always welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
