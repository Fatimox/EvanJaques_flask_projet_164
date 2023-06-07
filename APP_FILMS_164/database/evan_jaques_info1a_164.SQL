-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: evan_jaques_info1a_164

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS evan_jaques_info1a_164;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS evan_jaques_info1a_164;

-- Utilisation de cette base de donnée

USE evan_jaques_info1a_164;
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


-- Listage de la structure de la base pour evan_jaques_info1a_164
DROP DATABASE IF EXISTS `evan_jaques_info1a_164`;
CREATE DATABASE IF NOT EXISTS `evan_jaques_info1a_164` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `evan_jaques_info1a_164`;

-- Listage de la structure de table evan_jaques_info1a_164. t_adresse
DROP TABLE IF EXISTS `t_adresse`;
CREATE TABLE IF NOT EXISTS `t_adresse` (
  `id_adresse` int NOT NULL AUTO_INCREMENT,
  `NomRue` varchar(50) DEFAULT NULL,
  `NumeroRue` int DEFAULT NULL,
  `Ville` varchar(50) DEFAULT NULL,
  `Npa` int DEFAULT NULL,
  PRIMARY KEY (`id_adresse`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_adresse : ~3 rows (environ)
INSERT INTO `t_adresse` (`id_adresse`, `NomRue`, `NumeroRue`, `Ville`, `Npa`) VALUES
	(1, 'Avenue du papillon', 10, 'Geneve', 1090),
	(2, 'Route de la joie', 2, 'Morge', 1232),
	(3, 'Rue des ballons', 43, 'Villneuve', 1423);

-- Listage de la structure de table evan_jaques_info1a_164. t_cours
DROP TABLE IF EXISTS `t_cours`;
CREATE TABLE IF NOT EXISTS `t_cours` (
  `id_cours` int NOT NULL AUTO_INCREMENT,
  `Cours1` varchar(50) DEFAULT NULL,
  `Cours2` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_cours`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_cours : ~0 rows (environ)

-- Listage de la structure de table evan_jaques_info1a_164. t_enfants
DROP TABLE IF EXISTS `t_enfants`;
CREATE TABLE IF NOT EXISTS `t_enfants` (
  `id_enfants` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(50) DEFAULT NULL,
  `Prenom` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `DateNaissance` date DEFAULT NULL,
  PRIMARY KEY (`id_enfants`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_enfants : ~3 rows (environ)
INSERT INTO `t_enfants` (`id_enfants`, `Nom`, `Prenom`, `DateNaissance`) VALUES
	(1, 'Graf', 'Victor', '2022-12-28'),
	(2, 'Jaques', 'Evan', '2023-05-27'),
	(3, 'Salin', 'Joel', '2022-11-17');

-- Listage de la structure de table evan_jaques_info1a_164. t_enfants_cours
DROP TABLE IF EXISTS `t_enfants_cours`;
CREATE TABLE IF NOT EXISTS `t_enfants_cours` (
  `id_enfants_cours` int NOT NULL AUTO_INCREMENT,
  `fk_enfants` int DEFAULT NULL,
  `fk_cours` int DEFAULT NULL,
  PRIMARY KEY (`id_enfants_cours`),
  KEY `FK_t_enfants_cours_t_enfants` (`fk_enfants`),
  KEY `FK_t_enfants_cours_t_cours` (`fk_cours`),
  CONSTRAINT `FK_t_enfants_cours_t_cours` FOREIGN KEY (`fk_cours`) REFERENCES `t_cours` (`id_cours`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_enfants_cours_t_enfants` FOREIGN KEY (`fk_enfants`) REFERENCES `t_enfants` (`id_enfants`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_enfants_cours : ~0 rows (environ)

-- Listage de la structure de table evan_jaques_info1a_164. t_enfants_sante
DROP TABLE IF EXISTS `t_enfants_sante`;
CREATE TABLE IF NOT EXISTS `t_enfants_sante` (
  `id_enfants_sante` int NOT NULL AUTO_INCREMENT,
  `fk_enfants` int DEFAULT NULL,
  `fk_sante` int DEFAULT NULL,
  PRIMARY KEY (`id_enfants_sante`),
  KEY `FK_t_enfants_sante_t_enfants` (`fk_enfants`),
  KEY `FK_t_enfants_sante_t_sante` (`fk_sante`),
  CONSTRAINT `FK_t_enfants_sante_t_enfants` FOREIGN KEY (`fk_enfants`) REFERENCES `t_enfants` (`id_enfants`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_enfants_sante_t_sante` FOREIGN KEY (`fk_sante`) REFERENCES `t_sante` (`id_sante`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_enfants_sante : ~3 rows (environ)
INSERT INTO `t_enfants_sante` (`id_enfants_sante`, `fk_enfants`, `fk_sante`) VALUES
	(15, 2, 2),
	(22, 3, 1),
	(23, 1, 1);

-- Listage de la structure de table evan_jaques_info1a_164. t_factures
DROP TABLE IF EXISTS `t_factures`;
CREATE TABLE IF NOT EXISTS `t_factures` (
  `id_factures` int NOT NULL AUTO_INCREMENT,
  `Montant` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`id_factures`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_factures : ~1 rows (environ)
INSERT INTO `t_factures` (`id_factures`, `Montant`, `Date`) VALUES
	(1, 120, '2023-05-31');

-- Listage de la structure de table evan_jaques_info1a_164. t_mail
DROP TABLE IF EXISTS `t_mail`;
CREATE TABLE IF NOT EXISTS `t_mail` (
  `id_mail` int NOT NULL AUTO_INCREMENT,
  `NomMail` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_mail : ~2 rows (environ)
INSERT INTO `t_mail` (`id_mail`, `NomMail`) VALUES
	(1, 'claudine.labuche@gmail.com'),
	(2, 'samuel.graf@outlook.com');

-- Listage de la structure de table evan_jaques_info1a_164. t_parents
DROP TABLE IF EXISTS `t_parents`;
CREATE TABLE IF NOT EXISTS `t_parents` (
  `id_parents` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(50) DEFAULT NULL,
  `Prenom` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_parents`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_parents : ~5 rows (environ)
INSERT INTO `t_parents` (`id_parents`, `Nom`, `Prenom`) VALUES
	(1, 'Labuche', 'Claudine'),
	(2, 'Graf', 'Samuel'),
	(3, 'Feria', 'Daniel'),
	(4, 'Voles', 'Fabio'),
	(5, 'Legrand', 'Maxime');

-- Listage de la structure de table evan_jaques_info1a_164. t_parents_adresse
DROP TABLE IF EXISTS `t_parents_adresse`;
CREATE TABLE IF NOT EXISTS `t_parents_adresse` (
  `id_parents_adresse` int NOT NULL AUTO_INCREMENT,
  `fk_parents` int DEFAULT NULL,
  `fk_adresse` int DEFAULT NULL,
  PRIMARY KEY (`id_parents_adresse`),
  KEY `FK_t_parents_adresse_t_parents` (`fk_parents`),
  KEY `FK_t_parents_adresse_t_adresse` (`fk_adresse`),
  CONSTRAINT `FK_t_parents_adresse_t_adresse` FOREIGN KEY (`fk_adresse`) REFERENCES `t_adresse` (`id_adresse`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_parents_adresse_t_parents` FOREIGN KEY (`fk_parents`) REFERENCES `t_parents` (`id_parents`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_parents_adresse : ~3 rows (environ)
INSERT INTO `t_parents_adresse` (`id_parents_adresse`, `fk_parents`, `fk_adresse`) VALUES
	(1, 2, 1),
	(2, 5, 3),
	(3, 1, 2);

-- Listage de la structure de table evan_jaques_info1a_164. t_parents_factures
DROP TABLE IF EXISTS `t_parents_factures`;
CREATE TABLE IF NOT EXISTS `t_parents_factures` (
  `id_parents_factures` int NOT NULL AUTO_INCREMENT,
  `fk_parents` int DEFAULT NULL,
  `fk_factures` int DEFAULT NULL,
  PRIMARY KEY (`id_parents_factures`),
  KEY `FK_t_parents_factures_t_parents` (`fk_parents`),
  KEY `FK_t_parents_factures_t_factures` (`fk_factures`),
  CONSTRAINT `FK_t_parents_factures_t_factures` FOREIGN KEY (`fk_factures`) REFERENCES `t_factures` (`id_factures`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_parents_factures_t_parents` FOREIGN KEY (`fk_parents`) REFERENCES `t_parents` (`id_parents`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_parents_factures : ~1 rows (environ)
INSERT INTO `t_parents_factures` (`id_parents_factures`, `fk_parents`, `fk_factures`) VALUES
	(1, 1, 1);

-- Listage de la structure de table evan_jaques_info1a_164. t_parents_mail
DROP TABLE IF EXISTS `t_parents_mail`;
CREATE TABLE IF NOT EXISTS `t_parents_mail` (
  `id_parents_mail` int NOT NULL AUTO_INCREMENT,
  `fk_parents` int DEFAULT NULL,
  `fk_mail` int DEFAULT NULL,
  PRIMARY KEY (`id_parents_mail`),
  KEY `FK_t_parents_mail_t_parents` (`fk_parents`),
  KEY `FK_t_parents_mail_t_mail` (`fk_mail`),
  CONSTRAINT `FK_t_parents_mail_t_mail` FOREIGN KEY (`fk_mail`) REFERENCES `t_mail` (`id_mail`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_parents_mail_t_parents` FOREIGN KEY (`fk_parents`) REFERENCES `t_parents` (`id_parents`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_parents_mail : ~2 rows (environ)
INSERT INTO `t_parents_mail` (`id_parents_mail`, `fk_parents`, `fk_mail`) VALUES
	(1, 1, 1),
	(2, 2, 2);

-- Listage de la structure de table evan_jaques_info1a_164. t_parents_telephone
DROP TABLE IF EXISTS `t_parents_telephone`;
CREATE TABLE IF NOT EXISTS `t_parents_telephone` (
  `id_parents_telephone` int NOT NULL AUTO_INCREMENT,
  `fk_parents` int DEFAULT NULL,
  `fk_telephone` int DEFAULT NULL,
  PRIMARY KEY (`id_parents_telephone`),
  KEY `FK_t_parents_telephone_t_parents` (`fk_parents`),
  KEY `FK_t_parents_telephone_t_telephone` (`fk_telephone`),
  CONSTRAINT `FK_t_parents_telephone_t_parents` FOREIGN KEY (`fk_parents`) REFERENCES `t_parents` (`id_parents`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_parents_telephone_t_telephone` FOREIGN KEY (`fk_telephone`) REFERENCES `t_telephone` (`id_telephone`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_parents_telephone : ~3 rows (environ)
INSERT INTO `t_parents_telephone` (`id_parents_telephone`, `fk_parents`, `fk_telephone`) VALUES
	(1, 1, 3),
	(2, 2, 1),
	(3, 3, 2);

-- Listage de la structure de table evan_jaques_info1a_164. t_sante
DROP TABLE IF EXISTS `t_sante`;
CREATE TABLE IF NOT EXISTS `t_sante` (
  `id_sante` int NOT NULL AUTO_INCREMENT,
  `Allergie` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_sante`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_sante : ~3 rows (environ)
INSERT INTO `t_sante` (`id_sante`, `Allergie`) VALUES
	(1, 'Rhume des foins'),
	(2, 'Asthme'),
	(3, 'Accariens');

-- Listage de la structure de table evan_jaques_info1a_164. t_telephone
DROP TABLE IF EXISTS `t_telephone`;
CREATE TABLE IF NOT EXISTS `t_telephone` (
  `id_telephone` int NOT NULL AUTO_INCREMENT,
  `NumTel` varchar(50) DEFAULT NULL,
  `Indicatif` int DEFAULT NULL,
  PRIMARY KEY (`id_telephone`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table evan_jaques_info1a_164.t_telephone : ~4 rows (environ)
INSERT INTO `t_telephone` (`id_telephone`, `NumTel`, `Indicatif`) VALUES
	(1, '0798237277', 41),
	(2, '0785543216', 41),
	(3, '0779812301', NULL),
	(4, '0793039299', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
