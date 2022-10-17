-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Окт 12 2022 г., 05:58
-- Версия сервера: 8.0.24
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `cars`
--

-- --------------------------------------------------------

--
-- Структура таблицы `cars`
--

CREATE TABLE `cars` (
  `id` bigint NOT NULL,
  `number_id` varchar(6) NOT NULL,
  `status_of_reservation` tinyint(1) NOT NULL DEFAULT '0',
  `car_manufacturer_id` bigint NOT NULL,
  `model_id` bigint NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `cars`
--

INSERT INTO `cars` (`id`, `number_id`, `status_of_reservation`, `car_manufacturer_id`, `model_id`, `price`) VALUES
(1, '600aaa', 1, 1, 1, 200),
(2, '600aab', 1, 3, 2, 250),
(3, '600abc', 0, 1, 1, 200),
(4, '600aan', 0, 1, 4, 240),
(5, '500aaa', 1, 3, 1, 240),
(6, '400aaa', 0, 3, 2, 280),
(7, '300aaa', 0, 3, 3, 380),
(8, '111aaa', 0, 7, 1, 140);

-- --------------------------------------------------------

--
-- Структура таблицы `car_canufacturer`
--

CREATE TABLE `car_canufacturer` (
  `car_manufacturer_id` bigint NOT NULL,
  `car_manufacturer_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `car_canufacturer`
--

INSERT INTO `car_canufacturer` (`car_manufacturer_id`, `car_manufacturer_name`) VALUES
(3, 'AUDI'),
(5, 'Bugatii'),
(7, 'Shevrolet\r\n'),
(1, 'Tesla');

-- --------------------------------------------------------

--
-- Структура таблицы `model`
--

CREATE TABLE `model` (
  `id` bigint NOT NULL,
  `model_of_car` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `model`
--

INSERT INTO `model` (`id`, `model_of_car`) VALUES
(2, 'model E'),
(3, 'model m\r\n'),
(4, 'Model S'),
(1, 'model X');

-- --------------------------------------------------------

--
-- Структура таблицы `reservation`
--

CREATE TABLE `reservation` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `car_id` varchar(10) NOT NULL,
  `data_get` date DEFAULT NULL,
  `data_return` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `reservation`
--

INSERT INTO `reservation` (`id`, `user_id`, `car_id`, `data_get`, `data_return`) VALUES
(9, 877411737, '600aaa', '2022-10-11', '2022-10-21'),
(15, 877411737, '500aaa', '2022-10-11', '2022-10-13'),
(16, 877411737, '600aab', '2022-10-11', '2022-10-14');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` bigint NOT NULL,
  `user_id_by_tg` bigint NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `passport_seriess` varchar(20) NOT NULL,
  `cantact_number` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `user_id_by_tg`, `fullname`, `passport_seriess`, `cantact_number`) VALUES
(5, 877411737, 'Joha', 'ad321332', 231312231);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number` (`number_id`),
  ADD KEY `car_manufacturer_id` (`car_manufacturer_id`),
  ADD KEY `model_id` (`model_id`);

--
-- Индексы таблицы `car_canufacturer`
--
ALTER TABLE `car_canufacturer`
  ADD PRIMARY KEY (`car_manufacturer_id`),
  ADD UNIQUE KEY `car_manufacturer_name` (`car_manufacturer_name`);

--
-- Индексы таблицы `model`
--
ALTER TABLE `model`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `model` (`model_of_car`);

--
-- Индексы таблицы `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `car_id` (`car_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pasport` (`passport_seriess`),
  ADD UNIQUE KEY `id_tg` (`user_id_by_tg`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `cars`
--
ALTER TABLE `cars`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `car_canufacturer`
--
ALTER TABLE `car_canufacturer`
  MODIFY `car_manufacturer_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `model`
--
ALTER TABLE `model`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `cars`
--
ALTER TABLE `cars`
  ADD CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`car_manufacturer_id`) REFERENCES `car_canufacturer` (`car_manufacturer_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `cars_ibfk_2` FOREIGN KEY (`model_id`) REFERENCES `model` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ограничения внешнего ключа таблицы `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id_by_tg`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `reservation_ibfk_3` FOREIGN KEY (`car_id`) REFERENCES `cars` (`number_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
