"""Module for class Roku form"""
import tkinter as tk
from tkinter import ttk
import Settings


class RokuForm(tk.Frame): # pylint: disable=too-many-ancestors
    """Tkinter form to provide control of a roku via desktop et al"""
    def __init__(self, parent, rokucontrol=None, is_error=False, error_message=''):
        """cstr for roku form
               Args:
                   parent tkinter root frame
                   rokucontrol roku adapter for callbacks
                   is_error Determines if form should just display an error
                   error_message if needed the error message to display
        """
        tk.Frame.__init__(self, parent, background="black")
        self.style = ttk.Style()
        self.parent = parent
        self.rokucontrol = rokucontrol

        self.init_ui()

        if is_error:
            self.place_error_message(error_message)
        else:
            self.place_buttons()
            self.place_app_buttons()

    def init_ui(self):
        """method to set title and theme  """
        self.parent.title("Roku Player Controller")
        self.style.theme_use("default")

    def place_error_message(self, message):
        """method to display error if need and cease any further functionality  """
        msg = tk.Message(self.parent, text='Error: ' + message)
        msg.config(bg='white', font=('times', 18, 'bold'))
        msg.pack()

    def place_app_buttons(self):
        """method to place roku application buttons from ini file  """
        i = 0
        for app in Settings.roku_apps:# pylint: disable=no-member
            tk.Button(self.parent,
                      text=app,
                      command=lambda: self.rokucontrol.app_callback(app)).grid(row=i, column=4)
            i += 1

    def place_buttons(self):
        """method to place functional rokubuttons """
        tk.Button(self.parent, text='^', command=self.up_callback).grid(row=0, column=1)
        tk.Button(self.parent, text='v', command=self.down_callback).grid(row=2, column=1)
        tk.Button(self.parent, text='>', command=self.right_callback).grid(row=1, column=2)
        tk.Button(self.parent, text='<', command=self.left_callback).grid(row=1, column=0)
        tk.Button(self.parent, text='<-', command=self.back_callback).grid(row=0, column=0)
        tk.Button(self.parent, text='OK', command=self.ok_callback).grid(row=1, column=1)
        tk.Button(self.parent, text='<<', command=self.rewind_callback).grid(row=3, column=0)
        tk.Button(self.parent, text='>||', command=self.pp_callback).grid(row=3, column=1)
        tk.Button(self.parent, text='>>', command=self.pp_callback).grid(row=3, column=2)

        tk.Button(self.parent, text='HOME', command=self.home_callback).grid(row=0, column=3)

    def up_callback(self):
        """callback wrapper for up button  """
        self.rokucontrol.up_callback()

    def down_callback(self):
        """callback wrapper for down button  """
        self.rokucontrol.down_callback()

    def left_callback(self):
        """callback wrapper for left button  """
        self.rokucontrol.left_callback()

    def right_callback(self):
        """callback wrapper for right button  """
        self.rokucontrol.right_callback()

    def back_callback(self):
        """callback wrapper for back button  """
        self.rokucontrol.back_callback()

    def ok_callback(self):
        """callback wrapper for ok button  """
        self.rokucontrol.ok_callback()

    def rewind_callback(self):
        """callback wrapper for rewind button  """
        self.rokucontrol.rewind_callback()

    def ff_callback(self):
        """callback wrapper for fast forward button  """
        self.rokucontrol.ff_callback()

    def pp_callback(self):
        """callback wrapper for pause/play button  """
        self.rokucontrol.pp_callback()

    def home_callback(self):
        """callback wrapper for home button  """
        self.rokucontrol.home_callback()
