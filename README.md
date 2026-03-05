# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] **Describe the game's purpose.**  
The purpose of the game is to guess a secret number chosen by the program. The game provides hints ("Higher" or "Lower") to guide the player toward the correct number.

- [ ] **Detail which bugs you found.**  
1. The secret number changes every time the "Submit" button is clicked, making it impossible to win.  
2. The hints provided ("Higher" or "Lower") are incorrect and misleading.  

- [ ] **Explain what fixes you applied.**  
1. To fix the secret number resetting issue, I used Streamlit's `st.session_state` to persist the secret number across button clicks.  
2. I corrected the logic for the hints by comparing the player's guess with the secret number and ensuring the output accurately reflects whether the guess is too high or too low.  
3. I refactored the game logic into a separate `logic_utils.py` file for better modularity and maintainability.  
4. I wrote and ran tests using `pytest` to verify the correctness of the fixes.

## 📸 Demo

![Winning Game Screenshot](Screenshot%202026-03-04%20at%2010.49.59%20p.m..png)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
