def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top = []
    bottom = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        width = max(len(num1), len(num2)) + 2
        top.append(num1.rjust(width))
        bottom.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)

        if show_answers:
            result = str(eval(f"{num1} {operator} {num2}"))
            results.append(result.rjust(width))

    arranged = '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(results)

    return arranged


if __name__ == "__main__":
    print('\n' + arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
