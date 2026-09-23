# Q4. Write a program to implement a simple recursive-descent evaluator for basic arithmetic
# expressions (+, -, *, /) without using eval().

import re
def tokenize(expr):
    return re.findall(r"\d+\.?\d*|[+\-*/()]", expr)
def evaluate(tokens):
    def parse_expr(pos):
        val, pos = parse_term(pos)
        while pos < len(tokens) and tokens[pos] in "+-":
            op = tokens[pos]
            rhs, pos = parse_term(pos + 1)
            val = val + rhs if op == "+" else val - rhs
        return val, pos
    def parse_term(pos):
        val, pos = parse_factor(pos)
        while pos < len(tokens) and tokens[pos] in "*/":
            op = tokens[pos]
            rhs, pos = parse_factor(pos + 1)
            val = val * rhs if op == "*" else val / rhs
        return val, pos
    def parse_factor(pos):
        if tokens[pos] == "(":
            val, pos = parse_expr(pos + 1)
            return val, pos + 1
        return float(tokens[pos]), pos + 1
    result, _ = parse_expr(0)
    return result
expr = "3 + 4 * (2 - 1)"
print(evaluate(tokenize(expr.replace(" ", ""))))