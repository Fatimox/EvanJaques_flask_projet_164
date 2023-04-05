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
-- Hôte :                        127.0.0.1
-- Version du serveur:           5.1.72-community - MySQL Community Server (GPL)
-- SE du serveur:                Win32
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Listage de la structure de la base pour evan_jaques_info1a_164_2023
CREATE DATABASE IF NOT EXISTS `evan_jaques_info1a_164_2023` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `evan_jaques_info1a_164_2023`;

-- Listage de la structure de la table evan_jaques_info1a_164_2023. enfants
CREATE TABLE IF NOT EXISTS `enfants` (
  `ENo` int(11) NOT NULL AUTO_INCREMENT,
  `ENom` varchar(50) DEFAULT NULL,
  `EPrenom` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ENo`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.enfants : 1 rows
/*!40000 ALTER TABLE `enfants` DISABLE KEYS */;
INSERT INTO `enfants` (`ENo`, `ENom`, `EPrenom`) VALUES
	(1, 'Frederic', 'Lebois');
/*!40000 ALTER TABLE `enfants` ENABLE KEYS */;

-- Listage de la structure de la table evan_jaques_info1a_164_2023. factures
CREATE TABLE IF NOT EXISTS `factures` (
  `FNo` int(11) NOT NULL AUTO_INCREMENT,
  `FDate` date DEFAULT NULL,
  `FMontant` smallint(6) DEFAULT '0',
  PRIMARY KEY (`FNo`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.factures : 1 rows
/*!40000 ALTER TABLE `factures` DISABLE KEYS */;
INSERT INTO `factures` (`FNo`, `FDate`, `FMontant`) VALUES
	(1, '2023-03-15', 120);
/*!40000 ALTER TABLE `factures` ENABLE KEYS */;

-- Listage de la structure de la table evan_jaques_info1a_164_2023. mail
CREATE TABLE IF NOT EXISTS `mail` (
  `MNo` int(11) NOT NULL AUTO_INCREMENT,
  `MNomMail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MNo`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.mail : 1 rows
/*!40000 ALTER TABLE `mail` DISABLE KEYS */;
INSERT INTO `mail` (`MNo`, `MNomMail`) VALUES
	(1, 'claudine.lebois@gmail.com');
/*!40000 ALTER TABLE `mail` ENABLE KEYS */;

-- Listage de la structure de la table evan_jaques_info1a_164_2023. parents
CREATE TABLE IF NOT EXISTS `parents` (
  `PNo` int(11) NOT NULL AUTO_INCREMENT,
  `PNom` varchar(50) DEFAULT NULL,
  `PPrenom` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`PNo`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.parents : 1 rows
/*!40000 ALTER TABLE `parents` DISABLE KEYS */;
INSERT INTO `parents` (`PNo`, `PNom`, `PPrenom`) VALUES
	(1, 'Lebois', 'Claudine');
/*!40000 ALTER TABLE `parents` ENABLE KEYS */;

-- Listage de la structure de la table evan_jaques_info1a_164_2023. telephones
CREATE TABLE IF NOT EXISTS `telephones` (
  `TNo` int(11) NOT NULL AUTO_INCREMENT,
  `TNumTel` int(11) DEFAULT '0',
  `TIndicatif` int(11) DEFAULT '0',
  PRIMARY KEY (`TNo`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Listage des données de la table evan_jaques_info1a_164_2023.telephones : 1 rows
/*!40000 ALTER TABLE `telephones` DISABLE KEYS */;
INSERT INTO `telephones` (`TNo`, `TNumTel`, `TIndicatif`) VALUES
	(1, 798342342, 41);
/*!40000 ALTER TABLE `telephones` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
