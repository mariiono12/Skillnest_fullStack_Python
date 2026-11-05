CREATE DATABASE IF NOT EXISTS esquema_seguidores;
USE esquema_seguidores;

-- Tabla Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(45) NOT NULL,
  apellido VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla Intermedia Seguidores (Auto-relación / Self Join)
CREATE TABLE IF NOT EXISTS seguidores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,  -- Usuario seguido
  seguidor_id INT NOT NULL, -- Usuario que sigue
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_seguidores_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  CONSTRAINT fk_seguidores_seguidor FOREIGN KEY (seguidor_id) REFERENCES usuarios(id),
  CONSTRAINT uq_usuario_seguidor UNIQUE (usuario_id, seguidor_id) -- BONUS: Evita duplicados en BD
);

-- Datos de prueba opcionales
INSERT INTO usuarios (nombre, apellido, email) VALUES
('Soraya', 'Montenegro', 'soraya@email.com'),
('Luis F.', 'de la Vega', 'luis@email.com'),
('Beatriz', 'Pinzón', 'beatriz@email.com'),
('Armando', 'Mendoza', 'armando@email.com'),
('Mia', 'Colucci', 'mia@email.com'),
('Roberta', 'Pardo', 'roberta@email.com');