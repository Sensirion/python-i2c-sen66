# Python I2C Driver for Sensirion SEN66

This repository contains the Python driver to communicate with a Sensirion SEN66 sensor over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sen66/master/images/product-image-sen6x.png"
    width="300px" alt="SEN66 picture">


Click [here](https://sensirion.com/sen6x-air-quality-sensor-platform) to learn more about the Sensirion SEN66 sensor.



The default I²C address of [SEN66](https://www.sensirion.com/products/catalog/SEN66) is **0x6b**.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/product-support/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sen66/master/images/product-pinout-sen6x.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red | VDD | Supply Voltage | 3.3V ±5%
| 2 | black | GND | Ground |
| 3 | green | SDA | I2C: Serial data input / output | TTL 5V compatible
| 4 | yellow | SCL | I2C: Serial clock input | TTL 5V compatible
| 5 |  | NC | Do not connect | Ground (Pins 2 and 5 are connected internally)
| 6 |  | NC | Do not connect | Supply voltage (Pins 1 and 6 are connected internally)


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-sen66) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-sen66/quickstart.html) example.


## Contributing

In case you want to contribute to this project, please read the [contribution guidelines]((https://sensirion.github.io/python-i2c-sen66/contributing.html)).

## License

See [LICENSE](LICENSE).