""" Input Module """

import fnmatch
import os
from src.errors import WrongFile

class File():
    """
    Input class
    """

    def __init__(self):
        """
        Init current_file and filename to Undefined
        """
        self.current_file = "Undefined"
        self.filename = "Undefined"

    def set_file(self, file):
        """
        Set a specific .tex file to use for the linter
        """
        for input_file in os.listdir('./input'):
                if fnmatch.fnmatch(input_file, '*.tex'):
                    if file == input_file:
                        self.current_file = str(file)
                        self.filename = "./input/" + file
                        return
        raise WrongFile

    def get_current_file(self):
        """
        Returns what current file is set
        """
        return self.current_file

    def open_file(self):
        """
        Open the file
        """
        with open(self.filename) as filehandle:
            line = filehandle.read()

        # print the line read from the file
        print(line)