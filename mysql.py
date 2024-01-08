

MYSQL 공부 

2024. 1. 3


Download XAMPP for Windwos

https://www.apachefriends.org/download.html




C:\xampp\mysql\bin

mysql -uroot -pㄷ




CREATE DATABASE opentutorials;

DROP DATABASE opentutorials;

SHOW DATABASES;

SHOW SCHEMAS;

USE opentutorials;




CREATE TABLE topic(
    -> id INT(11) NOT NULL AUTO_INCREMENT,
    -> title VARCHAR(100) NOT NULL,
    -> description TEXT NULL,
    -> created DATETIME NOT NULL,
    -> author VARCHAR(30) NULL,
    -> profile VARCHAR(100) NULL,
    -> PRIMARY KEY(id));




SHOW TABLES;

DESC topic;




INSERT INTO topic(title, description, created, author, profile) VALUES('MySQL', 'MySQL is...', NOW(), 'jey', 'QA');




SELECT * FROM topic;

SELECT id,title,created,author FROM topic;

SELECT id,title,created,author FROM topic WHERE author='jey';

SELECT id,title,created,author FROM topic WHERE author='jey' ORDER BY id DESC;

SELECT id,title,created,author FROM topic WHERE author='jey' ORDER BY id DESC LIMIT 2;




UPDATE topic SET description='Oracle is', title='Oracle' WHERE id=2;

DELETE FROM topic WHERE id=5;




테이블 분리




RENAME TABLE topic TO topic_backup;




--
-- Table structure for table `author`
--
 
 
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `profile` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
 
--
-- Dumping data for table `author`
--
 
INSERT INTO `author` VALUES (1,'egoing','developer');
INSERT INTO `author` VALUES (2,'duru','database administrator');
INSERT INTO `author` VALUES (3,'taeho','data scientist, developer');
 
--
-- Table structure for table `topic`
--
 
CREATE TABLE `topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `description` text,
  `created` datetime NOT NULL,
  `author_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
 
--
-- Dumping data for table `topic`
--
 
INSERT INTO `topic` VALUES (1,'MySQL','MySQL is...','2018-01-01 12:10:11',1);
INSERT INTO `topic` VALUES (2,'Oracle','Oracle is ...','2018-01-03 13:01:10',1);
INSERT INTO `topic` VALUES (3,'SQL Server','SQL Server is ...','2018-01-20 11:01:10',2);
INSERT INTO `topic` VALUES (4,'PostgreSQL','PostgreSQL is ...','2018-01-23 01:03:03',3);
INSERT INTO `topic` VALUES (5,'MongoDB','MongoDB is ...','2018-01-30 12:31:03',1);




SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id;

SELECT topic.id, title, description, created, name, profile FROM topic LEFT JOIN author ON topic.author_id = author.id;

SELECT topic.id AS topic_id, title, description, created, name, profile FROM topic LEFT JOIN author ON topic.author_id = author.id;




/mysql -uroot -p -hlocalhost








