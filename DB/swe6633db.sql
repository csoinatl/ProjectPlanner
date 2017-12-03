-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 03, 2017 at 06:35 PM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `swe6633db`
--

-- --------------------------------------------------------

--
-- Table structure for table `projecthours`
--

DROP TABLE IF EXISTS `projecthours`;
CREATE TABLE IF NOT EXISTS `projecthours` (
  `projectID` bigint(10) NOT NULL,
  `reqID` bigint(10) NOT NULL,
  `teamMemberID` bigint(10) NOT NULL,
  `analysisHours` int(5) NOT NULL,
  `designHours` int(5) NOT NULL,
  `developmentHours` int(5) NOT NULL,
  `testingHours` int(5) NOT NULL,
  `managementHours` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projectrisks`
--

DROP TABLE IF EXISTS `projectrisks`;
CREATE TABLE IF NOT EXISTS `projectrisks` (
  `projectID` bigint(10) NOT NULL,
  `riskID` bigint(10) NOT NULL,
  `riskDesc` varchar(200) NOT NULL,
  `riskPriority` int(10) NOT NULL,
  `riskStatus` varchar(30) NOT NULL,
  PRIMARY KEY (`riskID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
CREATE TABLE IF NOT EXISTS `projects` (
  `projectID` bigint(10) NOT NULL,
  `projectName` varchar(100) NOT NULL,
  `projectDesc` varchar(1000) NOT NULL,
  `projectOwner` varchar(100) NOT NULL,
  `projectTeam` varchar(10000) NOT NULL,
  `startDate` varchar(11) NOT NULL,
  `endDate` varchar(11) NOT NULL,
  PRIMARY KEY (`projectID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projectteam`
--

DROP TABLE IF EXISTS `projectteam`;
CREATE TABLE IF NOT EXISTS `projectteam` (
  `projectID` bigint(10) NOT NULL,
  `teamMemberID` bigint(10) NOT NULL,
  `teamMemberName` varchar(100) NOT NULL,
  `designation` varchar(30) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `requirements`
--

DROP TABLE IF EXISTS `requirements`;
CREATE TABLE IF NOT EXISTS `requirements` (
  `projectID` bigint(10) NOT NULL,
  `reqID` bigint(10) NOT NULL,
  `requirements` varchar(200) NOT NULL,
  `reqType` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
