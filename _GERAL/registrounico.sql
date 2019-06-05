-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 26-Maio-2019 às 23:51
-- Versão do servidor: 10.1.40-MariaDB
-- versão do PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registrounico`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `consulta`
--

CREATE TABLE `consulta` (
  `cd_consulta` int(11) NOT NULL,
  `cd_paciente` int(11) NOT NULL,
  `dt_consulta` datetime DEFAULT NULL,
  `ds_consulta_motivo` varchar(400) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `consulta`
--

INSERT INTO `consulta` (`cd_consulta`, `cd_paciente`, `dt_consulta`, `ds_consulta_motivo`) VALUES
(1, 1, '2019-05-20 00:00:00', 'Dor no estomago'),
(2, 1, '2018-06-18 00:00:00', 'dor de cabeca');

-- --------------------------------------------------------

--
-- Estrutura da tabela `laudo`
--

CREATE TABLE `laudo` (
  `cd_laudo` int(11) NOT NULL,
  `cd_consulta` int(11) NOT NULL,
  `ds_laudo` varchar(400) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura da tabela `paciente`
--

CREATE TABLE `paciente` (
  `cd_paciente` int(11) NOT NULL,
  `ds_paciente_nome` varchar(400) DEFAULT NULL,
  `ds_paciente_cpf` varchar(200) DEFAULT NULL,
  `ds_paciente_endereco` varchar(400) DEFAULT NULL,
  `dt_paciente_nascimento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `paciente`
--

INSERT INTO `paciente` (`cd_paciente`, `ds_paciente_nome`, `ds_paciente_cpf`, `ds_paciente_endereco`, `dt_paciente_nascimento`) VALUES
(1, 'Gabriel Nascimento de Oliveira', '16094715713', 'rua gardenia, n 10, campinho da serra 1', '1997-11-30'),
(2, 'Rafael Arcanjo', '99999999999', 'rua das rosas, n 43, colina de laranjeiras', '1995-12-30'),
(3, 'Gabriel 123 sdf', '11111111111', 'rua das dores, n 666, bairro infernal, Espirito amaldicoado', '1995-11-30'),
(11, ' sdadas ', '12312312', 'dsadsad', '1999-05-30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`cd_consulta`);

--
-- Indexes for table `laudo`
--
ALTER TABLE `laudo`
  ADD PRIMARY KEY (`cd_laudo`);

--
-- Indexes for table `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`cd_paciente`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `consulta`
--
ALTER TABLE `consulta`
  MODIFY `cd_consulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `laudo`
--
ALTER TABLE `laudo`
  MODIFY `cd_laudo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paciente`
--
ALTER TABLE `paciente`
  MODIFY `cd_paciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
