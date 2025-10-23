#!/bin/bash
set -e

GRAM="grammars/ejemplo_p6.g"

echo "== PRUEBAS OK =="
for f in examples/ok/*.txt; do
  echo "[OK] $f"
  python3 -m src.main --grammar "$GRAM" --parse "$f"
done

echo "== PRUEBAS BAD =="
for f in examples/bad/*.txt; do
  echo "[BAD] $f"
  # si acepta un inválido, avisamos
  if python3 -m src.main --grammar "$GRAM" --parse "$f" | grep -q "exitosamente"; then
    echo "❌ ACEPTÓ INVÁLIDO: $f"
  else
    echo "✅ Rechazado correctamente"
  fi
done
