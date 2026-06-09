import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_accepts_whole_number_float_string():
    ok, guess, err = parse_guess("42.0")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_guess_rejects_non_integer_float_string():
    ok, guess, err = parse_guess("42.5")
    assert ok is False
    assert guess is None
    assert err == "Enter a whole number."


def test_get_range_for_hard_mode():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_update_score_awards_minimum_win_points():
    assert update_score(0, "Win", 20) == 10


def test_check_guess_raises_for_invalid_value():
    with pytest.raises(ValueError):
        check_guess("banana", 50)
