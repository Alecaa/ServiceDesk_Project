-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: servicedesk
-- ------------------------------------------------------
-- Server version	8.0.45

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

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area` (
  `id` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `descripcion` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `estado` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (1,'soporte tecnico','Soporte N1','Activo'),(2,'Administrativa','Area administrativa','Activo'),(3,'Consultoria','Consultoria contable','Activo'),(4,'N2','Soporte nivel 2','Activo'),(5,'N3','Soporte nivel 3','Activo');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo_empresa` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `razon_social` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `identificacion` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `contacto` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `correo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `estado` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo_empresa` (`codigo_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'EMP001','Empresa Demo SAS','900123456','Nuevo Contacto','nuevo@email.com','2026-03-20 21:18:03','Inactivo'),(3,'EMP0003','Empresa Test','900111222','Juan Perez','empresa@test.com','2026-03-25 14:32:04','Activo');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'super_admin'),(2,'admin'),(3,'tecnico'),(4,'cliente');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num_ticket` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `codigo_empresa` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_usr` int DEFAULT NULL,
  `id_tec` int DEFAULT NULL,
  `id_area` int DEFAULT NULL,
  `modulo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_caso` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci,
  `evidencia` text COLLATE utf8mb4_unicode_ci,
  `solucion` text COLLATE utf8mb4_unicode_ci,
  `estado` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prioridad` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `escalado` tinyint(1) DEFAULT NULL,
  `area_escalado_id` int DEFAULT NULL,
  `tec_escalado_id` int DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `codigo_empresa` (`codigo_empresa`),
  KEY `id_usr` (`id_usr`),
  KEY `id_tec` (`id_tec`),
  KEY `id_area` (`id_area`),
  KEY `area_escalado_id` (`area_escalado_id`),
  KEY `tec_escalado_id` (`tec_escalado_id`),
  CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`codigo_empresa`) REFERENCES `empresa` (`codigo_empresa`),
  CONSTRAINT `tickets_ibfk_2` FOREIGN KEY (`id_usr`) REFERENCES `users` (`id`),
  CONSTRAINT `tickets_ibfk_3` FOREIGN KEY (`id_tec`) REFERENCES `users` (`id`),
  CONSTRAINT `tickets_ibfk_4` FOREIGN KEY (`id_area`) REFERENCES `area` (`id`),
  CONSTRAINT `tickets_ibfk_5` FOREIGN KEY (`area_escalado_id`) REFERENCES `area` (`id`),
  CONSTRAINT `tickets_ibfk_6` FOREIGN KEY (`tec_escalado_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (2,'TKT-000002','EMP001',19,18,1,'Facturación','Error','No genera factura',NULL,'Se reinició el servidor y el servicio quedó operativo','Resuelto','Alta',1,4,18,'2026-03-25 15:27:19'),(3,'TKT-000003','EMP001',19,NULL,NULL,'Facturación','Inconsistencia','Saldos incorrectos',NULL,NULL,'Abierto','Alta',NULL,NULL,NULL,'2026-03-25 17:08:03');
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets_asignados`
--

DROP TABLE IF EXISTS `tickets_asignados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets_asignados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_tkt` int DEFAULT NULL,
  `id_tec` int DEFAULT NULL,
  `id_area` int DEFAULT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tkt` (`id_tkt`),
  KEY `id_tec` (`id_tec`),
  KEY `id_area` (`id_area`),
  CONSTRAINT `tickets_asignados_ibfk_1` FOREIGN KEY (`id_tkt`) REFERENCES `tickets` (`id`),
  CONSTRAINT `tickets_asignados_ibfk_2` FOREIGN KEY (`id_tec`) REFERENCES `users` (`id`),
  CONSTRAINT `tickets_asignados_ibfk_3` FOREIGN KEY (`id_area`) REFERENCES `area` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets_asignados`
--

LOCK TABLES `tickets_asignados` WRITE;
/*!40000 ALTER TABLE `tickets_asignados` DISABLE KEYS */;
/*!40000 ALTER TABLE `tickets_asignados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets_comentarios`
--

DROP TABLE IF EXISTS `tickets_comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets_comentarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_tkt` int DEFAULT NULL,
  `id_tec` int DEFAULT NULL,
  `comentario` text COLLATE utf8mb4_unicode_ci,
  `tipo` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tkt` (`id_tkt`),
  KEY `id_tec` (`id_tec`),
  CONSTRAINT `tickets_comentarios_ibfk_1` FOREIGN KEY (`id_tkt`) REFERENCES `tickets` (`id`),
  CONSTRAINT `tickets_comentarios_ibfk_2` FOREIGN KEY (`id_tec`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets_comentarios`
--

LOCK TABLES `tickets_comentarios` WRITE;
/*!40000 ALTER TABLE `tickets_comentarios` DISABLE KEYS */;
INSERT INTO `tickets_comentarios` VALUES (1,2,1,'Estamos revisando el caso','publico','2026-03-25 15:56:32'),(2,2,1,'Error identificado en backend','interno','2026-03-25 15:56:52'),(3,2,1,'Solución aplicada: Se reinició el servidor y el servicio quedó operativo','interno','2026-03-25 16:53:13');
/*!40000 ALTER TABLE `tickets_comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets_evidencias`
--

DROP TABLE IF EXISTS `tickets_evidencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets_evidencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_tkt` int DEFAULT NULL,
  `nombre_archivo` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ruta` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tkt` (`id_tkt`),
  CONSTRAINT `tickets_evidencias_ibfk_1` FOREIGN KEY (`id_tkt`) REFERENCES `tickets` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets_evidencias`
--

LOCK TABLES `tickets_evidencias` WRITE;
/*!40000 ALTER TABLE `tickets_evidencias` DISABLE KEYS */;
INSERT INTO `tickets_evidencias` VALUES (1,2,'PRUEBATICKET.png','uploads/PRUEBATICKET.png','image/png','2026-03-25 16:44:41'),(2,2,'PRUEBATICKET.png','uploads/PRUEBATICKET.png','image/png','2026-03-25 16:47:32');
/*!40000 ALTER TABLE `tickets_evidencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_empresa` int DEFAULT NULL,
  `id_rol` int DEFAULT NULL,
  `id_area` int DEFAULT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `contacto` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `correo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `estado` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_empresa` (`id_empresa`),
  KEY `id_rol` (`id_rol`),
  KEY `id_area` (`id_area`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`id_empresa`) REFERENCES `empresa` (`id`),
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`),
  CONSTRAINT `users_ibfk_3` FOREIGN KEY (`id_area`) REFERENCES `area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,NULL,1,NULL,'root','Admin Actualizado','$2b$12$LxB3MnT46cPe82MDLEfovOU3JoUlyWMCtRRlNuDAcT60/pOHcTDAi','3111111111','superadmin@test.com','2026-03-25 15:02:43','Activo'),(18,NULL,3,1,'spt_n1','Tecnico Soporte N1','$2b$12$Qx91MS7z4Akk.Dm3tmf3/.nzLocOGAiM4GhmjIW7sx.WdM/n7kkwO','3000000001','tecn1@test.com','2026-03-25 15:05:54','Activo'),(19,1,4,NULL,'cliente1','Cliente Demo','$2b$12$rGDNya09uHYOzWTXKWel/OyZltakgYzMG6JJObl2Ki24P2Uuiupc2','3000000002','cliente@test.com','2026-03-25 15:15:54','Activo');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'servicedesk'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-11 12:59:21
