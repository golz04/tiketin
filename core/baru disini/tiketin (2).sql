-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2021 at 01:12 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tiketin`
--

-- --------------------------------------------------------

--
-- Table structure for table `chairs`
--

CREATE TABLE `chairs` (
  `id_chair` int(5) NOT NULL,
  `chair_number` varchar(5) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `studio_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chairs`
--

INSERT INTO `chairs` (`id_chair`, `chair_number`, `status`, `studio_id`) VALUES
(114, 'A01', 1, 1),
(115, 'A02', 1, 1),
(116, 'A03', 1, 1),
(117, 'A04', 1, 1),
(118, 'A05', 1, 1),
(119, 'A06', 0, 1),
(120, 'A07', 0, 1),
(121, 'A08', 0, 1),
(122, 'A09', 0, 1),
(123, 'A010', 0, 1),
(124, 'A011', 0, 1),
(125, 'A012', 0, 1),
(126, 'A013', 0, 1),
(127, 'A014', 0, 1),
(128, 'A015', 0, 1),
(129, 'B01', 0, 2),
(130, 'B02', 0, 2),
(131, 'B03', 0, 2),
(132, 'B04', 0, 2),
(133, 'B05', 0, 2),
(134, 'B06', 0, 2),
(135, 'B07', 0, 2),
(136, 'B08', 0, 2),
(137, 'B09', 0, 2),
(138, 'B010', 0, 2),
(139, 'B011', 0, 2),
(140, 'B012', 0, 2),
(141, 'B013', 0, 2),
(142, 'B014', 0, 2),
(143, 'B015', 0, 2),
(144, 'Y01', 0, 3),
(145, 'Y02', 0, 3),
(146, 'Y03', 0, 3),
(147, 'Y04', 0, 3),
(148, 'Y05', 0, 3),
(149, 'Y06', 0, 3),
(150, 'Y07', 0, 3),
(151, 'Y08', 0, 3),
(152, 'Y09', 0, 3),
(153, 'Y010', 0, 3),
(154, 'Y011', 0, 3),
(155, 'Y012', 0, 3),
(156, 'Y013', 0, 3),
(157, 'Y014', 0, 3),
(158, 'Y015', 0, 3);

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

CREATE TABLE `companies` (
  `id_company` int(5) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `companies`
--

INSERT INTO `companies` (`id_company`, `company_name`, `address`) VALUES
(1, 'Universal studios', 'US'),
(2, '20th century studios', 'LA'),
(3, 'Warner Bros', 'California'),
(4, 'The Walt Disney Company', 'Burbank, California.');

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

CREATE TABLE `genres` (
  `id_genre` smallint(2) NOT NULL,
  `genre_name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `genres`
--

INSERT INTO `genres` (`id_genre`, `genre_name`) VALUES
(1, 'action'),
(2, 'drama'),
(3, 'horror'),
(4, 'animasi'),
(5, 'romance');

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `code_film` int(10) NOT NULL,
  `title` varchar(50) NOT NULL,
  `genre_id` smallint(2) NOT NULL,
  `company_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`code_film`, `title`, `genre_id`, `company_id`) VALUES
(1, 'TENET', 1, 3),
(2, 'babadook', 3, 1),
(3, 'Aku Bukan Milik Mu', 2, 1),
(5, 'Post Malone', 1, 4),
(6, 'Souls', 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `schedules`
--

CREATE TABLE `schedules` (
  `id_schedule` int(5) NOT NULL,
  `date_schedule` date NOT NULL DEFAULT current_timestamp(),
  `start` time NOT NULL,
  `end` time NOT NULL,
  `film_code` int(10) NOT NULL,
  `id_studio` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `schedules`
--

INSERT INTO `schedules` (`id_schedule`, `date_schedule`, `start`, `end`, `film_code`, `id_studio`) VALUES
(1, '2020-12-17', '09:00:00', '11:00:00', 1, 1),
(3, '2000-12-26', '10:00:00', '13:00:00', 5, 2),
(4, '2020-12-27', '10:00:00', '12:00:00', 3, 3),
(7, '2020-12-30', '18:00:00', '21:00:00', 3, 1),
(8, '2021-01-01', '10:00:00', '14:00:00', 1, 1),
(9, '2021-01-02', '10:10:00', '12:00:00', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `studios`
--

CREATE TABLE `studios` (
  `id_studio` int(5) NOT NULL,
  `studio_name` varchar(10) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studios`
--

INSERT INTO `studios` (`id_studio`, `studio_name`, `description`) VALUES
(1, 'ARJUNA', ''),
(2, 'BIMA', ''),
(3, 'YUDHISTIRA', '');

-- --------------------------------------------------------

--
-- Table structure for table `tickets`
--

CREATE TABLE `tickets` (
  `code_ticket` int(10) NOT NULL,
  `chair_id` int(5) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tickets`
--

INSERT INTO `tickets` (`code_ticket`, `chair_id`, `price`) VALUES
(81269, 118, 75000),
(82020, 117, 75000);

-- --------------------------------------------------------

--
-- Table structure for table `toppings`
--

CREATE TABLE `toppings` (
  `id_topping` int(5) NOT NULL,
  `topping_name` varchar(20) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `toppings`
--

INSERT INTO `toppings` (`id_topping`, `topping_name`, `price`) VALUES
(1, 'popcorn', 35000),
(3, 'corndog', 25000),
(4, 'air mineral', 10000),
(5, 'Coca-Cola', 10000),
(6, 'Vanilla Tea', 10000),
(7, 'cheetos', 10000);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `code_transaction` varchar(20) NOT NULL,
  `order_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `operator_id` int(5) NOT NULL,
  `customer_id` int(5) NOT NULL,
  `ticket_code` int(10) NOT NULL,
  `topping_id` int(5) NOT NULL,
  `schedule_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`code_transaction`, `order_date`, `operator_id`, `customer_id`, `ticket_code`, `topping_id`, `schedule_id`) VALUES
('28214', '2021-01-02 00:00:40', 0, 25, 82020, 1, 9),
('36114', '2021-01-02 00:06:30', 0, 25, 81269, 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id_user` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(32) NOT NULL,
  `gender` enum('L','P') NOT NULL,
  `contact` varchar(13) NOT NULL,
  `address` text NOT NULL,
  `role_id` smallint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id_user`, `name`, `username`, `password`, `gender`, `contact`, `address`, `role_id`) VALUES
(1, 'admin', 'admin', 'admin', 'L', 'admin', '', 1),
(24, 'asd', 'asd', 'asd', 'L', 'asd', 'asd', 1),
(25, 'avi', 'qwe', 'qwe', 'L', 'qwe', 'blitar', 2),
(28, 'opi', 'opii', 'opii', 'L', 'asd', 'asd', 2),
(29, 'yupi', 'yupi', 'yupi', 'P', 'asd', 'asd', 2),
(30, 'kevin', 'kevin', 'kevin', 'L', 'qwe', 'qwe', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user_balances`
--

CREATE TABLE `user_balances` (
  `id_balance` int(5) NOT NULL,
  `id_user` int(5) NOT NULL,
  `amount` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_balances`
--

INSERT INTO `user_balances` (`id_balance`, `id_user`, `amount`) VALUES
(16, 24, 0),
(17, 25, 25000),
(20, 28, 0),
(21, 29, 84957),
(22, 30, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user_roles`
--

CREATE TABLE `user_roles` (
  `id_role` smallint(1) NOT NULL,
  `role_name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_roles`
--

INSERT INTO `user_roles` (`id_role`, `role_name`) VALUES
(1, 'admin'),
(2, 'costumer'),
(3, 'operator');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chairs`
--
ALTER TABLE `chairs`
  ADD PRIMARY KEY (`id_chair`),
  ADD KEY `studio_id` (`studio_id`);

--
-- Indexes for table `companies`
--
ALTER TABLE `companies`
  ADD PRIMARY KEY (`id_company`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id_genre`);

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`code_film`),
  ADD KEY `genre_id` (`genre_id`),
  ADD KEY `company_id` (`company_id`);

--
-- Indexes for table `schedules`
--
ALTER TABLE `schedules`
  ADD PRIMARY KEY (`id_schedule`),
  ADD KEY `film_code` (`film_code`),
  ADD KEY `id_studio` (`id_studio`);

--
-- Indexes for table `studios`
--
ALTER TABLE `studios`
  ADD PRIMARY KEY (`id_studio`);

--
-- Indexes for table `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`code_ticket`),
  ADD KEY `chair_id` (`chair_id`);

--
-- Indexes for table `toppings`
--
ALTER TABLE `toppings`
  ADD PRIMARY KEY (`id_topping`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`code_transaction`),
  ADD KEY `operator_id` (`operator_id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `ticket_code` (`ticket_code`),
  ADD KEY `schedule_id` (`schedule_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `user_balances`
--
ALTER TABLE `user_balances`
  ADD PRIMARY KEY (`id_balance`),
  ADD UNIQUE KEY `id_user_2` (`id_user`),
  ADD KEY `id_user` (`id_user`);

--
-- Indexes for table `user_roles`
--
ALTER TABLE `user_roles`
  ADD PRIMARY KEY (`id_role`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chairs`
--
ALTER TABLE `chairs`
  MODIFY `id_chair` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=159;

--
-- AUTO_INCREMENT for table `companies`
--
ALTER TABLE `companies`
  MODIFY `id_company` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `id_genre` smallint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `code_film` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `schedules`
--
ALTER TABLE `schedules`
  MODIFY `id_schedule` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `studios`
--
ALTER TABLE `studios`
  MODIFY `id_studio` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tickets`
--
ALTER TABLE `tickets`
  MODIFY `code_ticket` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT for table `toppings`
--
ALTER TABLE `toppings`
  MODIFY `id_topping` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `user_balances`
--
ALTER TABLE `user_balances`
  MODIFY `id_balance` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `user_roles`
--
ALTER TABLE `user_roles`
  MODIFY `id_role` smallint(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chairs`
--
ALTER TABLE `chairs`
  ADD CONSTRAINT `chairs_ibfk_1` FOREIGN KEY (`studio_id`) REFERENCES `studios` (`id_studio`);

--
-- Constraints for table `movies`
--
ALTER TABLE `movies`
  ADD CONSTRAINT `movies_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id_genre`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `movies_ibfk_2` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id_company`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `schedules`
--
ALTER TABLE `schedules`
  ADD CONSTRAINT `schedules_ibfk_1` FOREIGN KEY (`id_studio`) REFERENCES `studios` (`id_studio`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `schedules_ibfk_2` FOREIGN KEY (`film_code`) REFERENCES `movies` (`code_film`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `user_roles` (`id_role`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_balances`
--
ALTER TABLE `user_balances`
  ADD CONSTRAINT `user_balances_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
