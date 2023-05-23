-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: evan_jaques_info1a_164_2023

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS evan_jaques_info1a_164_2023;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS evan_jaques_info1a_164_2023;

-- Utilisation de cette base de donnée

USE evan_jaques_info1a_164_2023;
-- --------------------------------------------------------
-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour evan_jaques_info1a_164_2023
CREATE DATABASE IF NOT EXISTS `evan_jaques_info1a_164_2023` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `evan_jaques_info1a_164_2023`;

-- Listage de la structure de table evan_jaques_info1a_164_2023. t_enfants
CREATE TABLE IF NOT EXISTS `t_enfants` (
  `id_enfants` int NOT NULL AUTO_INCREMENT,
  `ENom` varchar(50) DEFAULT NULL,
  `EPrenom` varchar(50) DEFAULT NULL,
  `EDateNaissance` date DEFAULT NULL,
  `ESexe` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_enfants`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.t_enfants : 4 rows
/*!40000 ALTER TABLE `t_enfants` DISABLE KEYS */;
INSERT INTO `t_enfants` (`id_enfants`, `ENom`, `EPrenom`, `EDateNaissance`, `ESexe`) VALUES
	(1, 'Chomel', 'Joel', '2015-04-24', 'm'),
	(2, 'Voltaire', 'Arthur', '2017-06-14', 'm'),
	(3, 'Dupuis', 'Fabrice', '2014-02-03', 'm'),
	(4, 'Troille', 'Sophie', '2017-08-04', 'f');
/*!40000 ALTER TABLE `t_enfants` ENABLE KEYS */;

-- Listage de la structure de table evan_jaques_info1a_164_2023. t_factures
CREATE TABLE IF NOT EXISTS `t_factures` (
  `id_factures` int NOT NULL AUTO_INCREMENT,
  `FDate` date DEFAULT NULL,
  `FMontant` smallint DEFAULT '0',
  PRIMARY KEY (`id_factures`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.t_factures : 1 rows
/*!40000 ALTER TABLE `t_factures` DISABLE KEYS */;
INSERT INTO `t_factures` (`id_factures`, `FDate`, `FMontant`) VALUES
	(1, '2023-03-15', 120);
/*!40000 ALTER TABLE `t_factures` ENABLE KEYS */;

-- Listage de la structure de table evan_jaques_info1a_164_2023. t_mail
CREATE TABLE IF NOT EXISTS `t_mail` (
  `id_mail` int NOT NULL AUTO_INCREMENT,
  `MNomMail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_mail`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.t_mail : 3 rows
/*!40000 ALTER TABLE `t_mail` DISABLE KEYS */;
INSERT INTO `t_mail` (`id_mail`, `MNomMail`) VALUES
	(1, 'claudine.lebois@gmail.com'),
	(2, 'sam.kaien@gmail.com'),
	(3, 'max.delier@outlook.com');
/*!40000 ALTER TABLE `t_mail` ENABLE KEYS */;

-- Listage de la structure de table evan_jaques_info1a_164_2023. t_parents
CREATE TABLE IF NOT EXISTS `t_parents` (
  `id_parents` int NOT NULL AUTO_INCREMENT,
  `PNom` varchar(50) DEFAULT NULL,
  `PPrenom` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_parents`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.t_parents : 3 rows
/*!40000 ALTER TABLE `t_parents` DISABLE KEYS */;
INSERT INTO `t_parents` (`id_parents`, `PNom`, `PPrenom`) VALUES
	(1, 'Lebois', 'Claudine'),
	(2, 'Graf', 'Max'),
	(3, 'Delier', 'Sam');
/*!40000 ALTER TABLE `t_parents` ENABLE KEYS */;

-- Listage de la structure de table evan_jaques_info1a_164_2023. t_parents_avoir_mail
CREATE TABLE IF NOT EXISTS `t_parents_avoir_mail` (
  `id_parents_avoir_mail` int NOT NULL AUTO_INCREMENT,
  `fk_parents` int DEFAULT NULL,
  `fk_mail` int DEFAULT NULL,
  PRIMARY KEY (`id_parents_avoir_mail`) USING BTREE,
  KEY `FK_t_parents_avoir_mail_t_parents` (`fk_parents`),
  KEY `FK_t_parents_avoir_mail_t_mail` (`fk_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164_2023.t_parents_avoir_mail : ~0 rows (environ)
INSERT INTO `t_parents_avoir_mail` (`id_parents_avoir_mail`, `fk_parents`, `fk_mail`) VALUES
	(4, 1, 1);

-- Listage de la structure de table evan_jaques_info1a_164_2023. t_telephones
CREATE TABLE IF NOT EXISTS `t_telephones` (
  `id_telephones` int NOT NULL AUTO_INCREMENT,
  `TNumTel` int DEFAULT '0',
  `TIndicatif` int DEFAULT '0',
  PRIMARY KEY (`id_telephones`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.t_telephones : 1 rows
/*!40000 ALTER TABLE `t_telephones` DISABLE KEYS */;
INSERT INTO `t_telephones` (`id_telephones`, `TNumTel`, `TIndicatif`) VALUES
	(1, 798342342, 41);
/*!40000 ALTER TABLE `t_telephones` ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
