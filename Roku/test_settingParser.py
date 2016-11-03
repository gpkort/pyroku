from unittest import TestCase
import SettingParser as sp
import Settings


class TestSettingParser(TestCase):

    def setUp(self):
        self.parser = sp.SettingParser('/Users/gregkorthuis/PycharmProjects/Roku/settings.ini')

    def test_get_roku_config(self):
        self.assertEqual('192.168.1.123', Settings.roku_ip, 'Ip does not match')

    def test_get_roku_app(self):
        self.assertEqual(3, len(Settings.roku_apps), 'Not all apps were found')
