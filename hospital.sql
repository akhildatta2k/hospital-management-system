-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2021 at 12:57 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `name_of_tablets` varchar(255) NOT NULL,
  `reference_number` varchar(255) NOT NULL,
  `dose` varchar(255) DEFAULT NULL,
  `no_of_tablets` varchar(255) DEFAULT NULL,
  `lot` varchar(255) DEFAULT NULL,
  `issue_date` varchar(255) DEFAULT NULL,
  `expire_date` varchar(255) DEFAULT NULL,
  `daily_dose` varchar(255) DEFAULT NULL,
  `side_effect` varchar(255) DEFAULT NULL,
  `furthur_information` varchar(255) DEFAULT NULL,
  `blood_pressure` varchar(255) DEFAULT NULL,
  `storage` varchar(255) DEFAULT NULL,
  `medication` varchar(255) DEFAULT NULL,
  `patient_id` varchar(255) DEFAULT NULL,
  `nhs_number` varchar(255) DEFAULT NULL,
  `patient_name` varchar(255) DEFAULT NULL,
  `date_of_birth` varchar(255) DEFAULT NULL,
  `patient_address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital`
--



--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD UNIQUE KEY `reference_number` (`reference_number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
