from src.math_rl.verifier import verify_answer


def test_correct_answer():
    result = verify_answer(10000, 10000)

    assert result["correct"] is True
    assert result["reward"] == 1.0


def test_wrong_answer():
    result = verify_answer(9000, 10000)

    assert result["correct"] is False
    assert result["reward"] == 0.0