-- Crear la base de datos si no existe y seleccionarla
CREATE DATABASE IF NOT EXISTS voluntame_db;
USE voluntame_db;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- ------------------------------------------------------
-- 1. Estructura de tabla: usuarios
-- ------------------------------------------------------
DROP TABLE IF EXISTS `voluntarios_misiones`;
DROP TABLE IF EXISTS `misiones`;
DROP TABLE IF EXISTS `usuarios`;

CREATE TABLE `usuarios` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `apellido` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `contrasena` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Datos de ejemplo: usuarios
LOCK TABLES `usuarios` WRITE;
INSERT INTO `usuarios` VALUES (1,'Dany','Hernandez','dannyahg@gmail.com','$2b$12$v1NDZPw.7pSKr7Qh.ojyBefEL4b5JjuBUiHToolH8zuLJKG0ZWkZq','2026-02-11 19:27:30','2026-02-11 19:27:30');
UNLOCK TABLES;

-- ------------------------------------------------------
-- 2. Estructura de tabla: misiones
-- ------------------------------------------------------
CREATE TABLE `misiones` (
  `id_mision` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `fecha` DATE NOT NULL,
  `voluntarios_necesarios` INT NOT NULL,
  `descripcion` TEXT NOT NULL,
  `usuario_id` INT NOT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mision`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `misiones_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Datos de ejemplo: misiones
LOCK TABLES `misiones` WRITE;
INSERT INTO `misiones` VALUES (2,'Limpieza de Liceo VVH','2026-02-23',15,'Necesitamos a voluntarios que nos ayuden a mejorar la limpieza del entorno escolar para recibirles',1,'2026-02-11 19:30:25','2026-02-11 19:30:25');
UNLOCK TABLES;

-- ------------------------------------------------------
-- 3. Estructura de tabla: voluntarios_misiones (Tabla intermedia)
-- ------------------------------------------------------
CREATE TABLE `voluntarios_misiones` (
  `usuario_id` INT NOT NULL,
  `mision_id` INT NOT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`usuario_id`,`mision_id`),
  KEY `mision_id` (`mision_id`),
  CONSTRAINT `voluntarios_misiones_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `voluntarios_misiones_ibfk_2` FOREIGN KEY (`mision_id`) REFERENCES `misiones` (`id_mision`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Datos de ejemplo: voluntarios_misiones
LOCK TABLES `voluntarios_misiones` WRITE;
INSERT INTO `voluntarios_misiones` VALUES (1,2,'2026-02-11 19:30:30');
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;