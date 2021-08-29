#!/usr/bin/env python3

import sys
from os.path import abspath

from playsound import playsound

play_audio_file = playsound

if __name__ == "__main__":
    file_path = abspath(sys.argv[1])

    play_audio_file(file_path)
