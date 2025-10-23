# -*- coding: utf-8 -*-
from typing import Iterable

SUCCESS_MSG = "El analisis sintactico ha finalizado exitosamente."

def error_msg(line: int, col: int, found_lexeme: str, expected: Iterable[str]) -> str:
    exp = '", "'.join(expected)
    return f'<{line},{col}> Error sintactico: se encontro: "{found_lexeme}"; se esperaba: "{exp}"'
