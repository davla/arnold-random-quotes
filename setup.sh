#!/usr/bin/env sh

# This script sets up the whole application

########################################
# System dependencies
########################################

# Python dependencies
sudo apt install \
    python3 \
    python3-venv

# Audio dependencies
sudo apt install \
    gir1.2-gstreamer-1.0 \
    gstreamer1.0-gl \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-pulseaudio \
    python3-gi

# GPIO dependencies
sudo apt install \
    python3-rpi.gpio

########################################
# Python virtualenv
########################################

python3 -m venv --system-site-packages .venv

########################################
# Pip dependencies
########################################

. .venv/bin/activate
pip install -r requirements.txt
deactivate
