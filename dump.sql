-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: zilong_report
-- ------------------------------------------------------
-- Server version	5.7.13

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
-- Table structure for table `ad_action`
--

DROP TABLE IF EXISTS `ad_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ad_action` (
  `date` datetime NOT NULL,
  `id` varchar(20) DEFAULT NULL,
  `channel_name` varchar(45) DEFAULT NULL,
  `agent` varchar(45) DEFAULT NULL,
  `ad_click` varchar(45) DEFAULT NULL,
  `ad_action` varchar(45) DEFAULT NULL,
  `ad_action_new` varchar(45) DEFAULT NULL,
  `ad_account_new` varchar(45) DEFAULT NULL,
  `ad_account_new_pay` varchar(45) DEFAULT NULL,
  `ad_account_new_paymoney` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dis_result`
--

DROP TABLE IF EXISTS `dis_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dis_result` (
  `date` datetime DEFAULT NULL,
  `dis` float DEFAULT NULL,
  `class` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `login_info`
--

DROP TABLE IF EXISTS `login_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_info` (
  `user_id` int(11) DEFAULT NULL,
  `login_time` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `power_info`
--

DROP TABLE IF EXISTS `power_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `power_info` (
  `user_id` int(11) NOT NULL,
  `power_user_list` longtext,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `re_money`
--

DROP TABLE IF EXISTS `re_money`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `re_money` (
  `date` datetime NOT NULL,
  `id` varchar(20) DEFAULT NULL,
  `channel_name` varchar(45) NOT NULL,
  `agent` varchar(45) NOT NULL,
  `money_0` float DEFAULT NULL,
  `money_1` float DEFAULT NULL,
  `money_2` float DEFAULT NULL,
  `money_3` float DEFAULT NULL,
  `money_4` float DEFAULT NULL,
  `money_5` float DEFAULT NULL,
  `money_6` float DEFAULT NULL,
  `money_7` float DEFAULT NULL,
  `money_8` float DEFAULT NULL,
  `money_9` float DEFAULT NULL,
  `money_10` float DEFAULT NULL,
  `money_11` float DEFAULT NULL,
  `money_12` float DEFAULT NULL,
  `money_13` float DEFAULT NULL,
  `money_14` float DEFAULT NULL,
  `money_15` float DEFAULT NULL,
  `money_16` float DEFAULT NULL,
  `money_17` float DEFAULT NULL,
  `money_18` float DEFAULT NULL,
  `money_19` float DEFAULT NULL,
  `money_20` float DEFAULT NULL,
  `money_21` float DEFAULT NULL,
  `money_22` float DEFAULT NULL,
  `money_23` float DEFAULT NULL,
  `money_24` float DEFAULT NULL,
  `money_25` float DEFAULT NULL,
  `money_26` float DEFAULT NULL,
  `money_27` float DEFAULT NULL,
  `money_28` float DEFAULT NULL,
  `money_29` float DEFAULT NULL,
  `money_30` float DEFAULT NULL,
  `money_31` float DEFAULT NULL,
  `money_32` float DEFAULT NULL,
  `money_33` float DEFAULT NULL,
  `money_34` float DEFAULT NULL,
  `money_35` float DEFAULT NULL,
  `money_36` float DEFAULT NULL,
  `money_37` float DEFAULT NULL,
  `money_38` float DEFAULT NULL,
  `money_39` float DEFAULT NULL,
  `money_40` float DEFAULT NULL,
  `money_41` float DEFAULT NULL,
  `money_42` float DEFAULT NULL,
  `money_43` float DEFAULT NULL,
  `money_44` float DEFAULT NULL,
  `money_45` float DEFAULT NULL,
  `money_46` float DEFAULT NULL,
  `money_47` float DEFAULT NULL,
  `money_48` float DEFAULT NULL,
  `money_49` float DEFAULT NULL,
  `money_50` float DEFAULT NULL,
  `money_51` float DEFAULT NULL,
  `money_52` float DEFAULT NULL,
  `money_53` float DEFAULT NULL,
  `money_54` float DEFAULT NULL,
  `money_55` float DEFAULT NULL,
  `money_56` float DEFAULT NULL,
  `money_57` float DEFAULT NULL,
  `money_58` float DEFAULT NULL,
  `money_59` float DEFAULT NULL,
  `money_60` float DEFAULT NULL,
  `money_61` float DEFAULT NULL,
  `money_62` float DEFAULT NULL,
  `money_63` float DEFAULT NULL,
  `money_64` float DEFAULT NULL,
  `money_65` float DEFAULT NULL,
  `money_66` float DEFAULT NULL,
  `money_67` float DEFAULT NULL,
  `money_68` float DEFAULT NULL,
  `money_69` float DEFAULT NULL,
  `money_70` float DEFAULT NULL,
  `money_71` float DEFAULT NULL,
  `money_72` float DEFAULT NULL,
  `money_73` float DEFAULT NULL,
  `money_74` float DEFAULT NULL,
  `money_75` float DEFAULT NULL,
  `money_76` float DEFAULT NULL,
  `money_77` float DEFAULT NULL,
  `money_78` float DEFAULT NULL,
  `money_79` float DEFAULT NULL,
  `money_80` float DEFAULT NULL,
  `money_81` float DEFAULT NULL,
  `money_82` float DEFAULT NULL,
  `money_83` float DEFAULT NULL,
  `money_84` float DEFAULT NULL,
  `money_85` float DEFAULT NULL,
  `money_86` float DEFAULT NULL,
  `money_87` float DEFAULT NULL,
  `money_88` float DEFAULT NULL,
  `money_89` float DEFAULT NULL,
  `money_90` float DEFAULT NULL,
  `money_91` float DEFAULT NULL,
  `money_92` float DEFAULT NULL,
  `money_93` float DEFAULT NULL,
  `money_94` float DEFAULT NULL,
  `money_95` float DEFAULT NULL,
  `money_96` float DEFAULT NULL,
  `money_97` float DEFAULT NULL,
  `money_98` float DEFAULT NULL,
  `money_99` float DEFAULT NULL,
  `money_100` float DEFAULT NULL,
  `money_101` float DEFAULT NULL,
  `money_102` float DEFAULT NULL,
  `money_103` float DEFAULT NULL,
  `money_104` float DEFAULT NULL,
  `money_105` float DEFAULT NULL,
  `money_106` float DEFAULT NULL,
  `money_107` float DEFAULT NULL,
  `money_108` float DEFAULT NULL,
  `money_109` float DEFAULT NULL,
  `money_110` float DEFAULT NULL,
  `money_111` float DEFAULT NULL,
  `money_112` float DEFAULT NULL,
  `money_113` float DEFAULT NULL,
  `money_114` float DEFAULT NULL,
  `money_115` float DEFAULT NULL,
  `money_116` float DEFAULT NULL,
  `money_117` float DEFAULT NULL,
  `money_118` float DEFAULT NULL,
  `money_119` float DEFAULT NULL,
  `money_120` float DEFAULT NULL,
  `money_121` float DEFAULT NULL,
  `money_122` float DEFAULT NULL,
  `money_123` float DEFAULT NULL,
  `money_124` float DEFAULT NULL,
  `money_125` float DEFAULT NULL,
  `money_126` float DEFAULT NULL,
  `money_127` float DEFAULT NULL,
  `money_128` float DEFAULT NULL,
  `money_129` float DEFAULT NULL,
  `money_130` float DEFAULT NULL,
  `money_131` float DEFAULT NULL,
  `money_132` float DEFAULT NULL,
  `money_133` float DEFAULT NULL,
  `money_134` float DEFAULT NULL,
  `money_135` float DEFAULT NULL,
  `money_136` float DEFAULT NULL,
  `money_137` float DEFAULT NULL,
  `money_138` float DEFAULT NULL,
  `money_139` float DEFAULT NULL,
  `money_140` float DEFAULT NULL,
  `money_141` float DEFAULT NULL,
  `money_142` float DEFAULT NULL,
  `money_143` float DEFAULT NULL,
  `money_144` float DEFAULT NULL,
  `money_145` float DEFAULT NULL,
  `money_146` float DEFAULT NULL,
  `money_147` float DEFAULT NULL,
  `money_148` float DEFAULT NULL,
  `money_149` float DEFAULT NULL,
  `money_150` float DEFAULT NULL,
  `money_151` float DEFAULT NULL,
  `money_152` float DEFAULT NULL,
  `money_153` float DEFAULT NULL,
  `money_154` float DEFAULT NULL,
  `money_155` float DEFAULT NULL,
  `money_156` float DEFAULT NULL,
  `money_157` float DEFAULT NULL,
  `money_158` float DEFAULT NULL,
  `money_159` float DEFAULT NULL,
  `money_160` float DEFAULT NULL,
  `money_161` float DEFAULT NULL,
  `money_162` float DEFAULT NULL,
  `money_163` float DEFAULT NULL,
  `money_164` float DEFAULT NULL,
  `money_165` float DEFAULT NULL,
  `money_166` float DEFAULT NULL,
  `money_167` float DEFAULT NULL,
  `money_168` float DEFAULT NULL,
  `money_169` float DEFAULT NULL,
  `money_170` float DEFAULT NULL,
  `money_171` float DEFAULT NULL,
  `money_172` float DEFAULT NULL,
  `money_173` float DEFAULT NULL,
  `money_174` float DEFAULT NULL,
  `money_175` float DEFAULT NULL,
  `money_176` float DEFAULT NULL,
  `money_177` float DEFAULT NULL,
  `money_178` float DEFAULT NULL,
  `money_179` float DEFAULT NULL,
  `money_180` float DEFAULT NULL,
  `money_181` float DEFAULT NULL,
  `money_182` float DEFAULT NULL,
  `money_183` float DEFAULT NULL,
  `money_184` float DEFAULT NULL,
  `money_185` float DEFAULT NULL,
  `money_186` float DEFAULT NULL,
  `money_187` float DEFAULT NULL,
  `money_188` float DEFAULT NULL,
  `money_189` float DEFAULT NULL,
  `money_190` float DEFAULT NULL,
  `money_191` float DEFAULT NULL,
  `money_192` float DEFAULT NULL,
  `money_193` float DEFAULT NULL,
  `money_194` float DEFAULT NULL,
  `money_195` float DEFAULT NULL,
  `money_196` float DEFAULT NULL,
  `money_197` float DEFAULT NULL,
  `money_198` float DEFAULT NULL,
  `money_199` float DEFAULT NULL,
  `money_200` float DEFAULT NULL,
  `money_201` float DEFAULT NULL,
  `money_202` float DEFAULT NULL,
  `money_203` float DEFAULT NULL,
  `money_204` float DEFAULT NULL,
  `money_205` float DEFAULT NULL,
  `money_206` float DEFAULT NULL,
  `money_207` float DEFAULT NULL,
  `money_208` float DEFAULT NULL,
  `money_209` float DEFAULT NULL,
  `money_210` float DEFAULT NULL,
  `money_211` float DEFAULT NULL,
  `money_212` float DEFAULT NULL,
  `money_213` float DEFAULT NULL,
  `money_214` float DEFAULT NULL,
  `money_215` float DEFAULT NULL,
  `money_216` float DEFAULT NULL,
  `money_217` float DEFAULT NULL,
  `money_218` float DEFAULT NULL,
  `money_219` float DEFAULT NULL,
  `money_220` float DEFAULT NULL,
  `money_221` float DEFAULT NULL,
  `money_222` float DEFAULT NULL,
  `money_223` float DEFAULT NULL,
  `money_224` float DEFAULT NULL,
  `money_225` float DEFAULT NULL,
  `money_226` float DEFAULT NULL,
  `money_227` float DEFAULT NULL,
  `money_228` float DEFAULT NULL,
  `money_229` float DEFAULT NULL,
  `money_230` float DEFAULT NULL,
  `money_231` float DEFAULT NULL,
  `money_232` float DEFAULT NULL,
  `money_233` float DEFAULT NULL,
  `money_234` float DEFAULT NULL,
  `money_235` float DEFAULT NULL,
  `money_236` float DEFAULT NULL,
  `money_237` float DEFAULT NULL,
  `money_238` float DEFAULT NULL,
  `money_239` float DEFAULT NULL,
  `money_240` float DEFAULT NULL,
  `money_241` float DEFAULT NULL,
  `money_242` float DEFAULT NULL,
  `money_243` float DEFAULT NULL,
  `money_244` float DEFAULT NULL,
  `money_245` float DEFAULT NULL,
  `money_246` float DEFAULT NULL,
  `money_247` float DEFAULT NULL,
  `money_248` float DEFAULT NULL,
  `money_249` float DEFAULT NULL,
  `money_250` float DEFAULT NULL,
  `money_251` float DEFAULT NULL,
  `money_252` float DEFAULT NULL,
  `money_253` float DEFAULT NULL,
  `money_254` float DEFAULT NULL,
  `money_255` float DEFAULT NULL,
  `money_256` float DEFAULT NULL,
  `money_257` float DEFAULT NULL,
  `money_258` float DEFAULT NULL,
  `money_259` float DEFAULT NULL,
  `money_260` float DEFAULT NULL,
  `money_261` float DEFAULT NULL,
  `money_262` float DEFAULT NULL,
  `money_263` float DEFAULT NULL,
  `money_264` float DEFAULT NULL,
  `money_265` float DEFAULT NULL,
  `money_266` float DEFAULT NULL,
  `money_267` float DEFAULT NULL,
  `money_268` float DEFAULT NULL,
  `money_269` float DEFAULT NULL,
  `money_270` float DEFAULT NULL,
  `money_271` float DEFAULT NULL,
  `money_272` float DEFAULT NULL,
  `money_273` float DEFAULT NULL,
  `money_274` float DEFAULT NULL,
  `money_275` float DEFAULT NULL,
  `money_276` float DEFAULT NULL,
  `money_277` float DEFAULT NULL,
  `money_278` float DEFAULT NULL,
  `money_279` float DEFAULT NULL,
  `money_280` float DEFAULT NULL,
  `money_281` float DEFAULT NULL,
  `money_282` float DEFAULT NULL,
  `money_283` float DEFAULT NULL,
  `money_284` float DEFAULT NULL,
  `money_285` float DEFAULT NULL,
  `money_286` float DEFAULT NULL,
  `money_287` float DEFAULT NULL,
  `money_288` float DEFAULT NULL,
  `money_289` float DEFAULT NULL,
  `money_290` float DEFAULT NULL,
  `money_291` float DEFAULT NULL,
  `money_292` float DEFAULT NULL,
  `money_293` float DEFAULT NULL,
  `money_294` float DEFAULT NULL,
  `money_295` float DEFAULT NULL,
  `money_296` float DEFAULT NULL,
  `money_297` float DEFAULT NULL,
  `money_298` float DEFAULT NULL,
  `money_299` float DEFAULT NULL,
  `money_300` float DEFAULT NULL,
  `money_301` float DEFAULT NULL,
  `money_302` float DEFAULT NULL,
  `money_303` float DEFAULT NULL,
  `money_304` float DEFAULT NULL,
  `money_305` float DEFAULT NULL,
  `money_306` float DEFAULT NULL,
  `money_307` float DEFAULT NULL,
  `money_308` float DEFAULT NULL,
  `money_309` float DEFAULT NULL,
  `money_310` float DEFAULT NULL,
  `money_311` float DEFAULT NULL,
  `money_312` float DEFAULT NULL,
  `money_313` float DEFAULT NULL,
  `money_314` float DEFAULT NULL,
  `money_315` float DEFAULT NULL,
  `money_316` float DEFAULT NULL,
  `money_317` float DEFAULT NULL,
  `money_318` float DEFAULT NULL,
  `money_319` float DEFAULT NULL,
  `money_320` float DEFAULT NULL,
  `money_321` float DEFAULT NULL,
  `money_322` float DEFAULT NULL,
  `money_323` float DEFAULT NULL,
  `money_324` float DEFAULT NULL,
  `money_325` float DEFAULT NULL,
  `money_326` float DEFAULT NULL,
  `money_327` float DEFAULT NULL,
  `money_328` float DEFAULT NULL,
  `money_329` float DEFAULT NULL,
  `money_330` float DEFAULT NULL,
  `money_331` float DEFAULT NULL,
  `money_332` float DEFAULT NULL,
  `money_333` float DEFAULT NULL,
  `money_334` float DEFAULT NULL,
  `money_335` float DEFAULT NULL,
  `money_336` float DEFAULT NULL,
  `money_337` float DEFAULT NULL,
  `money_338` float DEFAULT NULL,
  `money_339` float DEFAULT NULL,
  `money_340` float DEFAULT NULL,
  `money_341` float DEFAULT NULL,
  `money_342` float DEFAULT NULL,
  `money_343` float DEFAULT NULL,
  `money_344` float DEFAULT NULL,
  `money_345` float DEFAULT NULL,
  `money_346` float DEFAULT NULL,
  `money_347` float DEFAULT NULL,
  `money_348` float DEFAULT NULL,
  `money_349` float DEFAULT NULL,
  `money_350` float DEFAULT NULL,
  `money_351` float DEFAULT NULL,
  `money_352` float DEFAULT NULL,
  `money_353` float DEFAULT NULL,
  `money_354` float DEFAULT NULL,
  `money_355` float DEFAULT NULL,
  `money_356` float DEFAULT NULL,
  `money_357` float DEFAULT NULL,
  `money_358` float DEFAULT NULL,
  `money_359` float DEFAULT NULL,
  `money_360` float DEFAULT NULL,
  `money_361` float DEFAULT NULL,
  `money_362` float DEFAULT NULL,
  `money_363` float DEFAULT NULL,
  `money_364` float DEFAULT NULL,
  PRIMARY KEY (`date`,`channel_name`,`agent`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `retention`
--

DROP TABLE IF EXISTS `retention`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retention` (
  `_date` datetime DEFAULT NULL,
  `id` varchar(20) DEFAULT NULL,
  `channel_name` varchar(45) DEFAULT NULL,
  `agent` varchar(45) DEFAULT NULL,
  `today_Acquisition` varchar(45) DEFAULT NULL,
  `Retention0` varchar(45) DEFAULT NULL,
  `Retention1` varchar(45) DEFAULT NULL,
  `Retention2` varchar(45) DEFAULT NULL,
  `Retention3` varchar(45) DEFAULT NULL,
  `Retention4` varchar(45) DEFAULT NULL,
  `Retention5` varchar(45) DEFAULT NULL,
  `Retention6` varchar(45) DEFAULT NULL,
  `Retention7` varchar(45) DEFAULT NULL,
  `Retention8` varchar(45) DEFAULT NULL,
  `Retention9` varchar(45) DEFAULT NULL,
  `Retention10` varchar(45) DEFAULT NULL,
  `Retention11` varchar(45) DEFAULT NULL,
  `Retention12` varchar(45) DEFAULT NULL,
  `Retention13` varchar(45) DEFAULT NULL,
  `Retention14` varchar(45) DEFAULT NULL,
  `Retention15` varchar(45) DEFAULT NULL,
  `Retention16` varchar(45) DEFAULT NULL,
  `Retention17` varchar(45) DEFAULT NULL,
  `Retention18` varchar(45) DEFAULT NULL,
  `Retention19` varchar(45) DEFAULT NULL,
  `Retention20` varchar(45) DEFAULT NULL,
  `Retention21` varchar(45) DEFAULT NULL,
  `Retention22` varchar(45) DEFAULT NULL,
  `Retention23` varchar(45) DEFAULT NULL,
  `Retention24` varchar(45) DEFAULT NULL,
  `Retention25` varchar(45) DEFAULT NULL,
  `Retention26` varchar(45) DEFAULT NULL,
  `Retention27` varchar(45) DEFAULT NULL,
  `Retention28` varchar(45) DEFAULT NULL,
  `Retention29` varchar(45) DEFAULT NULL,
  `Retention30` varchar(45) DEFAULT NULL,
  `Retention31` varchar(45) DEFAULT NULL,
  `Retention32` varchar(45) DEFAULT NULL,
  `Retention33` varchar(45) DEFAULT NULL,
  `Retention34` varchar(45) DEFAULT NULL,
  `Retention35` varchar(45) DEFAULT NULL,
  `Retention36` varchar(45) DEFAULT NULL,
  `Retention37` varchar(45) DEFAULT NULL,
  `Retention38` varchar(45) DEFAULT NULL,
  `Retention39` varchar(45) DEFAULT NULL,
  `Retention40` varchar(45) DEFAULT NULL,
  `Retention41` varchar(45) DEFAULT NULL,
  `Retention42` varchar(45) DEFAULT NULL,
  `Retention43` varchar(45) DEFAULT NULL,
  `Retention44` varchar(45) DEFAULT NULL,
  `Retention45` varchar(45) DEFAULT NULL,
  `Retention46` varchar(45) DEFAULT NULL,
  `Retention47` varchar(45) DEFAULT NULL,
  `Retention48` varchar(45) DEFAULT NULL,
  `Retention49` varchar(45) DEFAULT NULL,
  `Retention50` varchar(45) DEFAULT NULL,
  `Retention51` varchar(45) DEFAULT NULL,
  `Retention52` varchar(45) DEFAULT NULL,
  `Retention53` varchar(45) DEFAULT NULL,
  `Retention54` varchar(45) DEFAULT NULL,
  `Retention55` varchar(45) DEFAULT NULL,
  `Retention56` varchar(45) DEFAULT NULL,
  `Retention57` varchar(45) DEFAULT NULL,
  `Retention58` varchar(45) DEFAULT NULL,
  `Retention59` varchar(45) DEFAULT NULL,
  `Retention60` varchar(45) DEFAULT NULL,
  `Retention61` varchar(45) DEFAULT NULL,
  `Retention62` varchar(45) DEFAULT NULL,
  `Retention63` varchar(45) DEFAULT NULL,
  `Retention64` varchar(45) DEFAULT NULL,
  `Retention65` varchar(45) DEFAULT NULL,
  `Retention66` varchar(45) DEFAULT NULL,
  `Retention67` varchar(45) DEFAULT NULL,
  `Retention68` varchar(45) DEFAULT NULL,
  `Retention69` varchar(45) DEFAULT NULL,
  `Retention70` varchar(45) DEFAULT NULL,
  `Retention71` varchar(45) DEFAULT NULL,
  `Retention72` varchar(45) DEFAULT NULL,
  `Retention73` varchar(45) DEFAULT NULL,
  `Retention74` varchar(45) DEFAULT NULL,
  `Retention75` varchar(45) DEFAULT NULL,
  `Retention76` varchar(45) DEFAULT NULL,
  `Retention77` varchar(45) DEFAULT NULL,
  `Retention78` varchar(45) DEFAULT NULL,
  `Retention79` varchar(45) DEFAULT NULL,
  `Retention80` varchar(45) DEFAULT NULL,
  `Retention81` varchar(45) DEFAULT NULL,
  `Retention82` varchar(45) DEFAULT NULL,
  `Retention83` varchar(45) DEFAULT NULL,
  `Retention84` varchar(45) DEFAULT NULL,
  `Retention85` varchar(45) DEFAULT NULL,
  `Retention86` varchar(45) DEFAULT NULL,
  `Retention87` varchar(45) DEFAULT NULL,
  `Retention88` varchar(45) DEFAULT NULL,
  `Retention89` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `spend`
--

DROP TABLE IF EXISTS `spend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spend` (
  `id` varchar(20) DEFAULT NULL,
  `date` datetime NOT NULL,
  `gamename` varchar(45) DEFAULT NULL,
  `platform` varchar(45) DEFAULT NULL,
  `class_A` varchar(45) DEFAULT NULL,
  `channel_name` varchar(45) DEFAULT NULL,
  `agent` varchar(45) DEFAULT NULL,
  `class_ad` varchar(45) DEFAULT NULL,
  `today_budget` varchar(45) DEFAULT NULL,
  `today_spend` varchar(45) DEFAULT NULL,
  `discount` varchar(45) DEFAULT NULL,
  `dis_count2` varchar(45) DEFAULT NULL,
  `dis_spend` varchar(45) DEFAULT NULL,
  `staff` varchar(45) DEFAULT NULL,
  `update_time` varchar(45) DEFAULT NULL,
  `update_name` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `temp1`
--

DROP TABLE IF EXISTS `temp1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `temp1` (
  `DATE` varchar(10) DEFAULT NULL,
  `staff` varchar(45) DEFAULT NULL,
  `channel_name` varchar(45) DEFAULT NULL,
  `agent` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `sys_up_time` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL COMMENT '0,正常:1,初始化状态;2,失效状态',
  `user_up_time` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-13 10:02:52
