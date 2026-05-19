#!/bin/bash

echo "======================================"
echo " RESET TOTAL - FLASK + TINYDB"
echo "======================================"

# ======================================
# 1) MATAR FLASK SE ESTIVER RODANDO
# ======================================
echo "[1/4] Parando processos Flask..."

pkill -f "python3 main.py" 2>/dev/null
pkill -f "flask" 2>/dev/null

echo "Flask finalizado (se estava rodando)."

# ======================================
# 2) RESET BANCO TINYDB
# ======================================
echo "[2/4] Resetando banco TinyDB..."

if [ -f "db.json" ]; then
    rm -f db.json
    echo "db.json removido"
else
    echo "db.json não encontrado (ok)"
fi

# ======================================
# 3) LIMPAR CACHE PYTHON
# ======================================
echo "[3/4] Limpando cache..."

find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

echo "Cache limpo"

# ======================================
# 4) LIMPAR LOGS
# ======================================
echo "[4/4] Limpando logs..."

rm -f flask.log 2>/dev/null

echo ""
echo "======================================"
echo " RESET COMPLETO FINALIZADO"
echo "======================================"
echo ""
echo "Agora rode novamente:"
echo "   python3 main.py"
echo ""
