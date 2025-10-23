#!/bin/bash
set -e
GRAM="grammars/ejemplo_p6.g"
FILE="examples/ok/expresion1.txt"

echo "== Benchmark (10 corridas) =="
total=0
for i in {1..10}; do
  start=$(date +%s%N)
  python3 -m src.main --grammar "$GRAM" --parse "$FILE" > /dev/null
  end=$(date +%s%N)
  dur=$((end-start))
  total=$((total+dur))
  echo "run $i: $((dur/1000000)) ms"
done
avg_ns=$((total/10))
echo "avg: $((avg_ns/1000000)) ms"
