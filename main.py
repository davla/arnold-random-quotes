#!/usr/bin/env python3

import os
import random
import sys
from os import path

from playsound import playsound

play_audio_file = playsound


def random_file(dir_path):
    file_name = random.choice(os.listdir(dir_path))
    return path.join(dir_path, file_name)


def main(audio_files_dir):
    random.seed()

    audio_files_dir = path.abspath(audio_files_dir)
    file_path = random_file(audio_files_dir)

    play_audio_file(file_path)


if __name__ == "__main__":
    try:
        audio_files_dir = sys.argv[1]
    except IndexError:
        audio_files_dir = "./audio-files"

    main(audio_files_dir)
