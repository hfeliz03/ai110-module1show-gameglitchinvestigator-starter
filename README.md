# Game Glitch Investigator

## Overview

This project is a Streamlit number guessing game that was originally generated with AI and then debugged and cleaned up. The player chooses a difficulty, guesses a hidden number, and uses the game feedback to narrow down the answer before running out of attempts.

## Setup

1. Install dependencies with `pip install -r requirements.txt`
2. Start the app with `python -m streamlit run app.py`
3. Run tests with `pytest`

## TF Task Summary

### Game Purpose

The app is meant to be a simple guessing game: the program selects a secret number, the player submits guesses, and the app responds with whether the guess was too high, too low, or correct.

### Bugs Identified

1. The secret number could reset across interactions, which broke the game flow and made winning unreliable.
2. Guess feedback needed to be verified so the higher/lower hints matched the actual comparison.
3. Core game behavior was mixed directly into the Streamlit file, which made the logic harder to test.

### Fixes Applied

1. Persisted the active game state with `st.session_state` so the secret number, attempts, score, and history survive reruns.
2. Moved reusable game logic into `logic_utils.py` to keep the Streamlit UI thinner and easier to maintain.
3. Kept guess parsing and comparison logic centralized so feedback stays consistent.
4. Expanded the test coverage with `pytest` to validate win/lose comparisons, input parsing, difficulty ranges, and score behavior.

## Notes

- The Developer Debug Info panel is still available in the app for inspecting state while testing.
- Difficulty settings change both the valid number range and the attempt limit.
