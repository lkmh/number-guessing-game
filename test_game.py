from game import generate_secret_number, provide_feedback, track_guess


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
