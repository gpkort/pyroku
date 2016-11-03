"""Module for class Setting Parser"""
import configparser
import Settings


class SettingException(Exception):
    """ Class for wrapping error from configs"""
    pass


class SettingParser(object):
    """Class parsing setting needed for roku applications from ini file"""

    def __init__(self, path):
        """cstr for roku adapter
               Args:
                   path (str) path of Roku app ini file
        """
        if path is None or len(path) == 0:
            print('Path may not be None or empty')
            return

        self.config = configparser.ConfigParser()
        self.config.read(path)

        if len(self.config) < 3:
            raise SettingException('{} could not be read'.format(path))

        self.get_windows_settings()
        self.get_roku_app()
        self.get_roku_config()

    def get_roku_config(self):
        """Function for retrieving and populating what roku specific setting like ip address """
        try:
            Settings.roku_ip = self.config['Roku_Config']['ip']
        except KeyError as keyerr:
            raise SettingException(keyerr.args[0])

    def get_roku_app(self):
        """Function for retrieving and populating what roku apps buttons user
        want to make appear in gui """
        Settings.roku_apps = []

        try:
            for key in self.config['Roku_Apps']:
                Settings.roku_apps.append(self.config['Roku_Apps'].get(key))
        except KeyError:
            pass

    def get_windows_settings(self):
        """Function to retrieve windows settings"""
        try:
            Settings.width = self.config['Window'].get('width', '500')
            Settings.height = self.config['Window'].get('height', '300')
            Settings.x_offset = self.config['Window'].get('x_offset', '100')
            Settings.y_offset = self.config['Window'].get('y_offset', '100')
        except KeyError:
            pass
