Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install test requirements


We provide a mock implementation that allows you to execute the tests for SEN66 without hardware.

.. code-block:: bash

    pytest                                       # Run all tests for SEN66 using a driver mock

To use the real hardware you have to connect your SEN66 sensor to a
`SensorBridge <https://sensirion.com/products/catalog/SEK-SensorBridge/>`_ on port 1. Assuming the SensorBridge is
attached to COM1 you can start the tests with the following command:

.. code-block:: bash

    pytest --serial-port=COM1                    # Run all tests for SEN66 on the sensor attached to COM1


.. note::
    The SensorBridge must have default settings (baudrate 460800, address 0)

