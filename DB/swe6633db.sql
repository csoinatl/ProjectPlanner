-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 12, 2017 at 05:21 AM
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
-- Table structure for table `functionalrequirements`
--

DROP TABLE IF EXISTS `functionalrequirements`;
CREATE TABLE IF NOT EXISTS `functionalrequirements` (
  `projectID` bigint(10) NOT NULL,
  `fRequirement` varchar(200) NOT NULL,
  `fReqAnalysisHours` int(5) NOT NULL,
  `fReqDesignHours` int(5) NOT NULL,
  `fReqDevelopmentHours` int(5) NOT NULL,
  `fReqTestingHours` int(5) NOT NULL,
  `fReqManagementHours` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `nonfunctionalrequirements`
--

DROP TABLE IF EXISTS `nonfunctionalrequirements`;
CREATE TABLE IF NOT EXISTS `nonfunctionalrequirements` (
  `projectID` bigint(10) NOT NULL,
  `nonFunctionalRequirements` int(11) NOT NULL,
  `nFRAnalysisHours` int(5) NOT NULL,
  `nFRDesignHours` int(5) NOT NULL,
  `nFRDevelopmentHours` int(5) NOT NULL,
  `nFRTestingHours` int(5) NOT NULL,
  `nFRManagementHours` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
CREATE TABLE IF NOT EXISTS `projects` (
  `projectID` bigint(10) NOT NULL,
  `projectName` varchar(100) NOT NULL,
  `projectOwner` varchar(100) NOT NULL,
  `projectTeam` varchar(1000) NOT NULL,
  PRIMARY KEY (`projectID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projectteam`
--

DROP TABLE IF EXISTS `projectteam`;
CREATE TABLE IF NOT EXISTS `projectteam` (
  `projectID` bigint(10) NOT NULL,
  `designation` varchar(30) NOT NULL,
  `analysisHours` int(5) NOT NULL,
  `designHours` int(5) NOT NULL,
  `developmentHours` int(5) NOT NULL,
  `testingHours` int(5) NOT NULL,
  `managementHours` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS 'projectteamperson';
CREATE TABLE IF NOT EXISTS 'projectteamperson' (
	'projectID' bigint(10) not NULL,
	'idperson' INT not null
)

-- --------------------------------------------------------

--
-- Table structure for table `projecttools`
--

DROP TABLE IF EXISTS `projecttools`;
CREATE TABLE IF NOT EXISTS `projecttools` (
  `projectID` bigint(10) NOT NULL,
  `analysisTools` varchar(50) NOT NULL,
  `designTools` varchar(50) NOT NULL,
  `developmentTools` varchar(50) NOT NULL,
  `testingTools` varchar(50) NOT NULL,
  `managementTools` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


DROP TABLE IF EXISTS 'person'
CREATE TABLE `person` (
  `idperson` INT NOT NULL,
  `first_name` VARCHAR(40) NULL,
  `last_name` VARCHAR(40) NULL,
  `title` VARCHAR(40) NULL,
  PRIMARY KEY (`idperson`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1
COMMENT = 'Person information Table';
COMMIT;
