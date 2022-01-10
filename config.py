import configparser
import keyboard
import os


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
        config["move"] = {'up': "up",
                          'down': "down",
                          'right': "Right",
                          'left': "Left"}
        config["shoot"] = {'shoot': "space"}
        config["pause"] = {'pause': "p"}

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
        touches['pause'] = config['pause']['pause']
        return touches


    def modify_config(self):
        if self.file_exist == True:
            key_pressed = keyboard.read_key(suppress = True)
        else:
            self.file_exist = True
            self.default_config()
        return key_pressed

# config = Config('config.ini')
# print(config.modify_config())


# def key():
#     a = keyboard.read_key(suppress=False)
#     return a
#
# print(key())
