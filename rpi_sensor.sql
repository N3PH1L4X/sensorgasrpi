-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 04-10-2022 a las 22:16:23
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `rpi_sensor`
--
CREATE DATABASE IF NOT EXISTS `rpi_sensor` DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci;
USE `rpi_sensor`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lectura`
--

DROP TABLE IF EXISTS `lectura`;
CREATE TABLE `lectura` (
  `id` int(250) NOT NULL,
  `temperatura` float NOT NULL,
  `humedad` float NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `lectura`
--
ALTER TABLE `lectura`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `lectura`
--
ALTER TABLE `lectura`
  MODIFY `id` int(250) NOT NULL AUTO_INCREMENT;
COMMIT;
