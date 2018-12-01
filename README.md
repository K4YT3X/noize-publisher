# Noize Publisher

### This repository is part of the [Noize Project](https://github.com/Thayallan-S/noize).

## 1.0.0 (December 1, 2018)

- Initial release of noize publisher.
- Included basic noise level measuring and publishing functionality.

## Description

This is a program to be deployed on endpoint devices which will report sound levels for noize clients. It records the sound on the microphone for a certain during of time, and takes the average volume normal of that recorded sound as the current noise level, then push it to the mqtt broker.

## Usages

### Installation

First we have to download noise publisher (on the IoT device). You may either clone or download the source code of noise publisher.

```bash
$ git clone https://github.com/K4YT3X/noize-publisher.git
```

Then you can install dependencies via either standalone `pip` or the pip module within python.

```bash
noize-publisher/bin/$ pip install -r requirements.txt  # Install via standalone pip
noize-publisher/bin/$ python -m pip install -r requirements.txt  # Install via python pip module
```

After that, you can simply run noise publisher with one command, where the `device-id` is what you want to call the device. Noize clients will use this as an identifier to distinguish the devices.

```bash
$ python noise_publisher.py [device-id]
```

## Removal

Noize publisher doesn't install anything into the system. You can remove noize publisher simply by deleting the directory containing it.