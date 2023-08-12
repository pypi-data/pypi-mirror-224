# proxr-protocol

[![PyPI](https://img.shields.io/pypi/v/proxr-protocol)](https://pypi.org/project/proxr-protocol)
[![Conda](https://img.shields.io/conda/vn/conda-forge/proxr-protocol)](https://anaconda.org/conda-forge/proxr-protocol)
[![black](https://img.shields.io/badge/code--style-black-black)](https://black.readthedocs.io/)
[![ver](https://img.shields.io/badge/calver-YYYY.M.MICRO-blue)](https://calver.org/)
[![log](https://img.shields.io/badge/change-log-informational)](https://github.com/yaq-project/proxr-protocol/-/blob/main/CHANGELOG.md)

A sans I/O Python implementation of the [ProXR Protocol](https://ncd.io/proxr-quick-start-guide/).

## Introduction

This Python package contains tooling for encoding and decoding bytestrings for communication with ProXR peripherals.
ProXR has been implemented using a variety of transport layers---XBee, UART, Ethernet, etc.
In persuit of simplicity and reusability, this package does not contain any interface capabilities.
Use something like [pySerial](https://pyserial.readthedocs.io) for transport.
Read the [sans I/O manifesto](https://sans-io.readthedocs.io/) for more motivation regarding this design pattern.

## Maintainers

- [Blaise Thompson](https://github.com/untzag)
