#!/usr/bin/env sh

# This script sets up the whole application

########################################
# System dependencies
########################################

echo '[\e[32mINFO\e[0m] Install python system dependencies'
sudo apt install \
    python3 \
    python3-venv

echo '[\e[32mINFO\e[0m] Install audio system dependencies'
sudo apt install \
    gir1.2-gstreamer-1.0 \
    gstreamer1.0-gl \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-pulseaudio \
    python3-gi

echo '[\e[32mINFO\e[0m] Install GPIO system dependencies'
sudo apt install \
    python3-rpi.gpio

########################################
# Python virtualenv
########################################

echo '[\e[32mINFO\e[0m] Create python virtual environment'
python3 -m venv --system-site-packages .venv

########################################
# Pip dependencies
########################################

echo '[\e[32mINFO\e[0m] Install pip dependencies'
. .venv/bin/activate
pip install -r requirements.txt
deactivate

########################################
# Systemd integration
########################################

echo '[\e[32mINFO\e[0m] Install systemd units'
SYSTEMD_USER_PATH="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
install -d "$SYSTEMD_USER_PATH"
install "$PWD/systemd/"*.timer "$PWD/systemd/"*.service "$SYSTEMD_USER_PATH"
unset SYSTEMD_USER_PATH

echo '[\e[32mINFO\e[0m] Enable systemd timers'
ls -1 "$PWD/systemd" | grep '.timer' | xargs systemctl --user enable --now

echo '[\e[32mINFO\e[0m] Install project files to systemd-available location'
BIN_PATH="$HOME/bin"
LIB_PATH="$HOME/lib/arnold-random-quotes"
install -d "$BIN_PATH" "$LIB_PATH" "$LIB_PATH/audio-files"
install "$PWD/systemd/arnold-random-quotes" "$HOME/bin"
install "$PWD/main.py" "$LIB_PATH"
install "$PWD/audio-files/"* "$LIB_PATH/audio-files"
unset BIN_PATH

printf '[\e[32mINFO\e[0m] Create python virtual environment in '
echo 'systemd-available location'
python3 -m venv --system-site-packages "$LIB_PATH/.venv"
. "$LIB_PATH/.venv/bin/activate"
pip install -r requirements.txt
deactivate
unset LIB_PATH
