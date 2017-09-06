/*
Navicat MySQL Data Transfer

Source Server         : BBBs2
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-09-06 15:38:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `position` varchar(20) NOT NULL,
  `age` varchar(20) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('4', '44444', '4444@4444.com', '44444', '43', '44444.png', '123456');
INSERT INTO `user` VALUES ('7', '5555', '555@555.com', '5555', '23', '5555.png', null);
INSERT INTO `user` VALUES ('8', 'asssss', 'assss@fdfds.com', 'asssss', '43', 'default.png', null);
INSERT INTO `user` VALUES ('9', 'xml1', 'xml1@xml1.COM', 'xml1', '20', 'default.png', null);
INSERT INTO `user` VALUES ('10', 'xml3', 'xml3@xml3.COM', 'xml3', '22', 'default.png', null);
INSERT INTO `user` VALUES ('11', 'xml3', 'xml3@xml3.COM', 'xml3', '22', 'xml3.png', null);
INSERT INTO `user` VALUES ('12', 'PRUEBA4346563', 'PRUEBA4346563@PRUEBA4346563.COM', 'PRUEBA4346563', '27', 'PRUEBA4346563.png', null);
INSERT INTO `user` VALUES ('13', 'EEEEE43434', 'EEEEE43434@EEEEE43434.com', 'EEEEE43434', '43', 'EEEEE43434.png', null);
INSERT INTO `user` VALUES ('14', 'PRUEBA4346560', 'PRUEBA4346560@PRUEBA4346560.COM', 'PRUEBA4346560', '21', 'PRUEBA4346560.png', null);
INSERT INTO `user` VALUES ('15', 'PRUEBA434656110', 'PRUEBA434656110@PRUEBA434656110.COM', 'PRUEBA434656110', '21', 'PRUEBA434656110.png', null);
INSERT INTO `user` VALUES ('16', 'PRUEBA4346561101', 'PRUEBA4346561101@PRUEBA4346561101.com', 'PRUEBA4346561101', '22', 'PRUEBA4346561101.png', null);
INSERT INTO `user` VALUES ('17', 'p1', 'p1@p1.COM', 'p1', '27', 'default.png', null);
INSERT INTO `user` VALUES ('18', 'p2', 'p2@p2.com', 'p2', '43', 'default.png', null);
INSERT INTO `user` VALUES ('19', 'p3', 'p3@p3.com', 'p3', '43', 'default.png', null);
INSERT INTO `user` VALUES ('21', 'p5-p5-p5123456', 'p5-p5@p5-p5.com', 'p5-p5-p5123456', '23', 'p5-p5-p5123456.png', null);
INSERT INTO `user` VALUES ('26', '11111', '11111@11111.COM', '11111', '27', '11111.png', '123456');
