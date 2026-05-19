#!/bin/bash

BASE="http://127.0.0.1:5000"

echo "======================================"
echo " TESTE AUTOMATIZADO - FLASK + TINYDB "
echo "======================================"

# ======================================
# 1) API ONLINE
# ======================================
echo ""
echo "1) TESTE - API ONLINE"
curl -s "$BASE/" | jq .

# ======================================
# 2) CRIAR USUÁRIOS
# ======================================
echo ""
echo "======================================"
echo "2) CRIANDO USUÁRIOS"
echo "======================================"

USER1=$(curl -s -X POST "$BASE/usuario" \
  -H "Content-Type: application/json" \
  -d '{"nome":"Ana","idade":20}')

echo "$USER1" | jq .

USER2=$(curl -s -X POST "$BASE/usuario" \
  -H "Content-Type: application/json" \
  -d '{"nome":"Bruno","idade":25}')

echo "$USER2" | jq .

# ======================================
# 3) LISTAR USUÁRIOS
# ======================================
echo ""
echo "======================================"
echo "3) LISTANDO USUÁRIOS"
echo "======================================"

curl -s "$BASE/usuarios" | jq .

# ======================================
# 4) BUSCAR USUÁRIO (pega id do primeiro)
# ======================================
echo ""
echo "======================================"
echo "4) BUSCAR USUÁRIO"
echo "======================================"

ID=$(curl -s "$BASE/usuarios" | jq -r '.[0]._id')

curl -s "$BASE/usuario/$ID" | jq .

# ======================================
# 5) UPDATE USUÁRIO
# ======================================
echo ""
echo "======================================"
echo "5) ATUALIZAR USUÁRIO"
echo "======================================"

curl -s -X PUT "$BASE/usuario/$ID" \
  -H "Content-Type: application/json" \
  -d '{"idade":99}' | jq .

# ======================================
# 6) DELETE USUÁRIO
# ======================================
echo ""
echo "======================================"
echo "6) DELETAR USUÁRIO"
echo "======================================"

curl -s -X DELETE "$BASE/usuario/$ID" | jq .

# ======================================
# 7) STRESS TEST
# ======================================
echo ""
echo "======================================"
echo "7) STRESS TEST - CRIAÇÃO EM MASSA"
echo "======================================"

for i in {1..5}
do
  curl -s -X POST "$BASE/usuario" \
    -H "Content-Type: application/json" \
    -d "{\"nome\":\"User$i\",\"idade\":$((20+i))}" > /dev/null

  echo "User$i criado"
done

# ======================================
# 8) LISTAGEM FINAL
# ======================================
echo ""
echo "======================================"
echo "8) LISTAGEM FINAL"
echo "======================================"

curl -s "$BASE/usuarios" | jq .

# ======================================
# 9) TESTE DE FILMES (seu CRUD web)
# ======================================
echo ""
echo "======================================"
echo "9) TESTE FILMES (POST FORM)"
echo "======================================"

curl -s -X POST "$BASE/" \
  -d "filme=Matrix&opiniao=Excelente" > /dev/null

echo "Filme inserido"

curl -s "$BASE/" | head -n 10

# ======================================
# 10) HEADERS DEBUG
# ======================================
echo ""
echo "======================================"
echo "10) HEADERS HTTP"
echo "======================================"

curl -I "$BASE/usuarios"

echo ""
echo "======================================"
echo " TESTES FINALIZADOS "
echo "======================================"
