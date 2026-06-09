from configparser import ConfigParser


def config_read(c, k):
    config = ConfigParser()
    config.read("./config.ini")
    return config.get(c, k)
