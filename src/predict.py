# -*- coding: utf-8 -*-
from typing import Dict, List, Set, Tuple
from .grammar_io import Grammar, EPS
from .first_follow import first_sets, follow_sets

def _first_of_sequence(seq: List[str], F: Dict[str, Set[str]], G: Grammar) -> Set[str]:
    out: Set[str] = set()
    nullable = True
    for X in seq:
        if X == EPS:
            continue
        if X in G:
            out |= (F[X] - {EPS})
            if EPS not in F[X]:
                nullable = False; break
        else:
            out.add(X); nullable = False; break
    if nullable:
        out.add(EPS)
    return out

def predict_sets(G: Grammar, start: str) -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]], Dict[Tuple[str, Tuple[str,...]], Set[str]]]:
    F = first_sets(G)
    Fo = follow_sets(G, start, F)
    P: Dict[Tuple[str, Tuple[str, ...]], Set[str]] = {}
    for A, alts in G.items():
        for rhs in alts:
            First = _first_of_sequence(rhs, F, G)
            terms = (First - {EPS})
            if EPS in First:
                terms |= Fo[A]
            P[(A, tuple(rhs))] = terms
    return F, Fo, P
