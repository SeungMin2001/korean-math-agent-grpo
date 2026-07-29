from src.math_rl.tools import calculator


def test_calculator():
    result = calculator("6000 / 3 * 5")

    assert result == 10000.0