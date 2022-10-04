""" Test module to test Rule class from rule.py"""
import unittest
import fnmatch
import os
from src.rules import Rules
from src.file import File
from src.settings import Settings
from src.errors import ErrorDataLoaded
# pylint: disable=protected-access
# pylint: disable=line-too-long

class TestRule(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self, set_file = "main.tex", set_settings = "standard"):
        """ [Rule] Setup File, Settings and Rule class for the Rule class """
        # Arrange
        self.file = File()
        self.file.set_file(set_file)
        filename = self.file.get_current_file() # Get current file path
        filepath = self.file.get_current_filename() # Get file name

        self.settings = Settings()
        self.settings.set_settings(set_settings)
        settings_json_data = self.settings.get_settings(self.settings.get_current_settings()) # Get settings

        self.rules = Rules(filename, filepath, settings_json_data)

    def tearDown(self):
        """ [Rule] Reset File, Settings and Rule class for the Rule class """
        # Arrange
        self.rules = None
        self.file = None
        self.settings = None

    def test_init_correct_way(self):
        """ [Rule] Test Rule class that init works as expected """ # Kanske göra ett till setup med utan all asserts
        try:
            self.setUp()
        except ErrorDataLoaded:
            self.fail("Rule class raised ErrorDataLoaded exception")
        self.tearDown()

    def test_init_get_exception(self):
        """ [Rule] Test Rule class that init raises a exception when no input is inputed to the rule class """
        with self.assertRaises(ErrorDataLoaded) as _:
            self.rules = Rules()
        self.tearDown()

    def test_get_specific_settings_standard(self):
        """ [Rule] Test to get a specific setting in standard settings """
        self.setUp()

        newline = self.rules.get_specific_settings("sentence-newline")
        comment = self.rules.get_specific_settings("comment-space")
        emptylines = self.rules.get_specific_settings("emptylines")
        environment = self.rules.get_specific_settings("environment_blocks_exclude")

        self.assertEqual(newline, True)
        self.assertEqual(comment, 1)
        self.assertEqual(emptylines, 2)
        self.assertEqual(environment, ["document", "appendices"])

        self.tearDown()


    def test_backup_file(self):
        """ [Rule] Test to backup article_3.tex file """
        self.setUp("article_3.tex", "standard")
        count = 0
        for file in os.listdir('./output'):
            if fnmatch.fnmatch(file, 'Linted_article_3.tex'):
                count += 1

        if count != 1:
            self.fail("Backup failed | Not right backup created!")

        self.tearDown()

    def test_rule_emptylines_standard(self):
        """ [Rule] Test the rule Emptylines with standard settings and file test_emptylines.tex"""
        self.setUp("test_emptylines.tex", "standard")
        value = self.settings.get_settings_specific("standard","emptylines")

        rule_include = [
            r"\part{",
            r"\chapter{",
            r"\section{",
            r"\subsection{",
            r"\subsubsection{",
            r"\paragraph{",
            r"\subparagraph{"
        ]
        counter = 0
        with open("./output/Linted_test_emptylines.tex", "r", encoding="utf-8") as linted_file:
            for __, line in enumerate(linted_file, start=1):
                if line == "\n":
                    counter += 1
                for word in rule_include:
                    if word in line:
                        if counter != value: # If newline counter is not how many the settings value should be
                            self.fail("Emptylines rule failed | too many or to few lines created!")
                        else:
                            counter = 0

        self.tearDown()

    def test_rule_emptylines_customized(self):
        """ [Rule] Test the rule Emptylines with customized settings and file test_emptylines.tex"""
        self.setUp("test_emptylines.tex", "customized")
        value = self.settings.get_settings_specific("customized","emptylines")

        rule_include = [
            r"\part{",
            r"\chapter{",
            r"\section{",
            r"\subsection{",
            r"\subsubsection{",
            r"\paragraph{",
            r"\subparagraph{"
        ]
        counter = 0
        with open("./output/Linted_test_emptylines.tex", "r", encoding="utf-8") as linted_file:
            for __, line in enumerate(linted_file, start=1):
                if line == "\n":
                    counter += 1
                for word in rule_include:
                    if word in line:
                        if counter != value:
                            self.fail("Emptylines rule failed | too many or to few lines created!")
                        else:
                            counter = 0

        self.tearDown()

    def test_rule_environment_blocks_exclude(self):
        """ [Rule] Test rule Environment Blocks Exclude """
        self.setUp()



        self.tearDown()

    def test_rule_comment_space(self):
        """ [Rule] Test rule Comment Space """
        self.setUp()



        self.tearDown()

    def test_rule_sentence_newline(self):
        """ [Rule] Test rule Sentence Newline """
        self.setUp()



        self.tearDown()
