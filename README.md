# Compilador_MiniLang

| Fase           | Descripción                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------|
| **Léxico**     | Convierte el código fuente en tokens (identificadores, números, operadores, palabras reservadas).|
| **Sintáctico** | Valida la estructura del código con reglas gramaticales y genera un árbol sintáctico (AST).      |
| **Semántico**  | Verifica el significado del programa, asegurando que variables usadas estén definidas previamente.|



## Arquitectura de Carpetas

minilang_compiler/
├── lexer/ # Análisis léxico
├── syntactic/ # Análisis sintáctico
├── semantic/ # Análisis semántico
├── codegen/ # Generación de código Python
├── sample_programs/ # Ejemplos de código MiniLang
├── main.py # Punto de entrada del compilador
└── README.md # Documentación del proyecto
