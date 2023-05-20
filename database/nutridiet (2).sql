-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2023 at 07:36 PM
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
-- Database: `nutridiet`
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
-- Table structure for table `dietplan`
--

CREATE TABLE `dietplan` (
  `id` int(11) NOT NULL,
  `tdee` float NOT NULL,
  `breakfast` varchar(100) NOT NULL,
  `snack1` varchar(100) NOT NULL,
  `lunch` varchar(100) NOT NULL,
  `snack2` varchar(100) NOT NULL,
  `dinner` varchar(100) NOT NULL,
  `snack3` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `diet_plan_model`
--

CREATE TABLE `diet_plan_model` (
  `tdee` double NOT NULL,
  `breakfast` varchar(500) NOT NULL,
  `snack1` varchar(500) NOT NULL,
  `lunch` varchar(500) NOT NULL,
  `snack2` varchar(500) NOT NULL,
  `dinner` varchar(500) NOT NULL,
  `snack3` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diet_plan_model`
--

INSERT INTO `diet_plan_model` (`tdee`, `breakfast`, `snack1`, `lunch`, `snack2`, `dinner`, `snack3`) VALUES
(1933.8, 'Cooked meat(85g), Banana', 'Cottage cheese (125g)', 'Yogurt(1 cup), Any vegetable(80g), Leafy greens, Small handful of nuts, Half Large Potato(75g), Bana', 'Flavored yogurt(125g), Leafy greens(Any Amount)', 'Cooked fish(100g), 2 vegetables 80g, Leafy Greens, Cooked Grain(150g), 2 TSP (10 ml) olive oil, Cook', 'Orange');

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
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `loginid` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `age` int(3) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Height` float NOT NULL,
  `weight` float NOT NULL,
  `BMI` double NOT NULL,
  `Status` varchar(10) NOT NULL,
  `med_history` varchar(20) NOT NULL,
  `pregnancy_status` varchar(50) NOT NULL,
  `medical_condition` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`loginid`, `id`, `age`, `Gender`, `Height`, `weight`, `BMI`, `Status`, `med_history`, `pregnancy_status`, `medical_condition`) VALUES
(1, 1, 22, 'Female', 173, 51, 17.040000915527344, 'Underweigh', '[value-9]', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `name` text NOT NULL,
  `weight` float NOT NULL,
  `height` float NOT NULL,
  `age` int(11) NOT NULL,
  `gender` text NOT NULL,
  `phys_act` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`name`, `weight`, `height`, `age`, `gender`, `phys_act`) VALUES
('fatima', 51, 163, 23, '0', 'value1'),
('esha', 60, 170, 22, '0', 'value2'),
('ali', 70, 180, 22, 'Male', 'value3'),
('Fatima', 51, 170, 23, 'Female', 'value2'),
('Usama', 80, 180, 25, 'Male', 'value2'),
('Huma', 80, 170, 25, 'Female', 'value1');

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
(4, 'esha123@gmail.com', 'esha1122', 'esha1122');

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
-- Indexes for table `dietplan`
--
ALTER TABLE `dietplan`
  ADD UNIQUE KEY `id_2` (`id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `query`
--
ALTER TABLE `query`
  ADD PRIMARY KEY (`queryid`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`loginid`),
  ADD KEY `id` (`id`);

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
-- AUTO_INCREMENT for table `query`
--
ALTER TABLE `query`
  MODIFY `queryid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `loginid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_login`
--
ALTER TABLE `user_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD CONSTRAINT `admin_login_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`);

--
-- Constraints for table `dietplan`
--
ALTER TABLE `dietplan`
  ADD CONSTRAINT `dietplan_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`);

--
-- Constraints for table `query`
--
ALTER TABLE `query`
  ADD CONSTRAINT `query_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_login` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
