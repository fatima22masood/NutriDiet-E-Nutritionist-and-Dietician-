-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2023 at 12:05 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nutridieteshfa`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Admin_id` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `adlogin_id` int(11) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(10) NOT NULL,
  `Admin_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) DEFAULT NULL,
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(15) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(NULL, 1, 'Fatima', 'fatima22@gmail.com', '0432146536', 'hey', '2023-01-08 00:00:00'),
(NULL, 20, 'fatima masood', 'bsef19m020@gmail.com', '03435762672', 'i wana generate diet plan', NULL),
(NULL, 21, 'fatima', 'fatima22@gmail.com', '0432657432', 'hey i wana generate a diet plan', NULL),
(NULL, 22, 'NutriDiet', 'saba@gmail.com', '098787575', 'njf', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `diet_plan_model`
--

CREATE TABLE `diet_plan_model` (
  `plan_id` int(11) NOT NULL,
  `tdee` float NOT NULL,
  `breakfast` varchar(100) NOT NULL,
  `snack1` varchar(100) NOT NULL,
  `lunch` varchar(100) NOT NULL,
  `snack2` varchar(100) NOT NULL,
  `dinner` varchar(100) NOT NULL,
  `snack3` varchar(100) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diet_plan_model`
--

INSERT INTO `diet_plan_model` (`plan_id`, `tdee`, `breakfast`, `snack1`, `lunch`, `snack2`, `dinner`, `snack3`, `id`) VALUES
(1, 2260.21, 'Cooked meat(85g), Dried Fruit(Handfull), 2 corn tortillas', 'Low fat milk(250ml)', 'Yogurt(1 cup), Leafy greens(Any Amount), Leafy greens, 1/4 medium avocado, Oats(250g), Orange, 1 who', 'Hummus(4 Tbsp), Any vegetable(80g)', 'Cooked fish(100g), 2 vegetables 80g, Leafy Greens, Whole Grain Bread(1 slice), Small handful of nuts', 'Fruit Juice(125ml)', 5);

-- --------------------------------------------------------

--
-- Table structure for table `query`
--

CREATE TABLE `query` (
  `queryid` int(11) NOT NULL,
  `query` varchar(100) NOT NULL,
  `id` int(11) NOT NULL,
  `Admin id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `info_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `height` float NOT NULL,
  `weight` float NOT NULL,
  `phys_act` varchar(50) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`info_id`, `name`, `age`, `gender`, `height`, `weight`, `phys_act`, `id`) VALUES
(1, 'Esha Tahir', 22, 'Female', 173, 62, 'value3', 5);

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_login`
--

INSERT INTO `user_login` (`id`, `email`, `username`, `password`) VALUES
(1, '', '', ''),
(2, '', 'fatima123', 'fatima123@gmail.com'),
(3, '', 'usama1122@gmail.com', 'usama123'),
(4, 'esha123@gmail.com', 'esha1122', 'esha1122'),
(5, 'eshatahir19@gmail.com', 'esha2601', 'esha@2601');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_id`);

--
-- Indexes for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD PRIMARY KEY (`adlogin_id`),
  ADD KEY `Admin_id` (`Admin_id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `diet_plan_model`
--
ALTER TABLE `diet_plan_model`
  ADD PRIMARY KEY (`plan_id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `query`
--
ALTER TABLE `query`
  ADD PRIMARY KEY (`queryid`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`info_id`),
  ADD KEY `fk_user_login_id` (`id`);

--
-- Indexes for table `user_login`
--
ALTER TABLE `user_login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_login`
--
ALTER TABLE `admin_login`
  MODIFY `adlogin_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `diet_plan_model`
--
ALTER TABLE `diet_plan_model`
  MODIFY `plan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `query`
--
ALTER TABLE `query`
  MODIFY `queryid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_info`
--
ALTER TABLE `user_info`
  MODIFY `info_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_login`
--
ALTER TABLE `user_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD CONSTRAINT `admin_login_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`);

--
-- Constraints for table `diet_plan_model`
--
ALTER TABLE `diet_plan_model`
  ADD CONSTRAINT `diet_plan_model_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `query`
--
ALTER TABLE `query`
  ADD CONSTRAINT `query_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`);

--
-- Constraints for table `user_info`
--
ALTER TABLE `user_info`
  ADD CONSTRAINT `fk_user_login_id` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `user_info_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
