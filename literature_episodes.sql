-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: literature
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `episodes`
--

DROP TABLE IF EXISTS `episodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `episodes` (
  `idEpisodes` int NOT NULL,
  `ep_name` varchar(100) DEFAULT NULL,
  `meta` text,
  `created` datetime(6) DEFAULT NULL,
  `Series_idSeries` int NOT NULL,
  `ep_no` int DEFAULT NULL,
  PRIMARY KEY (`idEpisodes`),
  UNIQUE KEY `idEpisodes_UNIQUE` (`idEpisodes`),
  KEY `fk_Episodes_Series1_idx` (`Series_idSeries`),
  CONSTRAINT `fk_Episodes_Series1` FOREIGN KEY (`Series_idSeries`) REFERENCES `series` (`idSeries`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `episodes`
--

LOCK TABLES `episodes` WRITE;
/*!40000 ALTER TABLE `episodes` DISABLE KEYS */;
INSERT INTO `episodes` VALUES (1,'book1:1The one','Once in a town...','2022-08-02 20:58:28.000000',1,1),(2,'book1:2The one','Once in a town...','2022-08-02 20:58:28.000000',1,2),(3,'book1:3The one','Once in a town...','2022-08-02 20:58:28.000000',1,3),(4,'book1:4The one','Once in a town...','2022-08-02 20:58:28.000000',1,4),(5,'book1:5The one','Once in a town...','2022-08-02 20:58:28.000000',1,5),(6,'book1:6The one','Once in a town...','2022-08-02 20:58:28.000000',1,6),(7,'book1:7The one','Once in a town...','2022-08-02 20:58:28.000000',1,7),(21,'book2:1The one','Once in a town...','2022-08-04 20:58:28.000000',2,1),(22,'book2:2The one','Once in a town...','2022-08-04 20:58:28.000000',2,2),(23,'book2:3The one','Once in a town...','2022-08-04 20:58:28.000000',2,3),(24,'book2:4The one','Once in a town...','2022-08-04 20:58:28.000000',2,4),(25,'book2:5The one','Once in a town...','2022-08-04 20:58:28.000000',2,5),(26,'book2:6The one','Once in a town...','2022-08-04 20:58:28.000000',2,6),(31,'book3:1The one','Once in a town...','2022-12-08 20:58:28.000000',3,1),(32,'book3:2The one','Once in a town...','2022-12-08 20:58:28.000000',3,2),(33,'book3:3The one','Once in a town...','2022-12-08 20:58:28.000000',3,3),(34,'book3:4The one','Once in a town...','2022-12-08 20:58:28.000000',3,4),(35,'book4:5The one','Once in a town...','2022-12-08 20:58:28.000000',3,5);
/*!40000 ALTER TABLE `episodes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-20 18:32:30
