from src.math_rl.tools import calculator # 계산 툴

try:
    result=calculator("hello")
    print(result)
    
except ValueError as error:
    print(error)
