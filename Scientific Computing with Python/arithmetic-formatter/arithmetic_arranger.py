from typing import List

def arithmetic_arranger(problems: List[str], calculate_solution: bool = False) -> str:
    SPACE: str = " " * 4
    top_row: str = ""
    bot_row: str = ""
    spacers: str = ""
    results: str = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        active_problem = problem.split()
        num_1: str = active_problem[0]
        operator: str = active_problem[1]
        num_2: str = active_problem[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not (num_1.isdecimal() and num_2.isdecimal()):
            return "Error: Numbers must only contain digits."

        if (len(num_1) and len(num_2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        length: int = max(len(num_1), len(num_2)) + 2
        top: str = num_1.rjust(length)
        bot: str = operator + num_2.rjust(length - 1)
        spacer: str = "-" * length
        result: str = "".rjust(length)

        if calculate_solution:
            if operator == "+":
                result = str(int(num_1) + int(num_2)).rjust(length)
            else:
                result = str(int(num_1) - int(num_2)).rjust(length)

        if problem == problems[-1]:
            top_row += top
            bot_row += bot
            spacers += spacer
            results += result
        else:
            top_row += top + SPACE
            bot_row += bot + SPACE
            spacers += spacer + SPACE
            results += result + SPACE
    
    if calculate_solution:
        arranged_problems: str = (
            top_row + "\n" + bot_row + "\n" + spacers + "\n" + results
        )
    else:
        arranged_problems: str = top_row + "\n" + bot_row + "\n" + spacers

    return arranged_problems