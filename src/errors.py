""" Errors module """
class WrongFile(Exception):
    """ When the file entered by user is not same as the files with .tex in input folder """

class WrongCommand(Exception):
    """ When user enters a command that dosen't exists """