#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Pipeline completo: grava um demo e monta o video final.
# Edite as variaveis abaixo e rode: bash capture/run.sh
# ============================================================

# --- Configuracoes do demo ---
DEMO_CMD="uv run python python_pyxel/pyxel_002.py"
FRAMEWORK="pyxel"              # pyxel | pygame | py5 | turtle
DURATION=30                    # segundos de gravacao
KEYS="r"                       # teclas para iniciar (ex: r)
POSITION="100,50"             # onde colocar a janela (X,Y)

# --- Configuracoes do video ---
INTRO_TEXT="PYXEL_002"
OUTPUT_NAME="pyxel_002"

# --- Nao mexer abaixo ---
DEMO_FILE="${OUTPUT_NAME}_demo.mp4"
FINAL_FILE="${OUTPUT_NAME}.mp4"

echo "=== Etapa 1: Gravando demo ==="
uv run python capture/record.py \
  --demo "$DEMO_CMD" \
  --framework "$FRAMEWORK" \
  --duration "$DURATION" \
  --keys "$KEYS" \
  --position "$POSITION" \
  --output "$DEMO_FILE"

echo ""
echo "=== Etapa 2: Montando video final ==="
uv run python capture/assemble.py \
  --text "$INTRO_TEXT" \
  --demo "$DEMO_FILE" \
  --output "$FINAL_FILE"

echo ""
echo "=== Pronto! ==="
echo "Video final: $FINAL_FILE"
ls -lh "$FINAL_FILE"
