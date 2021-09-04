#!/usr/bin/env python3

import os
import random
import sys
from os import path

import RPi.GPIO as gpio
from playsound import playsound

play_audio_file = playsound


def random_file(dir_path):
    file_name = random.choice(os.listdir(dir_path))
    return path.join(dir_path, file_name)


def setup_gpio(motion_sensor_pin):
    gpio.setmode(gpio.BCM)
    gpio.setup(motion_sensor_pin, gpio.IN, pull_up_down=gpio.PUD_UP)


def main(audio_files_dir, motion_sensor_pin):
    audio_files_dir = path.abspath(audio_files_dir)
    setup_gpio(motion_sensor_pin)
    random.seed()

    while True:
        gpio.wait_for_edge(motion_sensor_pin, gpio.RISING)
        file_path = random_file(audio_files_dir)
        play_audio_file(file_path)


if __name__ == "__main__":
    try:
        audio_files_dir = sys.argv[1]
    except IndexError:
        audio_files_dir = "./audio-files"
    try:
        motion_sensor_pin = int(sys.argv[2])
    except IndexError:
        motion_sensor_pin = 17

    main(audio_files_dir, motion_sensor_pin)
