# Subconjunto de Python para pruebas LL(1)
S -> stmt S | ε
stmt -> assign | print
assign -> ID = expr
expr -> term expr'
expr' -> + term expr' | ε
term -> factor term'
term' -> * factor term' | ε
factor -> ( expr ) | ID | NUM
print -> print ( expr )
