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
"""
The signal classes specify transformations of the raw sensor signals into a meaningful units.
The generated signal types are used by the driver class and not intended for direct use.
"""

from sensirion_driver_support_types.signals import AbstractSignal


class SignalMassConcentrationPm1p0(AbstractSignal):
    """Mass concentration in μg/m³ for particles smaller than 1.0 μm"""

    def __init__(self, mass_concentration_pm1p0_raw):
        self._mass_concentration_pm1p0 = mass_concentration_pm1p0_raw / 10.0

    @property
    def value(self):
        return self._mass_concentration_pm1p0

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalMassConcentrationPm2p5(AbstractSignal):
    """Mass concentration in μg/m³ for particles smaller than 2.5 μm"""

    def __init__(self, mass_concentration_pm2p5_raw):
        self._mass_concentration_pm2p5 = mass_concentration_pm2p5_raw / 10.0

    @property
    def value(self):
        return self._mass_concentration_pm2p5

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalMassConcentrationPm4p0(AbstractSignal):
    """Mass concentration in μg/m³ for particles smaller than 4.0 μm"""

    def __init__(self, mass_concentration_pm4p0_raw):
        self._mass_concentration_pm4p0 = mass_concentration_pm4p0_raw / 10.0

    @property
    def value(self):
        return self._mass_concentration_pm4p0

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalMassConcentrationPm10p0(AbstractSignal):
    """Mass concentration in μg/m³ for particles smaller than 10.0 μm"""

    def __init__(self, mass_concentration_pm10p0_raw):
        self._mass_concentration_pm10p0 = mass_concentration_pm10p0_raw / 10.0

    @property
    def value(self):
        return self._mass_concentration_pm10p0

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalNumberConcentrationPm0p5(AbstractSignal):
    """Number concentration in particles/cm³ for particles smaller than 0.5 μm"""

    def __init__(self, number_concentration_pm0p5_raw):
        self._number_concentration_pm0p5 = number_concentration_pm0p5_raw / 10.0

    @property
    def value(self):
        return self._number_concentration_pm0p5

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalNumberConcentrationPm1p0(AbstractSignal):
    """Number concentration in particles/cm³ for particles smaller than 1.0 μm"""

    def __init__(self, number_concentration_pm1p0_raw):
        self._number_concentration_pm1p0 = number_concentration_pm1p0_raw / 10.0

    @property
    def value(self):
        return self._number_concentration_pm1p0

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalNumberConcentrationPm2p5(AbstractSignal):
    """Number concentration in particles/cm³ for particles smaller than 2.5 μm"""

    def __init__(self, number_concentration_pm2p5_raw):
        self._number_concentration_pm2p5 = number_concentration_pm2p5_raw / 10.0

    @property
    def value(self):
        return self._number_concentration_pm2p5

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalNumberConcentrationPm4p0(AbstractSignal):
    """Number concentration in particles/cm³ for particles smaller than 4.0 μm"""

    def __init__(self, number_concentration_pm4p0_raw):
        self._number_concentration_pm4p0 = number_concentration_pm4p0_raw / 10.0

    @property
    def value(self):
        return self._number_concentration_pm4p0

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalNumberConcentrationPm10p0(AbstractSignal):
    """Number concentration in particles/cm³ for particles smaller than 10.0 μm"""

    def __init__(self, number_concentration_pm10p0_raw):
        self._number_concentration_pm10p0 = number_concentration_pm10p0_raw / 10.0

    @property
    def value(self):
        return self._number_concentration_pm10p0

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalTemperature(AbstractSignal):
    """Measured temperature in degrees celsius. The raw value is scaled appropriately."""

    def __init__(self, temperature_raw):
        self._temperature = temperature_raw / 200.0

    @property
    def value(self):
        return self._temperature

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalHumidity(AbstractSignal):
    """Measured humidity in %RH. The raw value is scaled appropriately."""

    def __init__(self, humidity_raw):
        self._humidity = humidity_raw / 100.0

    @property
    def value(self):
        return self._humidity

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalVocIndex(AbstractSignal):
    """Measured VOC Index ticks."""

    def __init__(self, voc_index_raw):
        self._voc_index = voc_index_raw / 10.0

    @property
    def value(self):
        return self._voc_index

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalNoxIndex(AbstractSignal):
    """Measured NOx Index ticks."""

    def __init__(self, nox_index_raw):
        self._nox_index = nox_index_raw / 10.0

    @property
    def value(self):
        return self._nox_index

    def __str__(self):
        return '{0:.2f}'.format(self.value)


class SignalCo2(AbstractSignal):
    """Measured CO2 in ppm."""

    def __init__(self, co2_raw):
        self._co2 = co2_raw

    @property
    def value(self):
        return self._co2

    def __str__(self):
        return '{0}'.format(self.value)

