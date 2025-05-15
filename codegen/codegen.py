def generate_code(instructions):
    code_lines = []
    for instr in instructions:
        if instr[0] == 'assign':
            var, expr = instr[1], eval_expr(instr[2])
            code_lines.append(f"{var} = {expr}")
        elif instr[0] == 'print':
            code_lines.append(f"print({instr[1]})")
    return "\n".join(code_lines)

def eval_expr(expr):
    if isinstance(expr, tuple):
        op = expr[0]
        if op in ('+', '-', '*', '/'):
            return f"({eval_expr(expr[1])} {op} {eval_expr(expr[2])})"
        elif op == 'num':
            return str(expr[1])
        elif op == 'id':
            return expr[1]
    else:
        return str(expr)
