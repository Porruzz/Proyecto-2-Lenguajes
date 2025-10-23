# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple

EPS = "ε"
Grammar = Dict[str, List[List[str]]]

def _tokenize_rhs(s: str) -> List[str]:
    # separa por espacios respetando símbolos como + * ( )
    # si el usuario escribe pegado, igual funciona para ()+-*
    out, buf = [], ""
    def flush():
        nonlocal buf
        if buf:
            out.append(buf); buf = ""
    for c in s:
        if c.isspace(): flush()
        elif c in "+*()|":
            flush(); out.append(c)
        else:
            buf += c
    flush()
    return [t for t in out if t]

def load_grammar(path: str) -> Tuple[str, Grammar]:
    """
    Formato por línea:
      A -> alpha1 | alpha2 | ...
    Soporta comentarios con # y el símbolo ε para vacío.
    El símbolo inicial es el LHS de la primera producción.
    """
    G: Grammar = {}
    start: str = ""
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue
            if "->" not in line:
                raise ValueError(f"Línea inválida (falta '->'): {raw.strip()}")
            lhs, rhs = [x.strip() for x in line.split("->", 1)]
            if not start:
                start = lhs
            alts = [x.strip() for x in rhs.split("|")]
            prods: List[List[str]] = []
            for alt in alts:
                if alt == EPS or alt.lower() == "epsilon":
                    prods.append([EPS])
                else:
                    prods.append(_tokenize_rhs(alt))
            G.setdefault(lhs, []).extend(prods)
    if not start or not G:
        raise ValueError("Archivo de gramática vacío o inválido.")
    return start, G

def nonterminals(G: Grammar) -> List[str]:
    return list(G.keys())

def terminals(G: Grammar) -> List[str]:
    nts = set(G.keys())
    terms = set()
    for alts in G.values():
        for rhs in alts:
            for s in rhs:
                if s != EPS and s not in nts:
                    terms.add(s)
    return list(terms)
