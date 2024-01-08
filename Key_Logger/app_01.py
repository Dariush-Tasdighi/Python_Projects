"""Learning Key Logger"""

from pynput.keyboard import Listener


def on_press(key):
    """On Key Press"""
    print(key)


with Listener(on_press=on_press) as listener:
    listener.join()
