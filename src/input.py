""" Input Module """

class Input():
    """
    Input class
    """

    def __init__(self):
        """
        Init
        """
        self.filename = "undefined"

    def load_file(self, file):
        self.filename = "./input/" + file

    def open_file(self):
        """
        Open the file
        """
        with open(self.filename) as filehandle:
            line = filehandle.read()

        # print the line read from the file
        print(line)