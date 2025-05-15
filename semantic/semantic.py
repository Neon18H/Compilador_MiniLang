class SemanticAnalyzer:
    def __init__(self):
        self.symbols = set()

    def analyze(self, instructions):
        for instr in instructions:
            kind = instr[0]
            if kind == 'assign':
                var = instr[1]
                self.symbols.add(var)
                self._check_expr(instr[2])
            elif kind == 'print':
                var = instr[1]
                if var not in self.symbols:
                    raise NameError(f"Error semántico: variable '{var}' no definida.")

    def _check_expr(self, expr):
        if isinstance(expr, tuple):
            op = expr[0]
            if op in ('+', '-', '*', '/'):
                self._check_expr(expr[1])
                self._check_expr(expr[2])
            elif op == 'id':
                var = expr[1]
                if var not in self.symbols:
                    raise NameError(f"Error semántico: variable '{var}' no definida.")
           
