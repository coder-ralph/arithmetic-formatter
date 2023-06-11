import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        if re.search(r"[^\s0-9.+-]", problem):
            if re.search(r"[/*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        operand1, operator, operand2 = re.split(r"\s+([+-])\s+", problem)
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        first_line += operand1.rjust(width) + "    "
        second_line += operator + " " + operand2.rjust(width - 2) + "    "
        dash_line += "-" * width + "    "

        if show_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line += answer.rjust(width) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()
    if show_answers:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems
