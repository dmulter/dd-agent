# stdlib
import random

user_ntp_settings = {}

DEFAULT_VERSION = 3
DEFAULT_TIMEOUT = 1 # in seconds
DEFAULT_PORT = "ntp"


def set_user_ntp_settings(instance):
    global user_ntp_settings
    user_ntp_settings = instance

def get_ntp_host(subpool=None):
    """
    Returns randomly a NTP hostname of our vendor pool. Or
    a given subpool if given in input.
    """

    if user_ntp_settings.get('host') is not None:
        return user_ntp_settings['host']

    subpool = subpool or random.randint(0, 3)
    return "{0}.datadog.pool.ntp.org".format(subpool)

def get_ntp_port():
    return user_ntp_settings.get('port') or DEFAULT_PORT

def get_ntp_version():
    return int(user_ntp_settings.get("version") or DEFAULT_VERSION)

def get_ntp_timeout():
    return float(user_ntp_settings.get('timeout') or DEFAULT_TIMEOUT)

def get_ntp_args():
    return {
        'host':    get_ntp_host(),
        'port':    get_ntp_port(),
        'version': get_ntp_version(),
        'timeout': get_ntp_timeout(),
    }
