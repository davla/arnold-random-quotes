# arnold-random-quotes
Play random Arnold Schwarzenegger quotes on GPIO rising edge.

## Run

From the project root directory, execute this within the python virtual
environment:

```sh
python main.py
```

This uses the defaults for all options. For more information on the options
themselves run:

```sh
python main.py --help
```

## Setup

Just run `setup.sh`. :smiley:

The script will:

- Install system dependencies
- Create a Python3 virtual environment
- Install pip dependencies
- Enable the program to run as a systemd service between 18:00 and 00:00
