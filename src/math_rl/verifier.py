def verify_answer(predicted_answer:float, expected_answer:float)->dict:
    is_correct=abs(predicted_answer-expected_answer)<1e-6
    
    return {
        "correct":is_correct,
        "reward":1.0 if is_correct else 0.0
    }