from src.math_rl.tools import calculator # 계산 툴
from src.math_rl.verifier import verify_answer #검증 및 보상
from src.math_rl.schemas import AgentAction, MathProblem
from src.math_rl.environment import MathAgentEnv
from src.math_rl.data_loader import load_problems

def main():
    problems=load_problems("data/sample.jsonl")
    
    problem=problems[0]
    environment=MathAgentEnv(problem)
    
    initial_state=environment.reset() #초기화
    
    calculation_action=AgentAction(
        "calculator",
        "6000/3*5"
    )
    calculation_result = environment.step(calculation_action)

    answer_action = AgentAction(
        "answer",
        10000
    )

    final_result = environment.step(answer_action)
    print("최종 결과:", final_result)

if __name__ == "__main__":
    main()