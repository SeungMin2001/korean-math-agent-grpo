from dataclasses import dataclass
from typing import Any

@dataclass
class MathProblem: #문제 
    problem_id: int
    question: str
    answer: Any
    category: str
    
@dataclass
class AgentAction: #모델 행동 
    action_type: str
    payload: Any
    
@dataclass
class EnvironmentResult: #환경이 행동 처리한 결과
    obervation: dict # 모델이 확인할 결과
    reward: float # 보상
    terminated: bool # good end?
    truncated: bool #초과 됬니?
    info: dict # 추가정보
    