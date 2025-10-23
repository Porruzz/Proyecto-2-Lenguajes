# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple
from .grammar_io import Grammar, EPS
from .ll1_table import build_ll1_table
from .lexer import lex
from .reporter import error_msg, SUCCESS_MSG

def parse_file_ll1(G: Grammar, start: str, path: str) -> Tuple[bool, str]:
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    tokens = lex(src)
    table, conflicts = build_ll1_table(G, start)
    if conflicts > 0:
        return False, "La gramática no es LL(1): hay conflictos en la tabla."

    stack: List[str] = ["$", start]
    i = 0  # índice del token actual
    while stack:
        X = stack.pop()
        t_type, t_lex, t_ln, t_col = tokens[i]

        if X == "$":
            if t_type == "$":
                return True, SUCCESS_MSG
            # error: input sobrante
            return False, error_msg(t_ln, t_col, t_lex, ["$"])

        # terminal
        if X not in G and X != EPS:
            if X == t_type:
                i += 1  # consumir token
                continue
            # error por terminal esperado
            return False, error_msg(t_ln, t_col, t_lex, [X])

        # no terminal
        if X in G:
            key = (X, t_type)
            prods = table.get(key, [])
            if not prods:
                # esperado = llaves con X en tabla
                expected = sorted({a for (A,a) in table.keys() if A == X})
                return False, error_msg(t_ln, t_col, t_lex, expected if expected else [X])
            rhs = prods[0]   # LL(1) → a lo sumo 1
            # apilar en orden inverso (omitir ε)
            for sym in reversed(rhs):
                if sym != EPS:
                    stack.append(sym)
            continue

        # ε (no llega aquí porque ε se omite al apilar)
    # si salimos sin $, rechazamos
    # tomar último token para reportar
    t_type, t_lex, t_ln, t_col = tokens[min(i, len(tokens)-1)]
    return False, error_msg(t_ln, t_col, t_lex, ["$"])
