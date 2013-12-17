""" Configuration handler """
import config

CONFIGURATION = config.get_configuration()


def get_configured_gsis():
    """ Returns a list of configured global secondary indexes

    :returns: list -- [(gsi_key_name, [table_names])]
    """
    gsis = []
    for gsi_key_name in CONFIGURATION['gsis']:
        print(CONFIGURATION['gsis'][gsi_key_name])
        gsis.append(
            (
                gsi_key_name,
                CONFIGURATION['gsis'][gsi_key_name]['table_key_name'],
            ))
    return gsis


def get_global_option(option):
    """ Returns the value of the option

    :returns: str
    """
    return CONFIGURATION['global'][option]


def get_gsi_option(table_key, gsi_key, option):
    """ Returns the value of the option

    :type table_key: str
    :param table_key: Table key name
    :type gsi_key: str
    :param gsi_key: GSI key name
    :returns: str
    """
    return CONFIGURATION['tables'][table_key]['gsis'][gsi_key][option]


def get_logging_option(option):
    """ Returns the value of the option

    :returns: str
    """
    return CONFIGURATION['logging'][option]


def get_table_option(table_name, option):
    """ Returns the value of the option

    :type table_name: str
    :param table_name: Name of the DynamoDB table
    :returns: str
    """
    return CONFIGURATION['tables'][table_name][option]
