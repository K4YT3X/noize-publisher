#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Noize Level
Author: K4YT3X
Date Created: December 1, 2018
Last Modified: December 1, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2018 K4YT3X

Partial code originally by @Ryan Martin at stackoverflow.
https://stackoverflow.com/a/40157297
"""
import sounddevice
import numpy


class NoiseGatherer:
    """ Noise Gatherer

    Record for a few seconds and return the volume normal.
    """

    def __init__(self):
        self.volume_norm = 0

    def get_level(self):
        with sounddevice.Stream(callback=self._parse_level):
            sounddevice.sleep(5 * 1000)
        return self.volume_norm

    def _parse_level(self, indata, outdata, frames, time, status):
        self.volume_norm = numpy.linalg.norm(indata) * 10
