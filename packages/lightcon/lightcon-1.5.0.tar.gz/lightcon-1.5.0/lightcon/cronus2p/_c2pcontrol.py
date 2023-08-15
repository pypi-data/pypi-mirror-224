#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c2pcontrol - remote control of the CRONUS-2P optical parametric oscillator.

Copyright 2020-2023 Light Conversion
Contact: support@lightcon.com
"""

import logging

logger = logging.getLogger('c2p')

file_log_handler = logging.FileHandler('cronus_2p.log')
logger.addHandler(file_log_handler)

stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log_handler.setFormatter(formatter)
stderr_log_handler.setFormatter(formatter)

logger.setLevel('DEBUG')

logger.info('Loading imports')

import json
from urllib.error import URLError
from ..common._http_methods import HTTP_methods


class C2PControl(HTTP_methods):
    """REST API interaction with CRONUS-2P REST Server."""

    silent = True
    connected = False
    logger = None
    type = 'cronus2p'

    def __init__(self, ip_address='127.0.0.1', port=35100, version='v0'):
        self.url = 'http://{}:{}/{}/Cronus/'.format(
            ip_address, port, version)
        print("Connecting to CRONUS-2P at {:s}:{:d}".format(
            ip_address, port))

        status = self.get_status()

        if status.get('OK'):
            print('Connection to CRONUS-2P established at', self.url)

        self.logger = logger

    def get_status(self):
        try:
            return self._get('Status')
        except URLError as excp:
            print("Could not reach CRONUS-2P {:s}".format(self.ip_address))
        except Exception as excp:
            print("An unknown error has occurred")
            print(excp)

    def set_mode_run(self):
        self._put("ModeRun", '')

    def get_mode(self):
        return self._get("Mode")

    def get_pump_power(self):
        return float(self._get("PumpPower").get("Power"))*1E-3

    def _check_channel(self, channel=None):
        if channel is None:
            print("No channel specified")
            return False

        if channel < 1 or channel > 3:
            print("Channel must be 1 – 3")
            return False

        return True

    def _check_wavelength(self, channel=None, wavelength=None):
        rng = self.get_wavelength_range(channel)
        if wavelength < rng[0] or wavelength > rng[1]:
            print("Wavelenngth {:.1f} nm is out of range for Channel {:d} ({:.1f} - {:.1f})".format(wavelength, channel, rng[0], rng[1]))
            return False

        return True

    def open_shutter(self, channel=None):
        if not self._check_channel(channel):
            return
        self._put("Ch{:d}".format(channel) + "/ShutterOpen", '')

    def close_shutter(self, channel=None):
        if not self._check_channel(channel):
            return
        self._put("Ch{:d}".format(channel) + "/ShutterClosed", '')

    def get_wavelength(self, channel=None):
        if not self._check_channel(channel):
            return
        return float(self._get("Ch{:d}".format(channel) + "/Wavelength").get("Wavelenghth"))

    def set_wavelength(self, channel=None, wavelength=None, verbose=True):
        if not self._check_channel(channel):
            return
        if not self._check_wavelength(channel, wavelength):
            return
        self._put("Ch{:d}".format(channel) + "/Wavelength", json.dumps({'Wavelength': wavelength}))

    def get_wavelength_range(self, channel=None):
        if not self._check_channel(channel):
            return
        response = self._get("Ch{:d}".format(channel) + "/WavelengthRange")
        return [float(response.get('Min')), float(response.get('Max'))]

    def get_current_gdd_range(self, channel=None):
        if not self._check_channel(channel):
            return
        response = self._get("Ch{:d}".format(channel) + "/CurrentGDDRange")
        return [float(response.get('Min')), float(response.get('Max'))]

    def get_gdd_range(self, channel=None, wavelength=None):
        if not self._check_channel(channel):
            return
        if not self._check_wavelength(channel, wavelength):
            return
        response = self._report("Ch{:d}".format(channel) + "/GDDRange", json.dumps({'Wavelength': wavelength}))
        return [float(response.get('Min')), float(response.get('Max'))]
