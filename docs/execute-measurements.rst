Install the SEN66 Driver
------------------------

.. include:: driver-installation.rst


Use the SensorBridge on Windows
-------------------------------

1. Install the driver for the `Sensirion SEK-SensorBridge`_:

   .. code-block:: console

      python -m pip install sensirion-shdlc-sensorbridge

2. Connect the SEK-SensorBridge to your PC over USB.

   If the SEK-SensorBridge is not detected by your system, follow the
   `SensorBridge FTDI Driver Installation`_.

3. Connect the SEN66 sensor to the SEK-SensorBridge.

4. Run the example script from the root of the repository.

   By default, the script assumes that the SensorBridge is connected to the
   ``COM1`` serial port. If a different port is used, specify it with the
   ``--serial-port`` parameter:

   .. code-block:: console

        python examples/example_usage_sensorbridge_sen66.py --serial-port <your COM port>


.. _Sensirion SEK-SensorBridge: https://developer.sensirion.com/product-support/sek-sensorbridge/
.. _SensorBridge FTDI Driver Installation: https://sensirion.github.io/python-shdlc-sensorbridge/sensor-bridge-installation.html

Example script
~~~~~~~~~~~~~~

.. literalinclude:: ../examples/example_usage_sensorbridge_sen66.py
    :language: python


Use the Linux I²C Driver
------------------------

On Linux systems, the sensor can alternatively be accessed directly through
the Linux user-space I²C driver.

1. Connect the SEN66 sensor to an I²C port of your system, for example I²C
   port 1 of a Raspberry Pi.

2. Run the example script from the root of the repository.

   By default, the script assumes that the sensor is connected to
   ``/dev/i2c-1``. If a different port is used, specify it with the
   ``--i2c-port`` parameter:

   .. code-block:: console

      python examples/example_usage_linux_sen66.py --i2c-port <your I2C port>

Example script
~~~~~~~~~~~~~~

.. literalinclude:: ../examples/example_usage_linux_sen66.py
    :language: python
