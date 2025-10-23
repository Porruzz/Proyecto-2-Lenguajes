# -*- coding: utf-8 -*-
from typing import Dict, List, Set, Tuple
from .grammar_io import Grammar
from .predict import predict_sets

Table = Dict[Tuple[str, str], List[List[str]]]

def build_ll1_table(G: Grammar, start: str) -> Tuple[Table, int]:
    _, _, P = predict_sets(G, start)
    table: Table = {}
    conflicts = 0
    for (A, rhs), terms in P.items():
        for a in terms:
            key = (A, a)
            table.setdefault(key, [])
            table[key].append(list(rhs))
            if len(table[key]) > 1:
                conflicts += 1
    return table, conflicts
