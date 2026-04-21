CREATE DATABASE IF NOT EXISTS gestioneordini;
USE gestioneordini;

CREATE TABLE Clienti (
    id       INT          NOT NULL AUTO_INCREMENT,
    nome     VARCHAR(100) NOT NULL,
    città    VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Ordini (
    id          INT            NOT NULL AUTO_INCREMENT,
    id_cliente  INT            NOT NULL,
    data_ordine DATE           NOT NULL,
    importo     DECIMAL(7, 2)  NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_ordini_clienti
        FOREIGN KEY (id_cliente) REFERENCES Clienti(id)
);