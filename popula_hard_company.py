import mysql.connector
import random
from datetime import date, timedelta

# =========================
# CONEXÃO
# =========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hard_company"
)

cursor = conn.cursor()

# =========================
# DADOS BASE
# =========================
nomes = [
    "Ana", "Carlos", "Joao", "Maria", "Fernanda",
    "Lucas", "Juliana", "Rafael", "Patricia", "Bruno"
]

departamentos = ["TI", "RH", "Financeiro", "Marketing"]
papeis = ["Desenvolvedor", "Gerente", "Analista", "Tester"]
fornecedores = ["Dell", "Amazon", "Microsoft", "Google"]
filiais = ["SP", "RJ", "MG"]

# =========================
# INSERIR DEPARTAMENTOS
# =========================
for i, nome in enumerate(departamentos, start=1):
    cursor.execute(
        "INSERT INTO Departamento (Dnumero, DNome, Orcamento) VALUES (%s, %s, %s)",
        (i, nome, random.randint(50000, 200000))
    )

# =========================
# INSERIR EMPREGADOS
# =========================
empregados_ids = []

for i in range(1, 11):
    nome = random.choice(nomes)
    salario = round(random.uniform(2000, 8000), 2)
    dept = random.randint(1, len(departamentos))

    # supervisor: primeiros não têm, depois aponta para alguém anterior
    if i <= 2:
        supervisor = None
    else:
        supervisor = random.choice(empregados_ids)

    cursor.execute(
        "INSERT INTO Empregado (NSS, Pnome, Salario, DNUM, NSSSUPER) VALUES (%s, %s, %s, %s, %s)",
        (i, nome, salario, dept, supervisor)
    )

    empregados_ids.append(i)

# =========================
# PAPÉIS
# =========================
for i, nome in enumerate(papeis, start=1):
    cursor.execute(
        "INSERT INTO Papel (ID, Nome) VALUES (%s, %s)",
        (i, nome)
    )

# =========================
# PROJETOS
# =========================
for i in range(1, 6):
    cursor.execute(
        "INSERT INTO Projeto (PNumero, PNome, DNO, Orcamento) VALUES (%s, %s, %s, %s)",
        (
            i,
            f"Projeto {i}",
            random.randint(1, len(departamentos)),
            random.randint(10000, 50000)
        )
    )

# =========================
# ALOCAÇÃO (TERNÁRIO)
# =========================
for _ in range(20):
    cursor.execute(
        "INSERT IGNORE INTO Alocacao (NSSE, PNO, PapelID, Horas) VALUES (%s, %s, %s, %s)",
        (
            random.choice(empregados_ids),
            random.randint(1, 5),
            random.randint(1, len(papeis)),
            random.randint(10, 100)
        )
    )

# =========================
# FORNECEDORES
# =========================
for i, nome in enumerate(fornecedores, start=1):
    cursor.execute(
        "INSERT INTO Fornecedor (ID, Nome) VALUES (%s, %s)",
        (i, nome)
    )

# =========================
# COMPRAS
# =========================
for i in range(1, 11):
    cursor.execute(
        "INSERT INTO Compra (ID, ProjetoID, FornecedorID, Responsavel, Valor) VALUES (%s, %s, %s, %s, %s)",
        (
            i,
            random.randint(1, 5),
            random.randint(1, len(fornecedores)),
            random.choice(empregados_ids),
            round(random.uniform(1000, 10000), 2)
        )
    )

# =========================
# FILIAIS
# =========================
for i, nome in enumerate(filiais, start=1):
    cursor.execute(
        "INSERT INTO Filial (ID, Nome) VALUES (%s, %s)",
        (i, nome)
    )

# =========================
# EMPREGADO-FILIAL
# =========================
for _ in range(15):
    cursor.execute(
        "INSERT IGNORE INTO EmpregadoFilial (NSS, FilialID, DataInicio) VALUES (%s, %s, %s)",
        (
            random.choice(empregados_ids),
            random.randint(1, len(filiais)),
            date.today() - timedelta(days=random.randint(0, 1000))
        )
    )

# =========================
# COMMIT
# =========================
conn.commit()

print("Banco populado com sucesso!")

cursor.close()
conn.close()
