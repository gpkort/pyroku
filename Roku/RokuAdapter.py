"""Module for class Roku adapter"""
import http.client as hc
from lxml import objectify


class RokuAdapter(object):
    """Class that provides functionality to provide html connection to a ROKU tv"""
    PORT = 8060
    TYPE = 'POST'
    DECLARATION = '<?xml version="1.0" encoding="UTF-8" ?>'

    def __init__(self, url):
        """cstr for roku adapter

               Args:
                   url (str) ip of roku device
                   see https://sdkdocs.roku.com/display/sdkdoc/External+Control+Guide
        """
        if url is None or len(url) == 0:
            raise Exception("Url may not be null!")

        self.url = url
        self.applications = self.get_apps()
        self.xml = ''

    def get_apps(self):
        """makes api call to get a list of apps on roku
            Returns: List of objects based on xml entry
        """

        conn = hc.HTTPConnection(self.url, RokuAdapter.PORT)
        conn.request("GET", '/query/apps')
        response = conn.getresponse()
        data = response.read()
        conn.close()
        self.xml = str(data)
        self.massage_xml()

        return self.get_obj_array()

    def app_callback(self, name):
        """wrapper callback app button press for send command
                Args: name (str) name of text value of button
             Returns: status of api call
        """
        for app in self.applications:
            if app.text.upper() == name.upper():
                return self.send_command('/launch/' + app.attrib['id'])

    def up_callback(self):
        """wrapper callback up button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Up')

    def down_callback(self):
        """wrapper callback down button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Down')

    def left_callback(self):
        """wrapper callback left button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Left')

    def right_callback(self):
        """wrapper callback right button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Right')

    def back_callback(self):
        """wrapper callback back button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Back')

    def ok_callback(self):
        """wrapper callback ok button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Select')

    def rewind_callback(self):
        """wrapper callback rewind button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Rev')

    def ff_callback(self):
        """wrapper callback fast forward button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Fwd')

    def pp_callback(self):
        """wrapper callback puase/play button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/Play')

    def home_callback(self):
        """wrapper callback home button press for send command
            Returns: status of api call
        """
        return self.send_command('/keypress/home')

    def send_command(self, requesturl):
        """Function for parsing a double tildae string into a list

        Args:
            requesturl (str) url portion of REST api call

        Returns:
            status of api call and reason
        """
        conn = hc.HTTPConnection(self.url, RokuAdapter.PORT)
        conn.request(RokuAdapter.TYPE, requesturl)
        response = conn.getresponse()

        result = str(response.status) + "-" + response.reason
        conn.close()

        return result

    def get_obj_array(self):
        """Function for parsing a double tilde string into a list

        Returns:
            List of objects based on xml entry
        """

        strarr = self.xml.split('~~')
        objarr = []

        for line in strarr:
            objarr.append(objectify.fromstring(line))

        return objarr

    def massage_xml(self):
        """Function for massaging data in to a form that lxml.objectify can handle """
        self.xml = self.xml[2:]
        self.xml = self.xml.replace(RokuAdapter.DECLARATION, '')
        self.xml = self.xml[0:len(self.xml) - 1]
        self.xml = self.xml.replace('\\n<apps>\\n', '')
        self.xml = self.xml.replace('\\n</apps>\\n', '')
        self.xml = self.xml.replace('\\r', '')
        self.xml = self.xml.replace('\\t', '')

        self.xml = self.xml.replace('\\n', '~~')
