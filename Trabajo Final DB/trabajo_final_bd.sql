DROP DATABASE IF EXISTS gestion_academica;
create database gestion_academica;
use gestion_academica;
CREATE TABLE departamento(
id INT AUTO_INCREMENT PRIMARY KEY,
nombre varchar(100)
);

 CREATE TABLE estudiante (
    id INT AUTO_INCREMENT PRIMARY KEY,
 --   matricula VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    departamento INT,
    FOREIGN KEY (departamento) REFERENCES departamento(id)
);

CREATE TABLE profesor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL
 --   departamento INT,
 --   FOREIGN KEY (departamento) REFERENCES departamento(id)
);

CREATE TABLE curso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
 --   codigo VARCHAR(20) UNIQUE NOT NULL,
    profesor INT,
    FOREIGN KEY (profesor) REFERENCES profesor(id)
);

CREATE TABLE clase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    curso INT NOT NULL,
 --   profesor INT NOT NULL,
    fecha VARCHAR(20),
 --   horario VARCHAR(50),
    aula VARCHAR(20),
    FOREIGN KEY (curso) REFERENCES curso(id)
 --   FOREIGN KEY (profesor) REFERENCES profesor(id)
);

CREATE TABLE inscripcion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante INT NOT NULL,
    clase INT NOT NULL,
    fecha_inscripcion DATE,
    FOREIGN KEY (estudiante) REFERENCES estudiante(id),
    FOREIGN KEY (clase) REFERENCES clase(id)
);

CREATE TABLE calificacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante INT,
    clase INT,
  --  inscripcion INT NOT NULL,
    nota DECIMAL(5,2),
 --   observaciones TEXT,
    FOREIGN KEY (estudiante) REFERENCES estudiante(id),
    FOREIGN KEY (clase) REFERENCES clase(id)  
);

-- POBLANDO LAS TABLAS

INSERT INTO departamento (nombre) VALUES
('Informática'),
('Arquitectura'),
('Mercadeo');

INSERT INTO estudiante (nombre, apellido, fecha_nacimiento, departamento) VALUES
('Juan', 'Vargas', '2000-05-19', 2),
('Jose', 'Ramirez', '2003-04-10', 1),
('Sheila', 'Polanco', '2005-10-24', 3),
('Pedro', 'Perez', '2002-05-03', 1),
('Maria', 'Soliz', '2001-01-11', 3);

INSERT INTO profesor (nombre, apellido) VALUES
('Carlos', 'Fuentes'),
('Ezequias', 'Sans'),
('Jesus', 'Baez')
;

INSERT INTO curso (nombre, profesor) VALUES
('Algebra', 2),
('Fisica', 2),
('Base de datos', 1),
('Administracion', 3);

INSERT INTO clase (curso, fecha, aula) VALUES
(1, '2026-01-12', 'A1'),
(1, '2026-01-13', 'A1'),
(2, '2026-01-14', 'Lab1'),
(3, '2026-01-15', 'B2')
;

INSERT INTO inscripcion (estudiante, clase, fecha_inscripcion) VALUES
(1, 1, '2025-12-09'),
(1, 3, '2025-12-09'),
(2, 2, '2025-12-09'),
(3, 1, '2025-12-10'),
(4, 3, '2025-12-10'),
(5, 2, '2025-12-11')
;

INSERT INTO calificacion (estudiante, clase, nota) VALUES
(1, 1, 90),
(1, 3, 80),
(2, 2, 95),
(3, 1, 87),
(4, 3, 92),
(5, 2, 83)
;

