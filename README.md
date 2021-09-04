# arnold-random-quotes
Play random Arnold Schwarzenegger quotes when a proximity sensor triggers.

This project is part of a bigger master plan: a little home-shrine to worship
his majesty Arnold Schwarzenegger. Close by a life-sized cardboard cutout of
Arnie, there's a humble Raspberry Pi whose only purpose is to play the most
memorable quotes of our favorite Terminator. Just imagine yourself, prostrating
in adoration in front of Arnold's magnificence, your spirit and mind guided by
a rumbling:

> Put that cookie down! NOW!

Isn't this all that you need in your life to achieve Nirvana?

In order to make this happen, this project has been created. It's meant to run
on a Raspberry Pi, with a speaker connected via AUX and a PIR motion sensor
attached via GPIO: whenever the sensor triggers, a random audio file from a
local directory is played. The program is run in the background, started at
18:00 and stopped at 00:00, so that it doesn't randomly disrupt your sleep or
work-from-home time.

## Running

Once the systemd has been set up (see [the setup section](#setup)), the project
can be run by means of the following command, within the python virtual
environment, from the project root directory,:

```sh
python main.py
```

This uses the defaults for all options. For more information on the options
themselves run:

```sh
python main.py --help
```

## Setup

The project is meant to run on Raspbian, with the PIR sensor connected to the
GPIO pin 17 (in BCM numbering system). If this is the case, just run
the `setup.sh` script and you're good to go. :smiley: Otherwise, you'll
probably need to find the equivalent of the installed APT packages for your
distribution and change the GPIO pin number.

The `setup.sh` script will:

- Install system dependencies
- Create a Python3 virtual environment
- Install pip dependencies
- Enable the program to run as a systemd service between 18:00 and 00:00
