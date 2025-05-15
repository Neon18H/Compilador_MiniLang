from syntactic.parser import parser
from semantic.semantic import SemanticAnalyzer
from codegen.codegen import generate_code

def compile_file(filename):
    with open(filename, 'r') as f:
        source = f.read()
    ast = parser.parse(source)

    semantic = SemanticAnalyzer()
    semantic.analyze(ast)  # Aquí detecta errores semánticos

    code = generate_code(ast)
    return code

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.ml")
    else:
        try:
            output = compile_file(sys.argv[1])
            print("Código Python generado:\n")
            print(output)
        except Exception as e:
            print(str(e))
