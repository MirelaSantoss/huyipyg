--criar um banco de dados
CREATE DATABASE BDALUNOCURSO -- NOME DO BANCO DE DADOS

--ATIVAR O BANCO PARA USO

GO
USE BDALUNOCURSO

--CRIAR AS TABELAS                     --dontpad.com/fvl
CREATE TABLE CURSO                             
(--INICIO
    codcurso INT,
    nome varchar (100),
    primary key(codcurso)

) --FINAL

CREATE TABLE ALUNO

(-- INICIO

    prontuario varchar(9), --termina em virgula
    nome varchar(50), 
     codcurso INT,
    --criação das chaves
    primary key(prontuario),
    foreign key (codcurso) REFERENCES curso(codcurso)


) -- FINAL

--INSERIR DADOS
--INSERT INTO <NOME DA TABELA> (COLUNO1, COLUNA2, COLUNA..)
--VALUES
--VALORES NA SEQUENCIA

INSERT INTO CURSO (codcurso, nome)
VALUES
(1, 'Técnico de Sistemas')

--inserir varios cursos
INSERT INTO CURSO (codcurso, nome)
VALUES
(2, 'Técnologo em ADS'), 
(3, 'Bacharelado em SI'),
(4, 'Pós em gestão de TI')

--verificar a table curso

SELECT * --retorna todas as colunas
FROM CURSO --NOME DA TABELA

--INSERIR DADOS DA TABELA ALUNO

INSERT INTO ALUNO 
VALUES(11, 'MIRELA TOPZEIRA', 1), 
(44, 'LORENA ZÉ NOINHA DIVA', 2),
(33, 'DAIKI CHEIRA BUNDA', 3)

--CADASTRANDO UM CURSO INVALIDO
SELECT *FROM ALUNO

