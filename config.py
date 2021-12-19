import configparser
import keyboard
import ctypes, os

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)	# if Unis
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0	# elese if Windows
    return is_admin

config = configparser.ConfigParser()

config["default"] = {'up': 'up',
                    'down': 'down',
                    'right': 'right',
                    'left': 'left'}
config['user'] = {}

def key():
    a = keyboard.read_key(suppress=False)
    return a


b = key()
print(b)