-- MySQL dump 10.13  Distrib 5.7.40, for osx10.16 (x86_64)
--
-- Host: localhost    Database: payhere
-- ------------------------------------------------------
-- Server version	5.7.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounthistory`
--

DROP TABLE IF EXISTS `accounthistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounthistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `detail_expense` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounthistory_user_id_bf72237a_fk_users_id` (`user_id`),
  CONSTRAINT `accounthistory_user_id_bf72237a_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounthistory`
--

LOCK TABLES `accounthistory` WRITE;
/*!40000 ALTER TABLE `accounthistory` DISABLE KEYS */;
INSERT INTO `accounthistory` VALUES (2,'2022-12-22',10000,'2022-12-22 15:02:41.138265','2022-12-22 15:02:41.138277',1),(3,'2022-12-22',10000,'2022-12-22 15:02:44.836362','2022-12-22 15:02:44.836375',1),(4,'2022-12-24',10000,'2022-12-22 15:02:54.360749','2022-12-22 15:02:54.360761',1),(5,'2022-12-30',10000,'2022-12-22 15:03:02.927391','2022-12-22 15:03:02.927404',1),(6,'2022-11-30',20000,'2022-12-22 15:41:49.832236','2022-12-22 15:41:49.832252',3),(7,'2022-12-01',20000,'2022-12-22 15:42:21.092499','2022-12-22 15:42:21.092512',3),(8,'2022-12-01',20000,'2022-12-22 15:42:23.787637','2022-12-22 15:42:23.787652',3),(9,'2022-12-01',20000,'2022-12-22 15:42:24.275907','2022-12-22 15:42:24.275922',3),(10,'2022-12-01',20000,'2022-12-22 15:42:24.998013','2022-12-22 15:42:24.998029',3),(11,'2022-12-10',20000,'2022-12-22 15:42:29.096588','2022-12-22 15:42:29.096603',3),(12,'2022-12-10',20000,'2022-12-22 15:42:29.430886','2022-12-22 15:42:29.430902',3),(13,'2022-12-10',20000,'2022-12-22 15:42:30.314678','2022-12-22 15:42:30.314693',3),(14,'2022-12-10',20000,'2022-12-22 15:42:31.039647','2022-12-22 15:42:31.039661',3),(15,'2022-12-25',50000,'2022-12-22 15:46:52.720124','2022-12-22 15:46:52.720139',3),(16,'2022-12-25',50000,'2022-12-22 15:46:53.775365','2022-12-22 15:46:53.775383',3),(17,'2022-12-15',50000,'2022-12-22 15:46:59.776338','2022-12-22 15:46:59.776353',3),(18,'2022-12-15',50000,'2022-12-22 15:47:00.288381','2022-12-22 15:47:00.288404',3),(19,'2022-12-16',50000,'2022-12-22 15:47:04.181476','2022-12-22 15:47:04.181493',3),(20,'2022-12-16',50000,'2022-12-22 15:47:04.636921','2022-12-22 15:47:04.636936',3),(21,'2022-12-16',50000,'2022-12-22 15:47:05.152476','2022-12-22 15:47:05.152490',3),(22,'2021-12-01',50000,'2022-12-22 15:47:32.404238','2022-12-22 15:47:32.404253',3),(23,'2021-12-01',50000,'2022-12-22 15:47:40.689325','2022-12-22 15:47:40.689339',4),(24,'2021-12-01',50000,'2022-12-22 15:47:41.316238','2022-12-22 15:47:41.316256',4),(25,'2021-12-06',50000,'2022-12-22 15:47:45.609289','2022-12-22 15:47:45.609304',4),(26,'2021-12-06',20000,'2022-12-22 15:47:50.881488','2022-12-22 15:47:50.881503',4),(27,'2021-12-06',20000,'2022-12-22 15:47:52.470503','2022-12-22 15:47:52.470517',4),(28,'2021-12-25',500000000,'2022-12-22 15:48:11.059180','2022-12-22 15:48:11.059195',5),(29,'2021-12-31',500000000,'2022-12-22 15:48:16.522723','2022-12-22 15:48:16.522737',5),(30,'2021-12-31',500000000,'2022-12-22 15:48:20.385236','2022-12-22 15:48:20.385250',5);
/*!40000 ALTER TABLE `accounthistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (4,'account','accounthistory'),(5,'account','memo'),(1,'contenttypes','contenttype'),(2,'sessions','session'),(6,'shorturl','shorturl'),(3,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'user','0001_initial','2022-12-22 14:35:11.493608'),(2,'account','0001_initial','2022-12-22 14:35:11.562649'),(3,'contenttypes','0001_initial','2022-12-22 14:35:11.674594'),(4,'contenttypes','0002_remove_content_type_name','2022-12-22 14:35:11.737490'),(5,'sessions','0001_initial','2022-12-22 14:35:11.768201'),(6,'shorturl','0001_initial','2022-12-22 14:35:11.828516'),(7,'user','0002_auto_20221221_0053','2022-12-22 14:35:11.831877'),(8,'user','0003_auto_20221221_0058','2022-12-22 14:35:11.835127');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memo`
--

DROP TABLE IF EXISTS `memo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `memo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `expense_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `memo_expense_id_de769faa_fk_accounthistory_id` (`expense_id`),
  CONSTRAINT `memo_expense_id_de769faa_fk_accounthistory_id` FOREIGN KEY (`expense_id`) REFERENCES `accounthistory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memo`
--

LOCK TABLES `memo` WRITE;
/*!40000 ALTER TABLE `memo` DISABLE KEYS */;
INSERT INTO `memo` VALUES (2,'test2','2022-12-22 15:02:41.139229','2022-12-22 15:02:41.139241',2),(3,'test3','2022-12-22 15:02:44.837259','2022-12-22 15:02:44.837271',3),(4,'test4','2022-12-22 15:02:54.361614','2022-12-22 15:02:54.361624',4),(5,'test5','2022-12-22 15:03:02.928062','2022-12-22 15:03:02.928074',5),(6,'fortest','2022-12-22 15:41:49.833327','2022-12-22 15:41:49.833342',6),(7,'fortest','2022-12-22 15:42:21.093463','2022-12-22 15:42:21.093479',7),(8,'fortest','2022-12-22 15:42:23.788583','2022-12-22 15:42:23.788596',8),(9,'fortest','2022-12-22 15:42:24.276862','2022-12-22 15:42:24.276876',9),(10,'fortest','2022-12-22 15:42:24.999026','2022-12-22 15:42:24.999041',10),(11,'fortest','2022-12-22 15:42:29.097562','2022-12-22 15:42:29.097579',11),(12,'fortest','2022-12-22 15:42:29.431914','2022-12-22 15:42:29.431931',12),(13,'fortest','2022-12-22 15:42:30.315641','2022-12-22 15:42:30.315654',13),(14,'fortest','2022-12-22 15:42:31.040538','2022-12-22 15:42:31.040551',14),(15,'fortest','2022-12-22 15:46:52.721184','2022-12-22 15:46:52.721201',15),(16,'fortest','2022-12-22 15:46:53.776750','2022-12-22 15:46:53.776771',16),(17,'fortest','2022-12-22 15:46:59.777470','2022-12-22 15:46:59.777490',17),(18,'fortest','2022-12-22 15:47:00.289697','2022-12-22 15:47:00.289721',18),(19,'fortest','2022-12-22 15:47:04.182523','2022-12-22 15:47:04.182543',19),(20,'fortest','2022-12-22 15:47:04.638014','2022-12-22 15:47:04.638031',20),(21,'fortest','2022-12-22 15:47:05.153390','2022-12-22 15:47:05.153403',21),(22,'fortest','2022-12-22 15:47:32.405345','2022-12-22 15:47:32.405366',22),(23,'fortest','2022-12-22 15:47:40.690342','2022-12-22 15:47:40.690356',23),(24,'fortest','2022-12-22 15:47:41.317547','2022-12-22 15:47:41.317567',24),(25,'fortest','2022-12-22 15:47:45.610279','2022-12-22 15:47:45.610293',25),(26,'fortest','2022-12-22 15:47:50.882447','2022-12-22 15:47:50.882462',26),(27,'fortest','2022-12-22 15:47:52.471417','2022-12-22 15:47:52.471433',27),(28,'fortest','2022-12-22 15:48:11.060096','2022-12-22 15:48:11.060112',28),(29,'fortest','2022-12-22 15:48:16.523905','2022-12-22 15:48:16.523924',29),(30,'fortest','2022-12-22 15:48:20.386141','2022-12-22 15:48:20.386154',30);
/*!40000 ALTER TABLE `memo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shorturl`
--

DROP TABLE IF EXISTS `shorturl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shorturl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `urlorigin` varchar(200) NOT NULL,
  `urlshorten` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `valid` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shorturl`
--

LOCK TABLES `shorturl` WRITE;
/*!40000 ALTER TABLE `shorturl` DISABLE KEYS */;
INSERT INTO `shorturl` VALUES (1,'http://192.168.200.174:8000/account/list','27a9bd0','2022-12-22 15:30:35.819068',1),(2,'http://192.168.200.174:8000/account/history/20221222','41c504b','2022-12-22 15:31:21.592109',1),(3,'http://192.168.200.174:8000/account/list','954af57','2022-12-22 15:36:30.452133',1);
/*!40000 ALTER TABLE `shorturl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'signet@naver.com','$2b$12$4eDk4/N1R0AJRef.vjU2s.zydvIIgb7heaKQ94i622eX2mPqUnDsK'),(2,'signet2@naver.com','$2b$12$OefN4eot1PhRiZLref.G5.alBqljVGRehlwOwhKghZDkFuA2cDJSy'),(3,'signet3@naver.com','$2b$12$oLEwUJKbr7n53NcL0IHlZeMKJRFSgL9aYEYuSlPHVZwRpjebaHh4C'),(4,'signet4@naver.com','$2b$12$Z9sI6eP9soJRLaN4y91tLeZJuGmjSu32fNpoC7Di23mU6wxG0x02u'),(5,'signet5@naver.com','$2b$12$izo4ZA0/phdSRpfUjNRSveI7x8M4g8cgzQu7V4.QI64P1RZPlgYni');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-22 17:28:20
