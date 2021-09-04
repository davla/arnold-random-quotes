#!/usr/bin/env python3

import logging
import os
import random
import sys
from os import path

import RPi.GPIO as gpio
from playsound import playsound

logger = logging.getLogger("arnold-random-quotes")

play_audio_file = playsound


def random_file(dir_path):
    file_name = random.choice(os.listdir(dir_path))
    logger.debug("Playing file %s in directory %s", file_name, dir_path)
    return path.join(dir_path, file_name)


def setup_gpio(motion_sensor_pin):
    gpio.setmode(gpio.BCM)
    gpio.setup(motion_sensor_pin, gpio.IN, pull_up_down=gpio.PUD_UP)


def main(audio_files_dir, motion_sensor_pin):
    logger.info(
        "Playing random audio files from %s when rising edge is detected on gpio BCM "
        "channel %s",
        audio_files_dir,
        motion_sensor_pin,
    )

    audio_files_dir = path.abspath(audio_files_dir)
    setup_gpio(motion_sensor_pin)
    random.seed()

    while True:
        logger.info("Waiting for rising edge on gpio BCM channel %s", motion_sensor_pin)
        gpio.wait_for_edge(motion_sensor_pin, gpio.RISING)
        logger.info("Rising edge detected on gpio BCM channel %s", motion_sensor_pin)

        file_path = random_file(audio_files_dir)
        play_audio_file(file_path)


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s:%(name)s:%(lineno)d] %(message)s", level=logging.INFO
    )

    try:
        audio_files_dir = sys.argv[1]
    except IndexError:
        logger.info("Argument for audio files directory not found: using default")
        audio_files_dir = "./audio-files"
    try:
        motion_sensor_pin = int(sys.argv[2])
    except IndexError:
        logger.info("Argument for motion sensor pin not found: using default")
        motion_sensor_pin = 17

    main(audio_files_dir, motion_sensor_pin)
