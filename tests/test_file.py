""" Test module to test File class from file.py"""
import unittest
from src.file import File
from src.errors import WrongFile
# pylint: disable=protected-access

class TestFile(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self):
        """ [File] Setup for the File class """
        # Arrange
        self.file = File()

    def tearDown(self):
        """ [File] Reset for the File class """
        # Arrange
        self.file = None

    def test_init(self):
        """ [File] Test File class that init works as expected """
        self.setUp()
        self.assertEqual(self.file.current_file, "undefined")
        self.assertEqual(self.file.filename, "undefined")
        self.tearDown()

    def test_set_correct_file(self):
        """ [File] Test File class to set a new filename from input folder with .tex file """
        self.setUp()
        self.file.set_file("test_main.tex")
        self.assertEqual(self.file.get_current_file(), "test_main.tex")
        self.tearDown()

    def test_exception_set_wrong_file(self):
        """ [File] Test File class that WrongFile exception raises when input wrong file """
        self.setUp()
        with self.assertRaises(WrongFile) as _:
            self.file.set_file("art.json")
        self.tearDown()
