#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Noize Server
Author: K4YT3X
Date Created: December 1, 2018
Last Modified: December 1, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2018 K4YT3X
"""
from noize_gatherer import NoiseGatherer
import paho.mqtt.client as mqtt
import sys
import traceback

VERSION = '1.0.0'


class NoizePublisher:
    """ Noize Publisher

    Publishes sound data to mqtt topic on noize server.
    This data is to be parsed by noize client to display.
    """

    def __init__(self, broker, topic):
        """ Receive and store noize publisher arguments
        """
        self.broker = broker
        self.topic = topic

    def init(self):
        """ Initialize mqtt client and connect to mqtt server
        """
        self.client = mqtt.Client()
        self.client.on_connect = self._on_connect
        self.client.connect(self.broker, 1883, 60)

    def publish(self, payload):
        """ Publish a payload to the topic
        """
        self.client.publish(self.topic, payload)

    def _on_connect(self, client, userdata, flags, rc):
        """ Print the connection result code on connect
        """
        print('Connected with result code: {}'.format(str(rc)))
        # client.subscribe(self.topic)


def serve():
    """ Start gathering noise level and publish them to mqtt topoic.
    """
    publisher = NoizePublisher('noize.flexio.org', 'noize/{}'.format(sys.argv[1]))
    publisher.init()
    gatherer = NoiseGatherer()
    while True:
        level = gatherer.get_level()
        print('[NoizePublisher]: Publishing Level: {}'.format(level))
        publisher.publish(int(round(gatherer.get_level()), 0))


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('ERROR: No device ID given', file=sys.stderr)
            print('Usage: ./{} [device ID]'.format(__file__), file=sys.stderr)
        serve()
    except Exception:
        traceback.print_exc()

# For debugging only
"""
if __name__ == '__main__':
    publisher = NoizePublisher('noize.flexio.org', 'noize/{}'.format(sys.argv[1]))
    publisher.init()

    while True:
        publisher.publish(input('[NoizePublisher: {}]> '.format(publisher.topic)))
"""
