
# input format: ["+", "3", "3"]
# range: -301 to 301 (300 included)
# invalid number inputs should return None
# operators available: +, -, *, /
# the division between two integers always truncates toward 0: 1/2=0 or 12/7=0
# if there is a division by 0, should return None
# the input must be valid as a polish notation: this is not valid: ["*", "-", "3", "4"]

input = ["3"]

def evaluatePNExpression(input):
    try:
        for i in range(0, len(input)):
            try:
                input[i] = int(input[i])
                if input[i] > 300 or input[i] < -300:
                    return None
            except:
                pass
        k = 2
        res = 0
        while len(input) > 1:
            if k == len(input) and type(input[k-1]) == int:
                if input[k-3] == '+':
                    res = input[k-1] + input[k-2]
                if input[k-3] == '-':
                    res = input[k-1] - input[k-2]
                if input[k-3] == '*':
                    res = input[k-1] * input[k-2]
                if input[k-3] == '/':
                    res = input[k-1] // input[k-2]
                    if res == 0:
                        return None
                input.pop(k-1)
                input.pop(k-2)
                input[k-3] = res
                k = 2
            if len(input) == 1:
                if int(input[0]) or input[0] == 0:
                    return input[0]
                    break
                else:
                    return None
                    break
            if type(input[k-1]) is int and type(input[k]) is int:
                if input[k-2] == '+':
                    res = input[k-1] + input[k]
                if input[k-2] == '-':
                    res = input[k - 1] - input[k]
                if input[k-2] == '*':
                    res = input[k - 1] * input[k]
                if input[k-2] == '/':
                    res = input[k - 1] // input[k]
                input.pop(k-2)
                input.pop(k-2)
                input[k-2] = res
                k = 2
            if len(input) == 1:
                if int(input[0]) or input[0] == 0:
                    return input[0]
                    break
                else:
                    return None
                    break
            k += 1
    except:
        return None


print(evaluatePNExpression(input))

invalid_prefix_test_cases = [
    ["+", "301", "3"],  # Invalid (out of range)
    ["/", "10", "0"],  # Invalid (division by zero)
    ["+", "-", "3", "4"],  # Invalid (not a valid expression)
    ["+", "*", "3", "4"],  # Invalid (not a valid expression)
    ["*", "/", "4", "2", "1"],  # Invalid (not a valid expression)
    ["3", "3", "+"],  # Invalid (missing operator)
    ["+", "+", "5", "3", "/", "2"],  # Invalid (operator without operands)
    ["-", "7", "2", "3"],  # Invalid (extra operands)
    ["+", "1", "2", "3"],  # Invalid (extra operands)
    ["-", "5", "+", "3", "*", "2", "4"],  # Invalid (extra operands)
    ["2"],
    ["+"],
    ["="],
    ["3", "2"],
    ["=", "="]
]

def evaluate_prefix_test_cases(test_cases):
    for i, test_case in enumerate(test_cases):
        print(f"Test Case {i + 1}: {test_case}")
        val = evaluatePNExpression(test_case)
        if val is not None:
            print(f"The value is: {val}")
        else:
            print("Invalid expression")

evaluate_prefix_test_cases(invalid_prefix_test_cases)
