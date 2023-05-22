import random
import time
from termcolor import colored
import signal

def generate_random_binary(length):
    binary = ""
    for _ in range(length):
        binary += random.choice(["■□■□■□■□■", "■□■□■□■□■"])
    return binary

def generate_random_color():
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    return random.choice(colors)

def display_moving_binary(length, delay):
    def handle_signals(signum, frame):
        pass

    signal.signal(signal.SIGINT, handle_signals)
    signal.signal(signal.SIGTSTP, handle_signals)
    signal.signal(signal.SIGQUIT, handle_signals)

    while True:
        binary = generate_random_binary(length)
        color = generate_random_color()
        colored_binary = colored(binary, color)
        print(colored_binary)
        time.sleep(delay)

binary_length = 50  # Length of the binary code
delay_seconds = 0.1  # Delay between each iteration in seconds

display_moving_binary(binary_length, delay_seconds)
