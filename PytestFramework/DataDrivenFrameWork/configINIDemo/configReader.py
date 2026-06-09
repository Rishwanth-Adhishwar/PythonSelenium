from configparser import ConfigParser


def config_read(c, k):
    config = ConfigParser()
    config.read("PytestFramework/DataDrivenFrameWork/configINIDemo/config.ini")
    return config.get(c, k)


