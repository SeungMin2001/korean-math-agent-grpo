from .tools import calculator
from .verifier import verify_answer
from .schemas import TrajectoryStep # observation을 포함한 step별 기록
import json
from dataclasses import asdict

class MathAgentEnv:
    def __init__(self, problem):
        self.problem=problem #문제
        self.done=False #종료여부
        self.tool_results=[] #툴 결과
        self.trajectory=[]
        self.step_number=0
    
    def reset(self): #초기화.
        self.done=False
        self.tool_results=[]
        self.trajectory=[]
        self.step_number=0
        
        return {
            "question":self.problem.question,
            "tool_results":self.tool_results
        }
        
    def step(self, action):
        if self.done: #이미종료
            raise RuntimeError("already end")
        
        self.step_number+=1
        
        if action.action_type == "calculator": #모델 계산할때
            result=calculator(action.payload)
            self.tool_results.append(result) #모델 계산결과 저장
            
            observation={
                "type":"tool_result",
                "result":result
            }
            
            self.trajectory.append(
                TrajectoryStep(
                    step_number=self.step_number,
                    action=action,
                    observation=observation,
                    reward=0.0,
                    done=False
                )
            )
            
            return observation,0.0,False #검증까지 하고 보상
            
        if action.action_type=="answer":
            result=verify_answer(
                predicted_answer=float(action.payload), #모델
                expected_answer=self.problem.answer #답
            )
            
            self.done=True
            
            observation={
                "type":"final_result",
                **result
            }
            
            self.trajectory.append(
                TrajectoryStep(
                    step_number=self.step_number,
                    action=action,
                    observation=observation,
                    reward=result["reward"],
                    done=True
                )
            )
            
            return observation,result["reward"],True
            
        raise ValueError("error")
    
    def save_trajectory(self, file_path:str):
        trajectory_data=[
            asdict(step)
            for step in self.trajectory
        ]
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                trajectory_data,
                file,
                ensure_ascii=False,
                indent=2,
            )
        
            
        