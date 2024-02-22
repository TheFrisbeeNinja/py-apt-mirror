import argparse
import logging
import os
import sys

import py_apt_mirror
from py_apt_mirror.config import Configuration


DEFAULT_CONFIG_FILE = "/etc/apt/mirror.list"
log = logging.getLogger()


########################################################################################################################
def _buildArgParser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--config", default=DEFAULT_CONFIG_FILE, help="Configuration file")
    parser.add_argument("-v", "--version", action="version", version=py_apt_mirror.VERSION)
    parser.add_argument("-l", "--log", default="INFO", help="Python logging level")

    return parser


########################################################################################################################
def main():
    """Main entry point for the 'py-apt-mirror' application."""
    parser = _buildArgParser()
    arguments = parser.parse_args()
    print(f'config = {arguments.config}')
    print(f'log = {arguments.log}')

    logLevel = getattr(logging, arguments.log.upper(), None)
    if not isinstance(logLevel, int):
        raise ValueError(f"Invalid log level: {arguments.log}")
    logging.basicConfig(level=logLevel)

    config = Configuration(arguments.config)

    print("Mirror dir = {}".format(config.mirrorDirectory))

    sys.exit(0)
