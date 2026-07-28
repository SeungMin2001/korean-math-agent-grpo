import ast # change str to 식
import operator # 계산 함수들

OPERATORS={ #기호, 함수 연결
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def calculator(expression: str) -> float: # 수식 입력 -> 계산 반환(float)
    tree=ast.parse(expression, mode="eval").body
    
    if isinstance(tree, ast.Constant):
        return float(tree.value)
    
    if isinstance(tree,ast.BinOp): #재귀 
        left=calculator(ast.unparse(tree.left))
        right=calculator(ast.unparse(tree.right))
        operation=OPERATORS[type(tree.op)]
        
        return operation(left, right)
            
    return ValueError("오류")