
SELECT * FROM estudiante;

SELECT nombre, apellido FROM estudiante;

SELECT * FROM estudiante
WHERE departamento = 1;

SELECT * FROM estudiante
ORDER BY fecha_nacimiento ASC;

SELECT COUNT(*) AS total_estudiantes
FROM estudiante;

SELECT * FROM estudiante
WHERE apellido = 'Vargas';

SELECT * FROM estudiante
WHERE nombre LIKE 'A%';

SELECT estudiante.nombre, estudiante.apellido, departamento.nombre AS departamento
FROM estudiante
INNER JOIN departamento
ON estudiante.departamento = departamento.id;

SELECT estudiante.nombre, estudiante.apellido, AVG(calificacion.nota) AS promedio
FROM estudiante
INNER JOIN calificacion
ON estudiante.id = calificacion.estudiante
GROUP BY estudiante.id;

SELECT departamento.nombre AS departamento, COUNT(estudiante.id) AS total
FROM departamento
LEFT JOIN estudiante
ON departamento.id = estudiante.departamento
GROUP BY departamento.nombre;

SELECT profesor.nombre, profesor.apellido, curso.nombre AS curso
FROM profesor
INNER JOIN curso
ON profesor.id = curso.profesor;

SELECT estudiante.nombre, estudiante.apellido, AVG(calificacion.nota) AS promedio
FROM estudiante
INNER JOIN calificacion
ON estudiante.id = calificacion.estudiante
GROUP BY estudiante.id
HAVING promedio > 90;

SELECT estudiante.nombre, estudiante.apellido, AVG(calificacion.nota) AS promedio
FROM estudiante
INNER JOIN calificacion
ON estudiante.id = calificacion.estudiante
GROUP BY estudiante.id
ORDER BY promedio DESC
LIMIT 3;
