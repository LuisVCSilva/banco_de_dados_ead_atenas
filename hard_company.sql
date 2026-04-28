-- =====================================
-- RESET DO BANCO
-- =====================================
DROP DATABASE IF EXISTS hard_company;
CREATE DATABASE hard_company;
USE hard_company;

-- =====================================
-- DEPARTAMENTO
-- =====================================
CREATE TABLE Departamento (
  Dnumero INT UNSIGNED PRIMARY KEY,
  DNome VARCHAR(50) NOT NULL UNIQUE,
  Orcamento DECIMAL(12,2) CHECK (Orcamento >= 0)
);

-- =====================================
-- EMPREGADO (AUTO-RELACIONAMENTO)
-- =====================================
CREATE TABLE Empregado (
  NSS INT UNSIGNED PRIMARY KEY,
  Pnome VARCHAR(50) NOT NULL,
  Salario DECIMAL(10,2) NOT NULL,
  DNUM INT UNSIGNED,
  NSSSUPER INT UNSIGNED,

  FOREIGN KEY (DNUM) REFERENCES Departamento(Dnumero),
  FOREIGN KEY (NSSSUPER) REFERENCES Empregado(NSS)
);

-- =====================================
-- GERENCIA (HISTÓRICO)
-- =====================================
CREATE TABLE Gerencia (
  NSSGER INT UNSIGNED,
  DNUM INT UNSIGNED,
  DataInicio DATE,
  DataFim DATE,

  PRIMARY KEY (NSSGER, DNUM, DataInicio),

  FOREIGN KEY (NSSGER) REFERENCES Empregado(NSS),
  FOREIGN KEY (DNUM) REFERENCES Departamento(Dnumero)
);

-- =====================================
-- DEPENDENTE
-- =====================================
CREATE TABLE Dependente (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  NSSEMP INT UNSIGNED,
  NomeDependente VARCHAR(100),
  Parentesco VARCHAR(30),

  FOREIGN KEY (NSSEMP) REFERENCES Empregado(NSS)
);

-- =====================================
-- PROJETO
-- =====================================
CREATE TABLE Projeto (
  PNumero INT UNSIGNED PRIMARY KEY,
  PNome VARCHAR(100),
  DNO INT UNSIGNED,
  Orcamento DECIMAL(12,2), CHECK (Orcamento >= 0)

  FOREIGN KEY (DNO) REFERENCES Departamento(Dnumero)
);

-- =====================================
-- PAPEL
-- =====================================
CREATE TABLE Papel (
  ID INT PRIMARY KEY,
  Nome VARCHAR(50) UNIQUE
);

-- =====================================
-- RELACIONAMENTO TERNÁRIO
-- =====================================
CREATE TABLE Alocacao (
  NSSE INT UNSIGNED,
  PNO INT UNSIGNED,
  PapelID INT,
  Horas INT,

  PRIMARY KEY (NSSE, PNO, PapelID),

  FOREIGN KEY (NSSE) REFERENCES Empregado(NSS),
  FOREIGN KEY (PNO) REFERENCES Projeto(PNumero),
  FOREIGN KEY (PapelID) REFERENCES Papel(ID)
);

-- =====================================
-- FORNECEDOR
-- =====================================
CREATE TABLE Fornecedor (
  ID INT PRIMARY KEY,
  Nome VARCHAR(100)
);

-- =====================================
-- COMPRA
-- =====================================
CREATE TABLE Compra (
  ID INT PRIMARY KEY,
  ProjetoID INT UNSIGNED,
  FornecedorID INT,
  Responsavel INT UNSIGNED,
  Valor DECIMAL(10,2),

  FOREIGN KEY (ProjetoID) REFERENCES Projeto(PNumero),
  FOREIGN KEY (FornecedorID) REFERENCES Fornecedor(ID),
  FOREIGN KEY (Responsavel) REFERENCES Empregado(NSS)
);

-- =====================================
-- FILIAL
-- =====================================
CREATE TABLE Filial (
  ID INT PRIMARY KEY,
  Nome VARCHAR(50)
);

-- =====================================
-- EMPREGADO-FILIAL
-- =====================================
CREATE TABLE EmpregadoFilial (
  NSS INT UNSIGNED,
  FilialID INT,
  DataInicio DATE,

  PRIMARY KEY (NSS, FilialID),

  FOREIGN KEY (NSS) REFERENCES Empregado(NSS),
  FOREIGN KEY (FilialID) REFERENCES Filial(ID)
);

-- =====================================
-- TRIGGERS
-- =====================================

DELIMITER $$

CREATE TRIGGER trg_salario_before_insert
BEFORE INSERT ON Empregado
FOR EACH ROW
BEGIN
  IF NEW.Salario < 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Salário não pode ser negativo';
  END IF;
END$$

CREATE TRIGGER trg_salario_before_update
BEFORE UPDATE ON Empregado
FOR EACH ROW
BEGIN
  IF NEW.Salario < 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Salário não pode ser negativo';
  END IF;
END$$

CREATE TRIGGER trg_horas_alocacao
BEFORE INSERT ON Alocacao
FOR EACH ROW
BEGIN
  IF NEW.Horas < 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Horas não podem ser negativas';
  END IF;
END$$

CREATE TRIGGER trg_compra_valor
BEFORE INSERT ON Compra
FOR EACH ROW
BEGIN
  IF NEW.Valor < 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Valor da compra inválido';
  END IF;
END$$

CREATE TRIGGER trg_auto_supervisao
BEFORE INSERT ON Empregado
FOR EACH ROW
BEGIN
  IF NEW.NSS = NEW.NSSSUPER THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Empregado não pode supervisionar a si mesmo';
  END IF;
END$$

DELIMITER ;
