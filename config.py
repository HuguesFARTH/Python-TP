import configparser
import keyboard
import os


class Config:
    """
    classe qui gère le fichier config et la configuration des touches
    """
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
        config["move"] = {'right': "Right",
                          'left': "Left"}
        config["shoot"] = {'shoot': "space"}
        config["pause"] = {'pause': "p"}
        config["overlay"] = {'overlay': 1}
        config["speed"] = {'playerSpeed': 1,
                           'monsterSpeed': 1,
                           'bulletSpeed': 1}


        with open(self.file_name, 'w') as configfile:
            config.write(configfile)


    def read_config(self):
        """
        lit le fichier config et stocke les données dans un dictionnaire
        :return:
        """
        touches = {}
        config = configparser.ConfigParser()
        config.read(self.file_name)
        if len(config.sections()) == 0:
            self.default_config()
        touches['right'] = config['move']['Right']
        touches['left'] = config['move']['left']
        touches['shoot'] = config['shoot']['shoot']
        touches['pause'] = config['pause']['pause']
        try:
            touches['overlay'] = int(config['overlay']['overlay'])
        except:
            touches['overlay'] = 1
            print("exept overlay")
        try:
            touches['playerSpeed'] = float(config['speed']['playerSpeed'])
        except:
            touches['playerSpeed'] = 1.0
            print("exept player")
        try:
            touches['monsterSpeed'] = float(config['speed']['monsterSpeed'])
        except:
            print("exept monster")
            touches['monsterSpeed'] = 1.0
        try:
            touches['bulletSpeed'] = float(config['speed']['bulletSpeed'])
        except:
            touches['bulletSpeed'] = 1.0
        return touches


    def modify_config(self,newConfigDic):
        """
        modifie la config et le fichier config
        :param newConfigDic:
        :return:
        """
        if self.file_exist == True:
            config = configparser.ConfigParser()
            config["move"] = {
                'right': newConfigDic["right"],
                              'left': newConfigDic["left"]}
            config["shoot"] = {'shoot': newConfigDic["shoot"]}
            config["pause"] = {'pause': newConfigDic["pause"]}
            config["overlay"] = {'overlay': newConfigDic["overlay"]}
            config["speed"] = {'playerSpeed': newConfigDic["playerSpeed"],
                               'monsterSpeed': newConfigDic["monsterSpeed"],
                               'bulletSpeed': newConfigDic["bulletSpeed"]}
            with open(self.file_name, 'w') as configfile:
                config.write(configfile)
        else:
            self.file_exist = True
            self.default_config()
