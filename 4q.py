def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch == " ":
            i += 1
            continue
        if ch.isdigit() or ch == ".":
            num = " "
            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                num += expression[i]
                i += 1
            tokens.append(num)
        elif ch in "+-*/()":
            tokens.append(ch)
            i += 1
        else:
            raise ValueError("Invalid character: " + ch)
    return tokens


def parse_expression(tokens, pos):
    left, pos = parse_term(tokens, pos)
    while pos < len(tokens) and tokens[pos] in ("+", "-"):
        op = tokens[pos]
        right, pos = parse_term(tokens, pos + 1)
        if op == "+":
            left = left + right
        else:
            left = left - right
    return left, pos


def parse_term(tokens, pos):
    left, pos = parse_factor(tokens, pos)
    while pos < len(tokens) and tokens[pos] in ("*", "/"):
        op = tokens[pos]
        right, pos = parse_factor(tokens, pos + 1)
        if op == "*":
            left = left * right
        else:
            if right == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            left = left / right
    return left, pos


def parse_factor(tokens, pos):
    token = tokens[pos]
    if token == "(":
        value, pos = parse_expression(tokens, pos + 1)
        if pos >= len(tokens) or tokens[pos] != ")":
            raise ValueError("Error: Mismatched parentheses.")
        return value, pos + 1
    
    if token == "-":
        value, pos = parse_factor(tokens, pos + 1)
        return -value, pos
    
    try:
        return float(token), pos + 1
    except ValueError:
        raise ValueError("Error: Invalid number: " + token)
    

def calculate(exression):
    tokens = tokenize(exression)
    if not tokens:
        raise ValueError("Error: Empty expression.")
    result, pos = parse_expression(tokens, 0)
    if pos != len(tokens):
        raise ValueError("Error: Invalid expression.")
    return result


while True:
    expr = input("Enter an expression (or 'q' to quit): ").strip()
    if expr == 'q':
        break
    try:
        print("Result:", calculate(expr))
    except (ValueError, ZeroDivisionError) as error:
        print("Error: ", error)
        
