#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2025 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 1.1.2
# Product:       sen66
# Model-Version: 1.6.0
#

import argparse
import time
from sensirion_i2c_driver import I2cConnection, CrcCalculator
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import (SensorBridgePort,
                                          SensorBridgeShdlcDevice,
                                          SensorBridgeI2cProxy)
from sensirion_driver_adapters.i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_sen66.device import Sen66Device

parser = argparse.ArgumentParser()
parser.add_argument('--serial-port', '-p', default='COM1')
args = parser.parse_args()

with ShdlcSerialPort(port=args.serial_port, baudrate=460800) as port:
    bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x6B,
                         crc=CrcCalculator(8, 0x31, 0xff, 0x0))
    sensor = Sen66Device(channel)
    sensor.device_reset()
    time.sleep(1.2)
    serial_number = sensor.get_serial_number()
    print(f"serial_number: {serial_number}; "
          )
    sensor.start_continuous_measurement()
    for i in range(100):
        try:
            time.sleep(1.0)
            (mass_concentration_pm1p0, mass_concentration_pm2p5, mass_concentration_pm4p0, mass_concentration_pm10p0, humidity,
             temperature, voc_index, nox_index, co2
             ) = sensor.read_measured_values()
            print(f"mass_concentration_pm1p0: {mass_concentration_pm1p0}; "
                  f"mass_concentration_pm2p5: {mass_concentration_pm2p5}; "
                  f"mass_concentration_pm4p0: {mass_concentration_pm4p0}; "
                  f"mass_concentration_pm10p0: {mass_concentration_pm10p0}; "
                  f"humidity: {humidity}; "
                  f"temperature: {temperature}; "
                  f"voc_index: {voc_index}; "
                  f"nox_index: {nox_index}; "
                  f"co2: {co2}; "
                  )
        except BaseException:
            continue
    sensor.stop_measurement()
