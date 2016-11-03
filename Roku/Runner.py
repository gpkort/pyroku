#!/usr/bin/env python3
"""Main module"""
from tkinter import Tk
import RokuForm as rf
import RokuAdapter as ra
import Settings
from SettingParser import SettingParser as sp, SettingException


def main():
    """Main function"""
    is_error = False
    message = ''
    root = Tk()
    adapter = None

    try:
        sp('/Users/gregkorthuis/PycharmProjects/Roku/settings.ini')
        adapter = ra.RokuAdapter(Settings.roku_ip)
        geostring = Settings.width + 'x' + Settings.height + '+' \
                    + Settings.x_offset + '+' + Settings.y_offset
        root.geometry(geostring)
    except SettingException as sexp:
        is_error = True
        message = sexp.args[0]
        root.geometry("350x150+100+100")



    rf.RokuForm(root, adapter, is_error, message)
    root.mainloop()


if __name__ == '__main__':
    main()
