# -*- coding: utf-8 -*-
import argparse
from .grammar_io import load_grammar, terminals, nonterminals
from .first_follow import first_sets, follow_sets
from .predict import predict_sets
from .ll1_table import build_ll1_table
from .parser_ll1 import parse_file_ll1

def main():
    ap = argparse.ArgumentParser(description="Proyecto LL(1) – Presentación 6")
    ap.add_argument("--grammar", required=True, help="Ruta a la gramática (.g)")
    ap.add_argument("--first", action="store_true", help="Imprimir PRIMEROS")
    ap.add_argument("--follow", action="store_true", help="Imprimir SIGUIENTES")
    ap.add_argument("--predict", action="store_true", help="Imprimir PREDICCIÓN por producción")
    ap.add_argument("--table", action="store_true", help="Imprimir tabla LL(1) y conflictos")
    ap.add_argument("--parse", help="Archivo de entrada a parsear")
    ap.add_argument("-o", "--out", help="Guardar salida en archivo")
    args = ap.parse_args()

    start, G = load_grammar(args.grammar)

    out_lines = []
    if args.first or args.follow or args.predict or args.table:
        F = first_sets(G)
        Fo = follow_sets(G, start, F)
        if args.first:
            out_lines.append("== PRIMEROS ==")
            for A in G: out_lines.append(f"{A} : {sorted(F[A])}")
        if args.follow:
            out_lines.append("\n== SIGUIENTES ==")
            for A in G: out_lines.append(f"{A} : {sorted(Fo[A])}")
        if args.predict:
            out_lines.append("\n== PREDICCIÓN ==")
            _, _, P = predict_sets(G, start)
            for (A, rhs), terms in P.items():
                out_lines.append(f"{A} -> {' '.join(rhs)} : {sorted(terms)}")
        if args.table:
            out_lines.append("\n== Tabla LL(1) ==")
            table, conflicts = build_ll1_table(G, start)
            for (A,a), prods in sorted(table.items()):
                rhs_s = [" ".join(p) for p in prods]
                out_lines.append(f"[{A},{a}] -> {' / '.join(rhs_s)}")
            out_lines.append("\n" + ("✓ Sin conflictos LL(1)" if conflicts==0 else f"✗ Conflictos: {conflicts}"))

    if args.parse:
        ok, msg = parse_file_ll1(G, start, args.parse)
        out_lines.append(msg)

    text = "\n".join(out_lines) if out_lines else "Nada para hacer. Usa --first/--follow/--predict/--table/--parse."
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    else:
        print(text)

if __name__ == "__main__":
    main()
