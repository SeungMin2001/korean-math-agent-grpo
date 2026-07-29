from src.math_rl.tools import calculator # 계산 툴
from src.math_rl.verifier import verify_answer #검증 및 보상
from src.math_rl.schemas import AgentAction, MathProblem
from src.math_rl.environment import MathAgentEnv

problem=MathProblem(
    problem_id="01",
    question="사과 3개의 가격이 6000원일 때 5개의 가격은?",
    answer=10000,
    category="arithmetic"
)

env=MathAgentEnv(problem)

print(env.reset())

tool_action=AgentAction( #계산
    action_type="calculator",
    payload="6000/3*5"
)

observation,reward,done=env.step(tool_action)
print(observation,reward,done)

answer_action=AgentAction( #답 나오고 검증
    action_type="answer",
    payload=10000
)

observation,reward,done=env.step(answer_action)
print(observation,reward,done)

wrong_env = MathAgentEnv(problem)
wrong_env.reset()

wrong_action = AgentAction(
    action_type="answer",
    payload=9000,
)

observation, reward, done = wrong_env.step(wrong_action)

print(observation, reward, done)

invalid_env = MathAgentEnv(problem)
invalid_env.reset()

invalid_action = AgentAction(
    action_type="search",
    payload="사과 가격",
)

try:
    invalid_env.step(invalid_action)
except ValueError as error:
    print(error)