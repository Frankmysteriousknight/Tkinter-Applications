-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2019 at 09:52 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gadmart`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `UserId` varchar(20) NOT NULL,
  `ProdId` varchar(20) NOT NULL,
  `DateofPurchase` varchar(20) NOT NULL,
  `Price` varchar(20) NOT NULL,
  `Email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`UserId`, `ProdId`, `DateofPurchase`, `Price`, `Email`) VALUES
('exmpl123', 'Imac', '2019-2-28', '49999.0', 'example@some.com'),
('exmpl123', 'Imac', '2019-2-28', '49999.0', 'example@some.com'),
('exmpl123', 'Imac', '2019-2-28', '49999.0', 'example@some.com'),
('exmpl123', 'Imac', '2019-2-28', '49999.0', 'example@some.com'),
('exmpl123', 'Opt6', '2019-2-28', '43400.0', 'example@some.com'),
('exmpl123', 'boAtH', '2019-2-28', '1990.0', 'example@some.com'),
('exmpl123', 'Ps4', '2019-2-28', '39990.0', 'example@some.com');

-- --------------------------------------------------------

--
-- Table structure for table `prodinfo`
--

CREATE TABLE `prodinfo` (
  `ProdId` varchar(5) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Price` float(7,2) NOT NULL,
  `Quantity` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prodinfo`
--

INSERT INTO `prodinfo` (`ProdId`, `Name`, `Price`, `Quantity`) VALUES
('boAtH', 'boAt 510', 1990.00, 11),
('Imac', 'IMAC 2019', 49999.00, 11),
('Opt6', 'OnePlus 6t', 43400.00, 11),
('Ps4', 'Play Station 4', 39990.00, 11);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Address` varchar(60) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `DateofBirth` date DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Username`, `Password`, `Name`, `Address`, `Mobile`, `DateofBirth`, `Email`) VALUES
('kritik123', 'qwerty', 'KritikSharma', 'Vapalli Nagar', '785412369', '1998-04-11', 'kritik@gmail.com'),
('mohit123', 'mohit', 'MohitKumar', 'Jaipur Nagar', '9632587412', '1998-02-04', 'mohit@gmail.com'),
('yash123', 'redhat', 'YashMathur', 'Bais Godam', '7896541335', '1998-07-06', 'yashmthr@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `prodinfo`
--
ALTER TABLE `prodinfo`
  ADD PRIMARY KEY (`ProdId`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`Username`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
