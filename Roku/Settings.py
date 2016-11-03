"""Module to contain Setting class"""
class Settings(object):
    """Class to hold sys wide parameters"""
    roku_apps = []
    roku_ip = ''
    width = 0
    height = 0
    x_offset = 0
    y_offset = 0

    def __str__(self):
        return 'Setting object'
