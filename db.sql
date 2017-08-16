/*
Navicat MySQL Data Transfer

Source Server         : BBBs
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-08-10 17:08:06
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `user2`
-- ----------------------------
DROP TABLE IF EXISTS `user2`;
CREATE TABLE `user2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `position` varchar(20) NOT NULL,
  `age` varchar(20) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user2
-- ----------------------------
INSERT INTO `user2` VALUES ('4', '44444', '4444@4444.com', '4444', '43', '44444.png');
INSERT INTO `user2` VALUES ('7', '5555', '555@555.com', '4455544', '23', '5555.png');
INSERT INTO `user2` VALUES ('8', 'asssss', 'assss@fdfds.com', 'asss', '43', 'default.png');
INSERT INTO `user2` VALUES ('9', 'xml1', 'xml1@xml1.COM', 'xml1', '20', 'default.png');
INSERT INTO `user2` VALUES ('10', 'xml3', 'xml3@xml3.COM', 'xml3', '22', 'default.png');
INSERT INTO `user2` VALUES ('11', 'xml3', 'xml3@xml3.COM', 'xml3', '22', 'xml3.png');
INSERT INTO `user2` VALUES ('12', 'PRUEBA4346563', 'PRUEBA4346563@PRUEBA4346563.COM', 'PRUEBA4346563', '27', 'PRUEBA4346563.png');
INSERT INTO `user2` VALUES ('13', 'EEEEE43434', 'EEEEE43434@EEEEE43434.com', 'EEEEE43434', '43', 'EEEEE43434.png');
INSERT INTO `user2` VALUES ('14', 'PRUEBA4346560', 'PRUEBA4346560@PRUEBA4346560.COM', 'PRUEBA4346560', '21', 'PRUEBA4346560.png');
INSERT INTO `user2` VALUES ('15', 'PRUEBA434656110', 'PRUEBA434656110@PRUEBA434656110.COM', 'PRUEBA434656110', '21', 'PRUEBA434656110.png');
INSERT INTO `user2` VALUES ('16', 'PRUEBA4346561101', 'PRUEBA4346561101@PRUEBA4346561101.com', 'PRUEBA4346561101', '22', 'PRUEBA4346561101.png');
INSERT INTO `user2` VALUES ('17', 'p1', 'p1@p1.COM', 'p1', '27', 'default.png');
INSERT INTO `user2` VALUES ('18', 'p2', 'p2@p2.com', 'p2', '43', 'default.png');
INSERT INTO `user2` VALUES ('19', 'p3', 'p3@p3.com', 'p3', '43', 'default.png');
INSERT INTO `user2` VALUES ('21', 'p5-p5-p5123456', 'p5-p5@p5-p5.com', 'p5-p5', '23', 'p5-p5-p5123456.png');
