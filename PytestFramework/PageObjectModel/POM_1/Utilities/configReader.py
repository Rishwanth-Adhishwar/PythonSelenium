from configparser import ConfigParser


def get_Config_Data(c, k):
    config = ConfigParser()
    config.read(
        ""
    )
    return config.get(c, k)
