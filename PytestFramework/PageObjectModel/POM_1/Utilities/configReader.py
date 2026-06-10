from configparser import ConfigParser


def get_Config_Data(c, k):
    config = ConfigParser()
    config.read(
        "PytestFramework/PageObjectModel/POM_1/Configuration/config.ini"
    )
    return config.get(c, k)
