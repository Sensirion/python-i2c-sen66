#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2024 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 1.0.1
# Product:       sen66
# Model-Version: 1.2.0
#
"""
The class Sen66DeviceBase implements the low level interface of the sensor.
The class Sen66Device extends the Sen66DeviceBase. It provides additional functions to ease the use of the
sensor.
"""

from sensirion_driver_adapters.transfer import execute_transfer
from sensirion_driver_support_types.mixin_access import MixinAccess
from sensirion_i2c_sen66.commands import (DeviceReset, GetDataReady, GetProductName, GetSerialNumber, GetVersion,
                                          PerformForcedCo2Recalibration, ReadMeasuredValuesAsIntegers,
                                          StartContinuousMeasurement, StopMeasurement)

from sensirion_i2c_sen66.result_types import (SignalCo2, SignalHumidity, SignalMassConcentrationPm10p0,
                                              SignalMassConcentrationPm1p0, SignalMassConcentrationPm2p5,
                                              SignalMassConcentrationPm4p0, SignalNoxIndex, SignalTemperature,
                                              SignalVocIndex)


class Sen66DeviceBase:
    """Low level API implementation of SEN66"""

    def __init__(self, channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def device_reset(self):
        """Executes a reset on the device. This has the same effect as a power cycle."""
        transfer = DeviceReset()
        return execute_transfer(self._channel, transfer)

    def start_continuous_measurement(self):
        """
        Starts a continuous measurement.
        After power up, wait at least 500 ms before sending this
        command. After sending this command, wait at least 1100 ms before
        reading measurements.
        This command is only available in idle mode. If the device is already
        in any measure mode, this command has no effect.
        """
        transfer = StartContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def stop_measurement(self):
        """
        Stops the measurement and returns to idle mode. After sending this
        command, wait at least 1000 ms before starting a new measurement.
        If the device is already in idle mode, this command has no effect.
        """
        transfer = StopMeasurement()
        return execute_transfer(self._channel, transfer)

    def get_data_ready(self):
        """
        This command can be used to check if new measurement results are ready to read. The data ready flag
        is automatically reset after reading the measurement values.

        :return padding:
            Padding byte, always 0x00.
        :return data_ready:
            True (0x01) if data is ready, False (0x00) if not. When no measurement is running, False will be
            returned.
        """
        transfer = GetDataReady()
        return execute_transfer(self._channel, transfer)

    def read_measured_values_as_integers(self):
        """
        Returns the measured values.
        The command 0x0202 \"Get Data Ready\" can be used to check if new
        data is available since the last read operation. If no new data is
        available, the previous values will be returned again. If no data
        is available at all (e.g. measurement not running for at least one
        second), all values will be at their upper limit (0xFFFF for `uint16`,
        0x7FFF for `int16`).

        :return mass_concentration_pm1p0:
            Value is scaled with factor 10: PM1.0 [µg/m³] = value / 10
            *Note: If this value is unknown, 0xFFFF is returned.*
        :return mass_concentration_pm2p5:
            Value is scaled with factor 10: PM2.5 [µg/m³] = value / 10
            *Note: If this value is unknown, 0xFFFF is returned.*
        :return mass_concentration_pm4p0:
            Value is scaled with factor 10: PM4.0 [µg/m³] = value / 10
            *Note: If this value is unknown, 0xFFFF is returned.*
        :return mass_concentration_pm10p0:
            Value is scaled with factor 10: PM10.0 [µg/m³] = value / 10
            *Note: If this value is unknown, 0xFFFF is returned.*
        :return ambient_humidity:
            Value is scaled with factor 100: RH [%] = value / 100
            *Note: If this value is unknown, 0x7FFF is returned.*
        :return ambient_temperature:
            Value is scaled with factor 200: T [°C] = value / 200
            *Note: If this value is unknown, 0x7FFF is returned.*
        :return voc_index:
            Value is scaled with factor 10: VOC Index = value / 10
            *Note: If this value is unknown, 0x7FFF is returned.*
        :return nox_index:
            Value is scaled with factor 10: NOx Index = value / 10
            *Note: If this value is unknown, 0x7FFF is returned. During
            the first 10..11 seconds after power-on or device reset, this
            value will be 0x7FFF as well.*
        :return co2:
            CO2 concentration [ppm]
            *Note: If this value is unknown, 0xFFFF is returned. During the
            first 5..6 seconds after power-on or device reset, this value
            will be 0xFFFF as well.*
        """
        transfer = ReadMeasuredValuesAsIntegers()
        return execute_transfer(self._channel, transfer)

    def perform_forced_co2_recalibration(self, target_co2_concentration):
        """
        Execute the forced recalibration (FRC) of the CO2 signal on the SCD4x
        sensor. See the datasheet of the SCD41 sensor for details how the
        forced recalibration shall be used.

        :param target_co2_concentration:
            Target CO2 concentration [ppm] of the test setup.

        :return correction:
            Correction value as received from the SCD [ppm CO2]. Offset is 0x8000, if the recalibration has
            failed this value is 0xFFFF.

        .. note::
            After power-on wait at least 1000 ms and after stopping a measurement 600 ms before sending this
            command. This command is not available in measure mode. The recalibration procedure will take about
            500 ms to complete, during which time no other functions can be executed.
        """
        transfer = PerformForcedCo2Recalibration(target_co2_concentration)
        return execute_transfer(self._channel, transfer)[0]

    def get_product_name(self):
        """
        Gets the product name from the device.

        :return product_name:
            Null-terminated ASCII string containing the product name. Up to 32 characters can be read from the
            device.
        """
        transfer = GetProductName()
        return execute_transfer(self._channel, transfer)[0]

    def get_serial_number(self):
        """
        Gets the serial number from the device.

        :return serial_number:
            Null-terminated ASCII string containing the serial number. Up to 32 characters can be read from the
            device.
        """
        transfer = GetSerialNumber()
        return execute_transfer(self._channel, transfer)[0]

    def get_version(self):
        """
        Gets the version information for the hardware, firmware and communication protocol.

        :return firmware_major:
            Firmware major version number.
        :return firmware_minor:
            Firmware minor version number.
        :return firmware_debug:
            Firmware debug state. If the debug state is set, the firmware is in development.
        :return hardware_major:
            Hardware major version number.
        :return hardware_minor:
            Hardware minor version number.
        :return protocol_major:
            Protocol major version number.
        :return protocol_minor:
            Protocol minor version number.
        :return padding:
            Padding byte, ignore this.
        """
        transfer = GetVersion()
        return execute_transfer(self._channel, transfer)


class Sen66Device(Sen66DeviceBase):
    """Driver class implementation of SEN66"""

    #: Access to base class
    sen66 = MixinAccess()

    def __init__(self, channel):
        super().__init__(channel)

    def read_measured_values(self):
        """
        Read measured values and apply scaling as defined in datasheet.

        :return mass_concentration_pm1p0:
            Mass concentration for particles smaller than 1.0 um.
        :return mass_concentration_pm2p5:
            Mass concentration for particles smaller than 2.5 um.
        :return mass_concentration_pm4p0:
            Mass concentration for particles smaller than 4.0 um.
        :return mass_concentration_pm10p0:
            Mass concentration for particles smaller than 10.0 um.
        :return humidity:
            Measured humidity in %RH.
        :return temperature:
            Measured temperature in degrees celsius.
        :return voc_index:
            Measured VOC Index between 0 and 500.
        :return nox_index:
            Measured NOx Index between 0 and 500.
        :return co2:
            Measured CO2 concentration in ppm.
        """
        (mass_concentration_pm1p0_raw, mass_concentration_pm2p5_raw, mass_concentration_pm4p0_raw,
         mass_concentration_pm10p0_raw, humidity_raw, temperature_raw, voc_index_raw, nox_index_raw,
         co2_raw
         ) = self.read_measured_values_as_integers()
        return (SignalMassConcentrationPm1p0(mass_concentration_pm1p0_raw),
                SignalMassConcentrationPm2p5(mass_concentration_pm2p5_raw),
                SignalMassConcentrationPm4p0(mass_concentration_pm4p0_raw),
                SignalMassConcentrationPm10p0(mass_concentration_pm10p0_raw), SignalHumidity(humidity_raw),
                SignalTemperature(temperature_raw), SignalVocIndex(voc_index_raw), SignalNoxIndex(nox_index_raw),
                SignalCo2(co2_raw))