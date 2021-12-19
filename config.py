import configparser
import keyboard
import os


# def isAdmin():
#     try:
#         is_admin = (os.getuid() == 0)	# if Unis
#     except AttributeError:
#         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0	# else if Windows
#     return is_admin

class Config:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file_exist = False
        self.verify_config = self.verify_config()


    def verify_config(self):
        """
        verify if a config file already exists and creates one if it doesn't
        :param file_name: str
        :return: bool
        """
        if os.path.isfile(self.file_name):
            self.file_exist = True
        else:
            self.default_config()


    def default_config(self):
        """
        function which sets default configuration for keyboard
        :param file_path: str
        :return:
        """
        config = configparser.ConfigParser()
        config["move"] = {'up': "'up'",
                          'down': "'down'",
                          'right': "'right'",
                          'left': "'left'"}
        config["shoot"] = {'shoot': "'space'"}

        with open(self.file_name, 'w') as configfile:
            config.write(configfile)


    def read_config(self):
        touches = {}
        config = configparser.ConfigParser()
        config.read(self.file_name)
        touches['up'] = config['move']['up']
        touches['down'] = config['move']['down']
        touches['right'] = config['move']['right']
        touches['left'] = config['move']['left']
        touches['shoot'] = config['shoot']['shoot']
        return touches


    def modify_config(self):
        if self.file_exist == True:
            pass
        else:
            self.file_exist = True
            self.default_config()



config = Config('config.ini')
# print(config.read_config())


# def verify_config(file_path):
#     try:
#         with open(file_path) as file:
#             return True
#     except FileNotFoundError:
#         default_config(file_path)
#         exit()





# def key():
#     a = keyboard.read_key(suppress=False)
#     return a
