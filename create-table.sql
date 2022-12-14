CREATE TABLE IF NOT EXISTS `METER` (
  `ID` INT(11) NOT NULL,
  `TIMESTAMP` DATETIME DEFAULT NULL,
  `TOTAL_DELIVERY_LOW_KWH` DECIMAL(10,3) DEFAULT NULL,
  `TOTAL_DELIVERY_HIGH_KWH` DECIMAL(10,3) DEFAULT NULL,
  `TOTAL_BACKDELIVERY_LOW_KWH` DECIMAL(10,3) DEFAULT NULL,
  `TOTAL_BACKDELIVERY_HIGH_KWH` DECIMAL(10,3) DEFAULT NULL,
  `TARIFF_INDICATOR` int(11) DEFAULT NULL,
  `ACTUAL_DELIVERY_KW` DECIMAL(10,3) DEFAULT NULL,
  `ACTUAL_BACKDELIVERY_KW` DECIMAL(10,3) DEFAULT NULL,
  `NR_POWERFAILURES` int(11) DEFAULT NULL,
  `NR_POWERFAILURES_LONG` int(11) DEFAULT NULL,
  `POWERFAILURE_LOG` TEXT DEFAULT NULL,
  `NR_VOLTAGE_SAGS_L1` int(11) DEFAULT NULL,
  `NR_VOLTAGE_SWELLS_L1` int(11) DEFAULT NULL,
  `TEXT_MESSAGE` TEXT DEFAULT NULL,
  `VOLTAGE_L1_V` DECIMAL(10,3) DEFAULT NULL,
  `CURRENT_L1_A` DECIMAL(10,3) DEFAULT NULL,
  `MBUS1_VALUE_GAS_M3` DECIMAL(10,3) DEFAULT NULL,
  `MBUS1_VALUE_TIMESTAMP` DATETIME DEFAULT NULL,
  `JSON` TEXT DEFAULT NULL,
  PRIMARY KEY (ID)
) ENGINE=INNODB  DEFAULT CHARSET=LATIN1 AUTO_INCREMENT=1;

ALTER TABLE `METER` CHANGE `ID` `ID` INT(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `METER` ADD INDEX(`TIMESTAMP`);
