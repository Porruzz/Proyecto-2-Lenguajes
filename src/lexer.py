# -*- coding: utf-8 -*-
import re
from typing import List, Tuple

Token = Tuple[str, str, int, int]  # (tipo, lexema, linea, columna)

RE_ID  = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
RE_NUM = re.compile(r'\d+')

def lex(s: str) -> List[Token]:
    i = 0; line = 1; col = 1
    out: List[Token] = []
    def emit(tt, lx, ln, cl): out.append((tt, lx, ln, cl))
    while i < len(s):
        c = s[i]
        if c == '\n': i += 1; line += 1; col = 1; continue
        if c.isspace(): i += 1; col += 1; continue
        if c in "+*()":
            emit(c, c, line, col); i += 1; col += 1; continue
        m = RE_NUM.match(s, i)
        if m:
            lx = m.group(); emit("id", lx, line, col)
            i = m.end(); col += len(lx); continue
        m = RE_ID.match(s, i)
        if m:
            lx = m.group(); emit("id", lx, line, col)
            i = m.end(); col += len(lx); continue
        # carácter inesperado
        emit("ERROR", s[i], line, col); i += 1; col += 1
        break
    emit("$", "$", line, col)
    return out
