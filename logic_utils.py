# FIX: Collaborative update — added cooperative comments describing how human and GitHub Copilot worked together on these helpers.

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Copilot-assisted decision: centralized ranges for clarity and testability.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 20  # Default


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Copilot and developer refined parsing to accept numeric-like strings and give clearer errors.
    if raw is None:
        return False, None, "Enter a guess."

    raw = str(raw).strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        # Allow numeric strings and floats that represent whole numbers
        if "." in raw:
            # reject inputs that are non-numeric after float conversion
            float_val = float(raw)
            value = int(float_val)
            if float_val != value:
                return False, None, "Enter a whole number."
        else:
            value = int(raw)
    except Exception:
        # FIX: Copilot suggested a user-friendly error message for non-numeric input.
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome string: "Win", "Too High", or "Too Low".
    """
    # FIX: Copilot-assisted robustness: coerce secret/guess to ints and surface clear errors for invalid types.
    try:
        if isinstance(secret, str):
            secret = int(secret)
        guess_int = int(guess)
    except Exception:
        # If conversion fails, treat as invalid comparison
        raise ValueError("Non-integer values provided to check_guess")

    if guess_int == secret:
        return "Win"
    if guess_int > secret:
        return "Too High"
    return "Too Low"


def hint_for_outcome(outcome: str):
    """Return a user-facing hint message for a given outcome."""
    # FIX: Copilot helped craft concise emoji hints for better UX.
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    attempt_number is 1-based (first attempt == 1).
    Winning awards between 100 (first try) down to 10 (10th+ try).
    """
    # FIX: Copilot and developer agreed on this scoring heuristic and added comments for maintainability.
    if outcome == "Win":
        points = 110 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # small reward/penalty depending on parity of attempt
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
