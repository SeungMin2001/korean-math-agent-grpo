import json
from pathlib import Path

from .schemas import MathProblem


def load_problems(file_path: str | Path) -> list[MathProblem]:
    problems = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            try:
                data = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{line_number}번째 줄의 JSON 형식이 잘못되었습니다."
                ) from error

            problem = MathProblem(
                problem_id=data["problem_id"],
                question=data["question"],
                answer=data["answer"],
                category=data["category"],
            )

            problems.append(problem)

    return problems