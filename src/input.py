""" Input Module """

import fnmatch
import os

class Input():
    """
    Input class
    """

    def __init__(self):
        """
        Init
        """
        self.current_file = "Undefined"
        self.filename = "Undefined"

    def set_file(self, file):
        for input_file in os.listdir('./input'):
                if fnmatch.fnmatch(input_file, '*.tex') or fnmatch.fnmatch(input_file, '*.bib'):
                    if file == input_file:
                        self.current_file = str(file)
                        self.filename = "./input/" + file
                        return
        # Fix so it raise a customized exception if not matching
        return

    def get_current_file(self):
        return self.current_file

    def open_file(self):
        """
        Open the file
        """
        with open(self.filename) as filehandle:
            line = filehandle.read()

        # print the line read from the file
        print(line)