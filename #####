#ohh nak tengok code 🥴










































































































import random

import importlib.util

import termios

import sys

import tty

# Check if a package is installed

def package_installed(package_name):

    return importlib.util.find_spec(package_name) is not None

# Install a package using pip

def install_package(package_name):

    import subprocess

    subprocess.check_call(["pip", "install", package_name])

# Check and install required packages

required_packages = ["termcolor", "term", "time"]

for package in required_packages:

    if not package_installed(package):

        install_package(package)

# Import the required modules

from termcolor import colored

import term

import time

# Function to get a single character input

def get_single_char_input():

    file_descriptor = sys.stdin.fileno()

    old_settings = termios.tcgetattr(file_descriptor)

    try:

        tty.setraw(file_descriptor)

        character = sys.stdin.read(1)

    finally:

        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)

    return character

def generate_random_binary(length):

    binary = ""

    for _ in range(length):

        binary += random.choice(["0", "1"])

    return binary

def generate_random_color():

    colors = ["red", "green"]

    return random.choice(colors)

def display_moving_binary(length, delay, stop_key):

    while True:

        binary = generate_random_binary(length)

        color = generate_random_color()

        colored_binary = colored(binary, color)

        print(colored_binary)

        time.sleep(delay)

        

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:

            character = get_single_char_input()

            if character.lower() == stop_key.lower():

                break

binary_length = 50  # Length of the binary code

delay_seconds = 0.1  # Delay between each iteration in seconds

stop_key = '8'  # Customize the stop key here

display_moving_binary(binary_length, delay_seconds, stop_key)











