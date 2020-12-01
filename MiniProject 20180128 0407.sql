-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.59


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema srmudb
--

CREATE DATABASE IF NOT EXISTS srmudb;
USE srmudb;

--
-- Definition of table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `userName` varchar(45) NOT NULL,
  `userPass` varchar(45) DEFAULT NULL,
  `userType` varchar(45) DEFAULT NULL,
  `fullname` varchar(45) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` (`userName`,`userPass`,`userType`,`fullname`,`phone`,`email`,`status`) VALUES 
 ('A001','1234','admin','Archita Singh','7084840355','architasingh@gmail.com','activated'),
 ('H001','2456','admin','Himanshu Goswami','9506208596','goswamiashish845@gmail.com','activated'),
 ('P001','12345','monitor','Preeti Chauhan','7607256372','preetichauhan@gmail.com','activated'),
 ('V001','1234','monitor','Vaishali Singh','7985262422','vaishalisingh@gmail.com','deactivated');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;


--
-- Definition of table `modal`
--

DROP TABLE IF EXISTS `modal`;
CREATE TABLE `modal` (
  `modalId` varchar(45) NOT NULL,
  `modalName` varchar(45) NOT NULL,
  `Price` float NOT NULL,
  PRIMARY KEY (`modalId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `modal`
--

/*!40000 ALTER TABLE `modal` DISABLE KEYS */;
INSERT INTO `modal` (`modalId`,`modalName`,`Price`) VALUES 
 ('AUDIR2018','2018 Audi R8',12373600),
 ('BENZSL02017','2017 Mercedes-Benz SL-Class',13993500),
 ('BUGATTI2015','2015 Bugatti Veyron',123456000),
 ('DODGEV2107','2017 Dodge Viper',7561300),
 ('JAGUAR2018','2018 Jaguar F-Type',7956250),
 ('LAMBOA2017','2017 Lamborghini Aventador',52234600),
 ('LAMBOH2017','2017 Lamborghini Huracan',39729900),
 ('LEXLC002018','2018 Lexus LC',6142860),
 ('NISSANG2018','2018 Nissan GT-R',11169900),
 ('PORSBO2018','2018 Porsche Boxster',4442770);
/*!40000 ALTER TABLE `modal` ENABLE KEYS */;


--
-- Definition of table `prospect`
--

DROP TABLE IF EXISTS `prospect`;
CREATE TABLE `prospect` (
  `prospID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `prospName` varchar(45) NOT NULL,
  `prospPhone` varchar(45) NOT NULL,
  `prospAddress` varchar(45) NOT NULL,
  `interestedModel` varchar(45) NOT NULL,
  `interestedColour` varchar(45) NOT NULL,
  `date_of_visit` datetime NOT NULL,
  `hotness` varchar(45) NOT NULL,
  PRIMARY KEY (`prospID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prospect`
--

/*!40000 ALTER TABLE `prospect` DISABLE KEYS */;
INSERT INTO `prospect` (`prospID`,`prospName`,`prospPhone`,`prospAddress`,`interestedModel`,`interestedColour`,`date_of_visit`,`hotness`) VALUES 
 (1,'Himanshu Goswami','9506208499','L-721 HIndalco, colony','LAMBOAVEN2017','Black','2018-01-23 11:40:22','hot'),
 (2,'Shobhit Goswami','9519268222','P-29 Barabanki,Lucknow','BUGATTI2015','White','2018-01-11 11:23:33','warm');
/*!40000 ALTER TABLE `prospect` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
