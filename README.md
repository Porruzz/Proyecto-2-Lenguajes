# Proyecto-2-Lenguajes
Este proyecto implementa un analizador sintáctico LL(1) completamente funcional en Python, que cumple con los requisitos del Parcial 2 (Lenguajes de Programación):

Cálculo de conjuntos de PRIMEROS y SIGUIENTES

Cálculo de conjuntos de PREDICCIÓN

Generación de la tabla LL(1)

Implementación de un parser predictivo descendente

Ejecución de pruebas automáticas (casos válidos e inválidos)

Benchmark de rendimiento

El sistema también soporta pruebas con una gramática aritmética (E, T, F) y una gramática tipo Python (subset).

📁 Estructura del proyecto
PROYECTO-LL1/
├── examples/
│   ├── ok/               # Casos válidos (aceptados)
│   └── bad/              # Casos inválidos (rechazados)
│
├── grammars/
│   ├── ejemplo_p6.g      # Gramática LL(1) principal (E, T, F)
│   └── python_subset.g   # Subconjunto de gramática estilo Python
│
├── scripts/
│   ├── run_examples.sh   # Ejecuta pruebas automáticas
│   └── bench.sh          # Evalúa el rendimiento
│
├── src/
│   ├── first_follow.py   # Algoritmos de PRIMEROS y SIGUIENTES
│   ├── grammar_io.py     # Lectura e interpretación de gramáticas .g
│   ├── lexer.py          # Análisis léxico
│   ├── ll1_table.py      # Construcción de la tabla LL(1)
│   ├── parser_ll1.py     # Parser predictivo descendente
│   ├── predict.py        # Cálculo de predicciones por producción
│   ├── reporter.py       # Generación de reportes y errores
│   └── main.py           # CLI principal
│
└── tests/
    ├── e2e/              # Pruebas integradas (fin a fin)
    └── unit/             # Pruebas unitarias

⚙️ Ejecución

1️⃣ Verificar la gramática y generar las tablas

python -m src.main --grammar grammars/ejemplo_p6.g --first --follow --predict --table


Esto mostrará los conjuntos FIRST, FOLLOW, PREDICT y la tabla LL(1), junto con la verificación de conflictos.

2️⃣ Ejecutar una prueba de análisis sintáctico (parser LL(1))

python -m src.main --grammar grammars/ejemplo_p6.g --parse examples/ok/expresion1.txt


✅ Si la entrada es válida:

El analisis sintactico ha finalizado exitosamente.


❌ Si la entrada contiene errores:

<1,6> Error sintactico: se encontro: "*"; se esperaba: "(", "id"

3️⃣ Ejecutar todas las pruebas automáticamente

chmod +x scripts/run_examples.sh
./scripts/run_examples.sh


Salida esperada:

== PRUEBAS OK ==
[OK] examples/ok/expresion1.txt
El analisis sintactico ha finalizado exitosamente.
== PRUEBAS BAD ==
[BAD] examples/bad/error1.txt
✅ Rechazado correctamente

4️⃣ Medir rendimiento

chmod +x scripts/bench.sh
./scripts/bench.sh


Salida esperada:

== Benchmark (10 corridas) ==
run 1: 51 ms
run 2: 49 ms
...
avg: 51 ms

📈 Resultados principales
Métrica	Resultado	Estado
Cálculo de PRIMEROS y SIGUIENTES	Correcto	✅
Tabla LL(1) sin conflictos	✓	✅
Parser predictivo descendente	Funcional	✅
Pruebas OK/BAD	Todas correctas	✅
Benchmark	~51 ms promedio	✅

🧩 Gramática utilizada (E, T, F)
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id


Esta gramática es LL(1) y cumple los requisitos del parcial.
