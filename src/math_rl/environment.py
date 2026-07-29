from .tools import calculator
from .verifier import verify_answer

class MathAgentEnv:
    def __init__(self, problem):
        self.problem=problem #문제
        self.done=False #종료여부
        self.tool_results=[] #툴 결과
    
    def reset(self): #초기화.
        self.done=False
        self.tool_results=[]
        
        return {
            "question":self.problem.question,
            "tool_results":self.tool_results
        }
        
    def step(self, action):
        if self.done: #이미종료
            raise RuntimeError("already end")
        
        if action.action_type == "calculator": #모델 계산할때
            result=calculator(action.payload)
            self.tool_results.append(result) #모델 계산결과 저장
            
            return {
                "type":"tool_result",
                "result":result
            },0.0,False #검증까지 하고 보상
            
        if action.action_type=="answer":
            result=verify_answer(
                predicted_answer=float(action.payload), #모델
                expected_answer=self.problem.answer #답
            )
            self.done=True
            return{
                "type":"final_result",
                **result # result(dic)넣어주기
            },result["reward"],True
            
        raise ValueError("error")
            
        