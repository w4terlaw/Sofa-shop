-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: sofa_shop
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `all_picture`
--

DROP TABLE IF EXISTS `all_picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_picture` (
  `id` int NOT NULL AUTO_INCREMENT,
  `picture` varchar(400) DEFAULT NULL,
  `product_has_color_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_all_picture_product_has_color1_idx` (`product_has_color_id`),
  CONSTRAINT `fk_all_picture_product_has_color1` FOREIGN KEY (`product_has_color_id`) REFERENCES `product_has_color` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_picture`
--

LOCK TABLES `all_picture` WRITE;
/*!40000 ALTER TABLE `all_picture` DISABLE KEYS */;
INSERT INTO `all_picture` VALUES (1,'https://ak1.ostkcdn.com/images/products/is/images/direct/350350252cca43b2cd4adf496fa3705c9b3e220f/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(2,'https://ak1.ostkcdn.com/images/products/is/images/direct/70b919326cc9202de8676668ddd5e4ce59e1b572/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(3,'https://ak1.ostkcdn.com/images/products/is/images/direct/96862196f042ae5538cfbd0dd54e40d0173fd8b9/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(4,'https://ak1.ostkcdn.com/images/products/is/images/direct/7abb06dd60c486801e606192f0738bcefc50e166/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(5,'https://ak1.ostkcdn.com/images/products/is/images/direct/ffc8da33a1c847d7a95a7bf5b2ab792140a54059/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(6,'https://ak1.ostkcdn.com/images/products/is/images/direct/efa21e7ee0e1d69e8d116f229cd56ff7161f13fe/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(7,'https://ak1.ostkcdn.com/images/products/is/images/direct/a73d828713f989a18e18914e59998d51d00550b9/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg',1),(8,'https://ak1.ostkcdn.com/images/products/is/images/direct/abe0d413a18fb4644c04bb83e0c895ad6bed7dcb/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(9,'https://ak1.ostkcdn.com/images/products/is/images/direct/58e72a1b10343636d789f6100ae4f57c925ad820/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(10,'https://ak1.ostkcdn.com/images/products/is/images/direct/f13d90ef9daff8855813814036a6e50931d10882/Corvus-Velvet-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(11,'https://ak1.ostkcdn.com/images/products/is/images/direct/d25708870aabaa49babd1e45d76ec8458f9d91ba/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(12,'https://ak1.ostkcdn.com/images/products/is/images/direct/768c0001b27b4419009c8961e5c6e332de66c764/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(13,'https://ak1.ostkcdn.com/images/products/is/images/direct/e7550e9a181621a823ac4b9aa50d88d5af8f19ff/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(14,'https://ak1.ostkcdn.com/images/products/is/images/direct/518c769b585186c8105d44e2037010dfca9383d8/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg',2),(15,'https://ak1.ostkcdn.com/images/products/is/images/direct/560b4e866ddfa9a72b14dff7cef0b24f3d198680/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(16,'https://ak1.ostkcdn.com/images/products/is/images/direct/8c6335f63b0e1740b6f69d89e647d78ce0df10aa/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(17,'https://ak1.ostkcdn.com/images/products/is/images/direct/0ce81f9eefdba8196e7baaf675662755c83dcab8/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(18,'https://ak1.ostkcdn.com/images/products/is/images/direct/563cc282a43721a01758bf8b02ecd3d0fe857fd7/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(19,'https://ak1.ostkcdn.com/images/products/is/images/direct/54e1debd2ff97ffd770a54aabb03d113ff3890a4/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(20,'https://ak1.ostkcdn.com/images/products/is/images/direct/6a760123e6779c31d28746b2d2191380416ada48/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(21,'https://ak1.ostkcdn.com/images/products/is/images/direct/f840e83eca8baa79ba07d4933d6ed5d4014a9c70/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(22,'https://ak1.ostkcdn.com/images/products/is/images/direct/5e25e79f2be3152108a90b3bea16169dc351be59/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(23,'https://ak1.ostkcdn.com/images/products/is/images/direct/a08f98c1d3e0df46c21822989b1e3c7f27ea349e/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',3),(24,'https://ak1.ostkcdn.com/images/products/is/images/direct/0c1f5bd415698ba44445fb5f1185aa3bdc7de567/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(25,'https://ak1.ostkcdn.com/images/products/is/images/direct/33ee2801d959ba0b5e8d0db2db14c3f0de5de919/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(26,'https://ak1.ostkcdn.com/images/products/is/images/direct/4e269cba02aa59c171207d3dc8fd8e561b95d577/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(27,'https://ak1.ostkcdn.com/images/products/is/images/direct/37989eda334a9a2a8ba99fad2760f9e1b4e08e80/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(28,'https://ak1.ostkcdn.com/images/products/is/images/direct/f4a5fc4ff9d59f00fb98d136a841b27b8ac38abe/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(29,'https://ak1.ostkcdn.com/images/products/is/images/direct/e64d67e62951f054ff3f10e8aa66a04fbb5a1e88/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(30,'https://ak1.ostkcdn.com/images/products/is/images/direct/d591092c32b8875b68ddcdcf00ff0f021473a325/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(31,'https://ak1.ostkcdn.com/images/products/is/images/direct/51a82c5fb8e1059571ebfc866037fde8b00be7b8/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(32,'https://ak1.ostkcdn.com/images/products/is/images/direct/623b9e990a44caed811898a5e7e218fbca1929e7/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',4),(33,'https://ak1.ostkcdn.com/images/products/is/images/direct/28976e342609c45d2c11ca41dd2d3c67a6843add/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(34,'https://ak1.ostkcdn.com/images/products/is/images/direct/a1bde2dca56ffbcebedd5e4b3bf26685996e7221/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(35,'https://ak1.ostkcdn.com/images/products/is/images/direct/d483682684d2a2bf000af6b6abb88a80fa54906b/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(36,'https://ak1.ostkcdn.com/images/products/is/images/direct/d12b2d6ef913c69f54fe9cb48aa534792668ffd0/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(37,'https://ak1.ostkcdn.com/images/products/is/images/direct/cc67d2c35692a75107f968f45874b6d56776ac2a/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(38,'https://ak1.ostkcdn.com/images/products/is/images/direct/ed9c9a7a5ef8e5a78c5b6c6f08c9010f5f678d27/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(39,'https://ak1.ostkcdn.com/images/products/is/images/direct/95500852176c2eab521380b1ebd69cee818fe31b/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(40,'https://ak1.ostkcdn.com/images/products/is/images/direct/970dca4a23e4864ccc9f5397641d1e1ac7c00830/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(41,'https://ak1.ostkcdn.com/images/products/is/images/direct/1f869a6f60d6b68576514c8d343a1f7bfd839103/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg',5),(42,'https://ak1.ostkcdn.com/images/products/is/images/direct/2db853efb7901c0b8f0b535d69fad3bdc0fa5b55/Ansonia-Contemporary-3-Seater-Velvet-Sofa-by-Christopher-Knight-Home.jpg',24),(43,'https://ak1.ostkcdn.com/images/products/is/images/direct/f58f938a45fa586c9d7bce7914d4bf7e25f17277/Ansonia-3-seat-Contemporary-Velvet-Sofa-by-Christopher-Knight-Home.jpg',24),(44,'https://ak1.ostkcdn.com/images/products/is/images/direct/ecd8449252eb31b60ac61293db2ec3d68c1ad54e/Ansonia-Contemporary-3-Seater-Velvet-Sofa-by-Christopher-Knight-Home.jpg',24),(45,'https://ak1.ostkcdn.com/images/products/is/images/direct/855eabbce12003dbc8584caf477d5ba8e70dfd73/Ansonia-Contemporary-3-Seater-Velvet-Sofa-by-Christopher-Knight-Home.jpg',24),(46,'https://ak1.ostkcdn.com/images/products/is/images/direct/fca1ef61640b66c67d5356b428a07471c8cecbd6/Ansonia-Contemporary-3-Seater-Velvet-Sofa-by-Christopher-Knight-Home.jpg',24);
/*!40000 ALTER TABLE `all_picture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `color`
--

DROP TABLE IF EXISTS `color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `color` (
  `id` int NOT NULL AUTO_INCREMENT,
  `color` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `color`
--

LOCK TABLES `color` WRITE;
/*!40000 ALTER TABLE `color` DISABLE KEYS */;
INSERT INTO `color` VALUES (1,'Черный'),(2,'Голубой'),(3,'Кориченвый'),(4,'Зеленый'),(5,'Серый'),(6,'Оранжевый'),(7,'Розовый'),(8,'Фиолетовый'),(9,'Красный'),(10,'Серебрянный'),(11,'Белый'),(12,'Желтый');
/*!40000 ALTER TABLE `color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material` (
  `id` int NOT NULL AUTO_INCREMENT,
  `material` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
INSERT INTO `material` VALUES (1,'Ткань'),(2,'Дерево'),(3,'Кожа'),(4,'Бархат'),(5,'Полиэстер'),(6,'Береза'),(7,'Искусственная кожа'),(8,'Лен');
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_product`
--

DROP TABLE IF EXISTS `order_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_product` (
  `idOrder` int NOT NULL,
  `idProduct` int NOT NULL,
  `count` int NOT NULL,
  `color_id` int NOT NULL,
  PRIMARY KEY (`idOrder`,`idProduct`,`color_id`),
  KEY `fk_Order_product_Product1_idx` (`idProduct`),
  KEY `fk_order_product_color1_idx` (`color_id`),
  CONSTRAINT `fk_order_product_color1` FOREIGN KEY (`color_id`) REFERENCES `color` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Order_product_Order1` FOREIGN KEY (`idOrder`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Order_product_Product1` FOREIGN KEY (`idProduct`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='							\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\ngkhhhh							';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_product`
--

LOCK TABLES `order_product` WRITE;
/*!40000 ALTER TABLE `order_product` DISABLE KEYS */;
INSERT INTO `order_product` VALUES (219,1,1,5),(219,1,1,11),(223,2,8,5);
/*!40000 ALTER TABLE `order_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idUser` int NOT NULL,
  `datetime` date NOT NULL,
  `actual` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Order_Customer1_idx` (`idUser`),
  CONSTRAINT `fk_Order_Customer1` FOREIGN KEY (`idUser`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=224 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (219,2,'2022-12-25',_binary ''),(223,1,'2022-12-26',_binary '');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Order_idOrder` int NOT NULL,
  `delivery` varchar(300) NOT NULL,
  `datetime` datetime NOT NULL,
  `method` varchar(45) NOT NULL,
  `total_price` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Payment_Order1_idx` (`Order_idOrder`),
  CONSTRAINT `fk_Payment_Order1` FOREIGN KEY (`Order_idOrder`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `type_id` int NOT NULL,
  `description` varchar(400) DEFAULT NULL,
  `price` int NOT NULL,
  `count` int NOT NULL,
  `country` varchar(45) NOT NULL,
  `weight` int DEFAULT NULL,
  `overall` varchar(200) DEFAULT NULL,
  `seat` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`,`type_id`),
  KEY `fk_product_type1_idx` (`type_id`),
  CONSTRAINT `fk_product_type1` FOREIGN KEY (`type_id`) REFERENCES `type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Трехместный диван Corvus Aleksis Tufted Chesterfield',1,'Привнесите классический стиль и традиционную элегантность в ваше пространство с помощью этого прекрасного и роскошного льняного дивана. Этот диван с отделкой на пуговицах и закатанными подлокотниками поднимает настроение вашему интерьеру, предлагая шикарное и красивое место для сидения, которое обязательно понравится вам и вашим гостям.',53998,9,'Китай',64,'75 см в высоту, 232 см в ширину и 93 см в глубину.','49,5 см в высоту, 179,8 см в ширину и 62,5 см в глубину.'),(2,'Reitz Glam Velvet Shell от Christopher Knight Home',1,'Придайте своему жилому пространству гламурный вид с диваном Reitz. Каркас из золотистого железа имеет зубчатую спинку сиденья в виде ракушки и наполнитель из пеноматериала. Выберите один из цветов полиэфирно-бархатной обивки, чтобы дополнить существующий декор.',47999,6,'Китай',317,'84,45 см в высоту, 193,68 см в ширину и 74,3 см в глубину.','47 см в высоту, 160 см в ширину и 55,88 см в глубину.'),(30,'Ansonia от Christopher Knight Home',1,'Наслаждайтесь гламурной текстурой эффектного дивана Ansonia от Christopher Knight Home. Каркас из каучукового дерева имеет наклонные подлокотники, наполнитель из пеноматериала, бархатную обивку и соответствующие акцентные подушки. Канальная тафтинговая ткань покрывает спинку сиденья, придавая ей неподвластную времени текстуру.',44949,1,'Китай',74,'213 см в высоту, 86 см в ширину и 74 см в глубину.','45,2 см в высоту, 140,8 см в ширину и 62,5 см в глубину.');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_has_color`
--

DROP TABLE IF EXISTS `product_has_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_has_color` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `color_id` int NOT NULL,
  `picture` varchar(400) DEFAULT NULL,
  `picture2` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_has_color_color1_idx` (`color_id`),
  KEY `fk_product_has_color_product1_idx` (`product_id`),
  CONSTRAINT `fk_product_has_color_color1` FOREIGN KEY (`color_id`) REFERENCES `color` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_product_has_color_product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_has_color`
--

LOCK TABLES `product_has_color` WRITE;
/*!40000 ALTER TABLE `product_has_color` DISABLE KEYS */;
INSERT INTO `product_has_color` VALUES (1,1,5,'https://ak1.ostkcdn.com/images/products/is/images/direct/350350252cca43b2cd4adf496fa3705c9b3e220f/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg','https://ak1.ostkcdn.com/images/products/is/images/direct/96862196f042ae5538cfbd0dd54e40d0173fd8b9/Corvus-Aleksis-Tufted-Chesterfield-3-seater-Sofa-with-Rolled-Arms.jpg'),(2,1,11,'https://ak1.ostkcdn.com/images/products/is/images/direct/abe0d413a18fb4644c04bb83e0c895ad6bed7dcb/Corvus-Tufted-Chesterfield-Sofa-with-Rolled-Arms.jpg','https://ak1.ostkcdn.com/images/products/is/images/direct/f13d90ef9daff8855813814036a6e50931d10882/Corvus-Velvet-Chesterfield-Sofa-with-Rolled-Arms.jpg'),(3,2,9,'https://ak1.ostkcdn.com/images/products/is/images/direct/560b4e866ddfa9a72b14dff7cef0b24f3d198680/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg','https://ak1.ostkcdn.com/images/products/is/images/direct/02464237d4689f11996868c74466ba2d515b59cf/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg'),(4,2,5,'https://ak1.ostkcdn.com/images/products/is/images/direct/0c1f5bd415698ba44445fb5f1185aa3bdc7de567/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg','https://ak1.ostkcdn.com/images/products/is/images/direct/463b88bd17751182d63cd242d0a78be19cf3ab9a/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg'),(5,2,12,'https://ak1.ostkcdn.com/images/products/is/images/direct/28976e342609c45d2c11ca41dd2d3c67a6843add/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg','https://ak1.ostkcdn.com/images/products/is/images/direct/e46e4b209649b20f1f66c55197a87f5af72e67ec/Reitz-Modern-Glam-Velvet-Channel-Stitch-3-Seater-Shell-Sofa-by-Christopher-Knight-Home.jpg'),(24,30,4,'https://ak1.ostkcdn.com/images/products/is/images/direct/2db853efb7901c0b8f0b535d69fad3bdc0fa5b55/Ansonia-Contemporary-3-Seater-Velvet-Sofa-by-Christopher-Knight-Home.jpg','https://ak1.ostkcdn.com/images/products/is/images/direct/f58f938a45fa586c9d7bce7914d4bf7e25f17277/Ansonia-3-seat-Contemporary-Velvet-Sofa-by-Christopher-Knight-Home.jpg]');
/*!40000 ALTER TABLE `product_has_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_has_material`
--

DROP TABLE IF EXISTS `product_has_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_has_material` (
  `product_id` int NOT NULL,
  `material_id` int NOT NULL,
  PRIMARY KEY (`product_id`,`material_id`),
  KEY `fk_product_has_material_material1_idx` (`material_id`),
  KEY `fk_product_has_material_product1_idx` (`product_id`),
  CONSTRAINT `fk_product_has_material_material1` FOREIGN KEY (`material_id`) REFERENCES `material` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_product_has_material_product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_has_material`
--

LOCK TABLES `product_has_material` WRITE;
/*!40000 ALTER TABLE `product_has_material` DISABLE KEYS */;
INSERT INTO `product_has_material` VALUES (1,1),(2,1),(1,2),(30,2),(30,4),(2,8);
/*!40000 ALTER TABLE `product_has_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_title` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'Диван');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `admin` tinyint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'abkerimov.e.i20@gmail.com','$5$rounds=535000$lXcAGcqTNzNuj.6H$4B4atvLL5e3lX0KAfoMwkrx4TI5p8YDRZIfLFJhKSi/','Эльмир','Абкеримов','',1),(2,'lera@gmail.com','$5$rounds=535000$vtKPyzwq6m8wtq15$bHD.R0JK/jiPjTIpU1acJDi4rvGhNBH7hwvGKwDzrq0','Валерия','Максимова','Октябрьская 1А',0),(9,'abkerimov.e.i20@gmail.com213','$5$rounds=535000$LWWqYKrbPtCNXhag$1eeUzeDHJIdbpDbz9FROoZBqfvCq980p1lf43Kog0t0','Эльмириано','Абкерика','',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-26 21:47:35
