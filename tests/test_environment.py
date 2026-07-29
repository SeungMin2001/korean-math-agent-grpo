from src.math_rl.environment import MathAgentEnv
from src.math_rl.schemas import AgentAction, MathProblem


def test_environment_flow():
    problem = MathProblem(
        problem_id="test_001",
        question="3 곱하기 5는?",
        answer=15,
        category="arithmetic",
    )

    env = MathAgentEnv(problem)

    observation = env.reset()
    assert observation["question"] == "3 곱하기 5는?"

    observation, reward, done = env.step(
        AgentAction("calculator", "3 * 5")
    )

    assert observation["result"] == 15.0
    assert reward == 0.0
    assert done is False

    observation, reward, done = env.step(
        AgentAction("answer", 15)
    )

    assert observation["correct"] is True
    assert reward == 1.0
    assert done is True