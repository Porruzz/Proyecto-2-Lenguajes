# -*- coding: utf-8 -*-
from typing import Dict, List, Set
from .grammar_io import Grammar, EPS

def first_sets(G: Grammar) -> Dict[str, Set[str]]:
    F: Dict[str, Set[str]] = {A: set() for A in G}
    changed = True
    while changed:
        changed = False
        for A, alts in G.items():
            for rhs in alts:
                nullable = True
                for X in rhs:
                    if X in G:  # no terminal
                        add = F[X] - {EPS}
                        if not add.issubset(F[A]):
                            F[A] |= add; changed = True
                        if EPS not in F[X]:
                            nullable = False
                            break
                    else:       # terminal
                        if X not in F[A]:
                            F[A].add(X); changed = True
                        nullable = False
                        break
                if nullable and EPS not in F[A]:
                    F[A].add(EPS); changed = True
    return F

def _first_of_sequence(seq: List[str], F: Dict[str, Set[str]], G: Grammar) -> Set[str]:
    out: Set[str] = set()
    nullable = True
    for X in seq:
        if X in G:
            out |= (F[X] - {EPS})
            if EPS not in F[X]:
                nullable = False; break
        else:
            out.add(X); nullable = False; break
    if nullable:
        out.add(EPS)
    return out

def follow_sets(G: Grammar, start: str, F: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    Fo: Dict[str, Set[str]] = {A: set() for A in G}
    Fo[start].add("$")
    changed = True
    while changed:
        changed = False
        for A, alts in G.items():
            for rhs in alts:
                for i, X in enumerate(rhs):
                    if X in G:
                        beta = rhs[i+1:]
                        first_beta = _first_of_sequence(beta, F, G) if beta else {EPS}
                        add = first_beta - {EPS}
                        if not add.issubset(Fo[X]):
                            Fo[X] |= add; changed = True
                        if EPS in first_beta and not Fo[A].issubset(Fo[X]):
                            Fo[X] |= Fo[A]; changed = True
    return Fo
