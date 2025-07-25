from game import (
    generate_secret_number,
    provide_feedback,
    track_guess,
    ask_to_play_again,
    get_user_guess,
    parse_arguments,
)
import sys


def test_generate_secret_number():
    min_range = 1
    max_range = 100
    secret_number = generate_secret_number(min_range, max_range)
    assert isinstance(secret_number, int)
    assert min_range <= secret_number <= max_range


def test_provide_feedback():
    # Test too low
    assert provide_feedback(50, 75) == "Too low!"
    # Test too high
    assert provide_feedback(75, 50) == "Too high!"
    # Test correct
    assert provide_feedback(50, 50) == "You guessed it!"


def test_track_guess():
    assert track_guess(0) == 1
    assert track_guess(5) == 6


def test_ask_to_play_again(monkeypatch):
    # Test 'yes' response
    monkeypatch.setattr("builtins.input", lambda _: "yes")
    assert ask_to_play_again() is True

    # Test 'no' response
    monkeypatch.setattr("builtins.input", lambda _: "no")
    assert ask_to_play_again() is False

    # Test invalid input then 'yes'
    inputs = iter(["invalid", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert ask_to_play_again() is True

    # Test invalid input then 'no'
    inputs = iter(["invalid", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert ask_to_play_again() is False


def test_get_user_guess(monkeypatch, capsys):
    min_range = 1
    max_range = 100

    # Test valid input
    monkeypatch.setattr("builtins.input", lambda _: "50")
    assert get_user_guess(min_range, max_range) == 50

    # Test non-integer input then valid input
    inputs = iter(["abc", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_user_guess(min_range, max_range) == 25
    captured = capsys.readouterr()
    assert "Invalid input. Please enter a valid integer." in captured.out

    # Test input below min_range then valid input
    inputs = iter(["0", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_user_guess(min_range, max_range) == 1
    captured = capsys.readouterr()
    assert (
        f"Your guess is out of range. Please enter a number between {min_range} and {max_range}."
        in captured.out
    )

    # Test input above max_range then valid input
    inputs = iter(["101", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_user_guess(min_range, max_range) == 100
    captured = capsys.readouterr()
    assert (
        f"Your guess is out of range. Please enter a number between {min_range} and {max_range}."
        in captured.out
    )


def test_parse_arguments(monkeypatch):
    # Test default arguments
    monkeypatch.setattr(sys, "argv", ["game.py"])
    min_val, max_val = parse_arguments()
    assert min_val == 1
    assert max_val == 100

    # Test custom arguments
    monkeypatch.setattr(sys, "argv", ["game.py", "--min", "10", "--max", "50"])
    min_val, max_val = parse_arguments()
    assert min_val == 10
    assert max_val == 50
