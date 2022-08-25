-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 25, 2022 at 01:57 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_monitoring_siswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('7ce4954c2d18');

-- --------------------------------------------------------

--
-- Table structure for table `tb_guru_detail`
--

CREATE TABLE `tb_guru_detail` (
  `guru_ID` int(11) NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `nip` varchar(32) NOT NULL,
  `nama_depan` varchar(128) NOT NULL,
  `nama_belakang` varchar(128) NOT NULL,
  `jenis_kelamin` varchar(64) NOT NULL,
  `alamat` varchar(256) DEFAULT NULL,
  `agama` varchar(32) DEFAULT NULL,
  `mapel_id` int(11) DEFAULT NULL,
  `kelas_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_guru_detail`
--

INSERT INTO `tb_guru_detail` (`guru_ID`, `user_id`, `nip`, `nama_depan`, `nama_belakang`, `jenis_kelamin`, `alamat`, `agama`, `mapel_id`, `kelas_id`) VALUES
(1, 10, '10111213', 'Abang', 'Icha', 'laki-laki', 'Jl. dr. Leimena', 'islam', NULL, NULL),
(2, 18, '10111213', 'Abang', 'Icha2', 'perempuan', 'Jl. dr. Leimena', 'islam', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tb_jadwal_belajar`
--

CREATE TABLE `tb_jadwal_belajar` (
  `jadwal_belajar_ID` int(11) NOT NULL,
  `siswa_id` int(10) UNSIGNED DEFAULT NULL,
  `mapel_id` int(11) NOT NULL,
  `hari` varchar(32) NOT NULL,
  `jam_mulai` varchar(32) NOT NULL,
  `jam_selesai` varchar(32) NOT NULL,
  `kelas_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_kelas`
--

CREATE TABLE `tb_kelas` (
  `kelas_ID` int(11) NOT NULL,
  `nama_kelas` varchar(128) NOT NULL,
  `jml_siswa` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_kelas`
--

INSERT INTO `tb_kelas` (`kelas_ID`, `nama_kelas`, `jml_siswa`) VALUES
(1, 'VII-1', NULL),
(2, 'VII-2', NULL),
(3, 'VII-3', NULL),
(4, 'VII-4', NULL),
(5, 'VII-5', NULL),
(6, 'VII-6', NULL),
(7, 'VII-7', NULL),
(8, 'VIII-1', NULL),
(9, 'VIII-2', NULL),
(10, 'VIII-3', NULL),
(11, 'VIII-4', NULL),
(12, 'VIII-5', NULL),
(13, 'VIII-6', NULL),
(14, 'VIII-7', NULL),
(15, 'VIII-8', NULL),
(16, 'IX-1', NULL),
(17, 'IX-2', NULL),
(18, 'IX-3', NULL),
(19, 'IX-4', NULL),
(20, 'IX-5', NULL),
(21, 'IX-6', NULL),
(22, 'IX-7', NULL),
(23, 'IX-8', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tb_mapel`
--

CREATE TABLE `tb_mapel` (
  `mapel_ID` int(11) NOT NULL,
  `mapel` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_mapel`
--

INSERT INTO `tb_mapel` (`mapel_ID`, `mapel`) VALUES
(1, 'ipa'),
(2, 'matematika'),
(3, 'bahasa indonesia'),
(4, 'bahasa inggris'),
(5, 'bahasa inggriss');

-- --------------------------------------------------------

--
-- Table structure for table `tb_mengajar`
--

CREATE TABLE `tb_mengajar` (
  `mengajar_ID` int(11) NOT NULL,
  `kode_mengajar` varchar(128) NOT NULL,
  `hari` varchar(32) NOT NULL,
  `guru_id` int(11) NOT NULL,
  `mapel_id` int(11) NOT NULL,
  `kelas_id` int(11) NOT NULL,
  `semester_id` int(11) NOT NULL,
  `th_ajaran_id` int(11) NOT NULL,
  `mulai` varchar(12) NOT NULL,
  `selesai` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_mengajar`
--

INSERT INTO `tb_mengajar` (`mengajar_ID`, `kode_mengajar`, `hari`, `guru_id`, `mapel_id`, `kelas_id`, `semester_id`, `th_ajaran_id`, `mulai`, `selesai`) VALUES
(1, 'MPL-533657', 'kamis', 1, 1, 2, 1, 1, '', ''),
(3, 'MPL-3356578', 'kamis', 2, 3, 3, 1, 1, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `tb_semester`
--

CREATE TABLE `tb_semester` (
  `semester_ID` int(11) NOT NULL,
  `semester` varchar(32) NOT NULL,
  `status` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_semester`
--

INSERT INTO `tb_semester` (`semester_ID`, `semester`, `status`) VALUES
(1, 'ganjil', '1'),
(2, 'genap', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tb_siswa_detail`
--

CREATE TABLE `tb_siswa_detail` (
  `siswa_ID` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `nama_depan` varchar(64) NOT NULL,
  `nama_belakang` varchar(64) NOT NULL,
  `nisn` varchar(32) NOT NULL,
  `tempat_lahir` varchar(64) DEFAULT NULL,
  `tanggal_lahir` varchar(64) DEFAULT NULL,
  `jenis_kelamin` varchar(32) NOT NULL,
  `agama` varchar(32) NOT NULL,
  `alamat` varchar(256) DEFAULT NULL,
  `nama_ayah` varchar(128) DEFAULT NULL,
  `nama_ibu` varchar(128) DEFAULT NULL,
  `foto_siswa` varchar(256) DEFAULT NULL,
  `kelas_id` int(11) DEFAULT NULL,
  `qr_code` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_siswa_detail`
--

INSERT INTO `tb_siswa_detail` (`siswa_ID`, `user_id`, `nama_depan`, `nama_belakang`, `nisn`, `tempat_lahir`, `tanggal_lahir`, `jenis_kelamin`, `agama`, `alamat`, `nama_ayah`, `nama_ibu`, `foto_siswa`, `kelas_id`, `qr_code`) VALUES
(2, 15, 'Dahlan', 'Al Ghazaly', '123456', NULL, NULL, 'pria', 'islam', NULL, NULL, NULL, NULL, 1, 'Dahlan_e10adc3949ba59abbe56e057f20f883e.png'),
(3, 17, 'Nancy', 'Momoland', '02468', NULL, NULL, 'wanita', 'islam', NULL, NULL, NULL, NULL, 3, 'Nancy_8f562a872c4a1ee488c27a3c40215e57.png');

-- --------------------------------------------------------

--
-- Table structure for table `tb_tahun_ajaran`
--

CREATE TABLE `tb_tahun_ajaran` (
  `tahun_ajaran_ID` int(11) NOT NULL,
  `tahun_ajaran` varchar(32) NOT NULL,
  `status` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_tahun_ajaran`
--

INSERT INTO `tb_tahun_ajaran` (`tahun_ajaran_ID`, `tahun_ajaran`, `status`) VALUES
(1, '2021/2022', '1'),
(2, '2022/2023', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tb_user`
--

CREATE TABLE `tb_user` (
  `ID` int(10) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL,
  `group` varchar(32) NOT NULL,
  `password` varchar(256) NOT NULL,
  `create_on` datetime DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `active` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`ID`, `username`, `group`, `password`, `create_on`, `last_login`, `active`) VALUES
(2, 'admin', 'admin', '$2b$12$hA/8LWDwyvC8Ge6CsWf3COEOccKOMwW.5i9vna7PQav3p1FqHTLti', '2022-08-05 14:57:19', '2022-08-19 11:21:25', 1),
(8, '0852', 'siswa', '$2b$12$MiLByG892gyNAhIzEYf3eOJAzXpoPH9Fs61Q7cZFKqkB2DFwIoxPu', '2022-08-10 17:53:06', '2022-08-14 23:34:49', 1),
(10, '10111213', 'guru', '$2b$12$2CeqshCzVo/shsVBD6Nq7uEZthoxNbEiihxEoLY8tdSHVVwqi7DT6', '2022-08-14 22:46:32', '2022-08-15 02:10:24', 1),
(15, '123456', 'siswa', '$2b$12$OTXeIobl4jEvSiH/Sbxdm.6hINTz2nOve39eI7yU/N/dbFapKmT02', '2022-08-15 02:22:53', '2022-08-17 07:57:07', 1),
(17, '02468', 'siswa', '$2b$12$cW0cJjOMrr.oFmGWvAjr0ealQU46vNQ8Q171BNOK33AcW/TrAfg/O', '2022-08-17 07:56:30', '2022-08-25 10:51:02', 1),
(18, '19970821', 'guru', '$2b$12$dQ9o3Ko9eTWA1c/on.RdyevQLg1Lelzhl7lXD7TrH9OsbIdV0SxZe', '2022-08-24 09:44:47', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_user_detail`
--

CREATE TABLE `tb_user_detail` (
  `user_detail_ID` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `nama_depan` varchar(128) NOT NULL,
  `nama_belakang` varchar(128) NOT NULL,
  `jenis_kelamin` varchar(32) NOT NULL,
  `alamat` varchar(256) NOT NULL,
  `telp` varchar(13) DEFAULT NULL,
  `profil_picture` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_user_detail`
--

INSERT INTO `tb_user_detail` (`user_detail_ID`, `user_id`, `nama_depan`, `nama_belakang`, `jenis_kelamin`, `alamat`, `telp`, `profil_picture`) VALUES
(1, 2, 'Ari2', 'Efendi', 'laki-laki', 'Jl. dr. Leimena', '085253886660', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tb_wali_kelas`
--

CREATE TABLE `tb_wali_kelas` (
  `wali_kelas_ID` int(11) NOT NULL,
  `guru_id` int(11) NOT NULL,
  `kelas_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `tb_guru_detail`
--
ALTER TABLE `tb_guru_detail`
  ADD PRIMARY KEY (`guru_ID`),
  ADD KEY `kelas_id` (`kelas_id`),
  ADD KEY `mapel_id` (`mapel_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tb_jadwal_belajar`
--
ALTER TABLE `tb_jadwal_belajar`
  ADD PRIMARY KEY (`jadwal_belajar_ID`),
  ADD KEY `kelas_id` (`kelas_id`),
  ADD KEY `mapel_id` (`mapel_id`),
  ADD KEY `siswa_id` (`siswa_id`);

--
-- Indexes for table `tb_kelas`
--
ALTER TABLE `tb_kelas`
  ADD PRIMARY KEY (`kelas_ID`);

--
-- Indexes for table `tb_mapel`
--
ALTER TABLE `tb_mapel`
  ADD PRIMARY KEY (`mapel_ID`);

--
-- Indexes for table `tb_mengajar`
--
ALTER TABLE `tb_mengajar`
  ADD PRIMARY KEY (`mengajar_ID`);

--
-- Indexes for table `tb_semester`
--
ALTER TABLE `tb_semester`
  ADD PRIMARY KEY (`semester_ID`);

--
-- Indexes for table `tb_siswa_detail`
--
ALTER TABLE `tb_siswa_detail`
  ADD PRIMARY KEY (`siswa_ID`),
  ADD KEY `kelas_id` (`kelas_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tb_tahun_ajaran`
--
ALTER TABLE `tb_tahun_ajaran`
  ADD PRIMARY KEY (`tahun_ajaran_ID`);

--
-- Indexes for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `tb_user_detail`
--
ALTER TABLE `tb_user_detail`
  ADD PRIMARY KEY (`user_detail_ID`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `tb_wali_kelas`
--
ALTER TABLE `tb_wali_kelas`
  ADD PRIMARY KEY (`wali_kelas_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_guru_detail`
--
ALTER TABLE `tb_guru_detail`
  MODIFY `guru_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_jadwal_belajar`
--
ALTER TABLE `tb_jadwal_belajar`
  MODIFY `jadwal_belajar_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_kelas`
--
ALTER TABLE `tb_kelas`
  MODIFY `kelas_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `tb_mapel`
--
ALTER TABLE `tb_mapel`
  MODIFY `mapel_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_mengajar`
--
ALTER TABLE `tb_mengajar`
  MODIFY `mengajar_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_semester`
--
ALTER TABLE `tb_semester`
  MODIFY `semester_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_siswa_detail`
--
ALTER TABLE `tb_siswa_detail`
  MODIFY `siswa_ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_tahun_ajaran`
--
ALTER TABLE `tb_tahun_ajaran`
  MODIFY `tahun_ajaran_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `tb_user_detail`
--
ALTER TABLE `tb_user_detail`
  MODIFY `user_detail_ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_wali_kelas`
--
ALTER TABLE `tb_wali_kelas`
  MODIFY `wali_kelas_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_guru_detail`
--
ALTER TABLE `tb_guru_detail`
  ADD CONSTRAINT `tb_guru_detail_ibfk_1` FOREIGN KEY (`kelas_id`) REFERENCES `tb_kelas` (`kelas_ID`),
  ADD CONSTRAINT `tb_guru_detail_ibfk_2` FOREIGN KEY (`mapel_id`) REFERENCES `tb_mapel` (`mapel_ID`),
  ADD CONSTRAINT `tb_guru_detail_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tb_jadwal_belajar`
--
ALTER TABLE `tb_jadwal_belajar`
  ADD CONSTRAINT `tb_jadwal_belajar_ibfk_1` FOREIGN KEY (`kelas_id`) REFERENCES `tb_kelas` (`kelas_ID`),
  ADD CONSTRAINT `tb_jadwal_belajar_ibfk_2` FOREIGN KEY (`mapel_id`) REFERENCES `tb_mapel` (`mapel_ID`),
  ADD CONSTRAINT `tb_jadwal_belajar_ibfk_3` FOREIGN KEY (`siswa_id`) REFERENCES `tb_siswa_detail` (`siswa_ID`);

--
-- Constraints for table `tb_siswa_detail`
--
ALTER TABLE `tb_siswa_detail`
  ADD CONSTRAINT `tb_siswa_detail_ibfk_1` FOREIGN KEY (`kelas_id`) REFERENCES `tb_kelas` (`kelas_ID`),
  ADD CONSTRAINT `tb_siswa_detail_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tb_user_detail`
--
ALTER TABLE `tb_user_detail`
  ADD CONSTRAINT `tb_user_detail_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
