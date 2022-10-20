""" Test module to test Rule class from rule.py"""
import unittest
import fnmatch
import os
import re
from src.rules import Rules
from src.file import File
from src.settings import Settings
from src.errors import ErrorDataLoaded
# pylint: disable=protected-access
# pylint: disable=line-too-long

class TestRule(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self, set_file = "test_main.tex", set_settings = "standard"):
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
        self.assertEqual(comment, 3)
        self.assertEqual(emptylines, 3)
        self.assertEqual(environment, ["document", "appendices"])

        self.tearDown()


    def test_backup_file(self):
        """ [Rule] Test to backup test_article.tex file """
        self.setUp("test_article.tex", "standard")
        count = 0
        for file in os.listdir('./output'):
            if fnmatch.fnmatch(file, 'Linted_test_article.tex'):
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
        with open("./output/Linted_test_emptylines.tex", "r", encoding="utf-8") as linted_test_file:
            for __, line in enumerate(linted_test_file, start=1):
                if line == "\n":
                    counter += 1
                for word in rule_include:
                    if word in line:
                        if counter != value:
                            self.fail("Emptylines rule failed | too many or to few lines created!")
                        else:
                            counter = 0

        self.tearDown()

    def test_rule_environment_blocks(self):
        """
        [Rule] Test rule Environment Blocks
        Test if the enviroment blocks have correct tab spaces
        """
        self.setUp("test_enviroment.tex", "standard")

        exclude_list = self.settings.get_settings_specific("standard","environment_blocks_exclude")
        setting_exclude_string_list = []
        word = r"\begin{" # Word to look after

        for setting in exclude_list:
            setting_exclude_string_list.append(word + setting + "}")

        found_word = False
        counter = 0
        with open("./output/Linted_test_enviroment.tex", "r", encoding="utf-8") as linted_test_file:
            for index, line in enumerate(linted_test_file, start=1):
                if word in line.strip() and not line.strip() in setting_exclude_string_list:
                    found_word = True
                if found_word:
                    if "\\begin{" in line.strip():
                        counter += 1
                        if not line.startswith((counter - 1) * "\t"):
                            self.fail("Enviroment block rule failed | Index: " + str(index) + "Line: " + line + " | \\begin has to few tab spaces")
                        elif line.startswith(counter * "\t"):
                            self.fail("Enviroment block rule failed | Index: " + str(index) + "Line: " + line + " | \\begin has to many tab spaces!")
                    elif "\\end" in line.strip():
                        counter -= 1
                        if not line.startswith(counter * "\t"):
                            self.fail("Enviroment block rule failed | Index: " + str(index) + "Line: " + line + " | \\end has to few tab spaces")
                        if line.startswith((counter + 1) * "\t"):
                            self.fail("Enviroment block rule failed | Index: " + str(index) + "Line: " + line + " | \\end has to many tab spaces!")
                    else:
                        if not line.startswith(counter * "\t"):
                            self.fail("Enviroment block rule failed | Index: " + str(index) + "Line: " + line + " | \\text has to few tab spaces")
                        if line.startswith((counter + 1) * "\t"):
                            self.fail("Enviroment block rule failed | Index: " + str(index) + "Line: " + line + " | \\text has to many tab spaces!")
                    if counter == 0:
                        found_word = False


        self.tearDown()

    def test_rule_environment_blocks_with_exclude(self):
        """
        [Rule] Test rule Environment Blocks with Exclude.
        Test if the enviroment blocks dosen't changhe when in exclude list.
        If it have found over 4 lines with no tab space then it passes and resets to find next exclude block.
        """
        self.setUp("test_enviroment.tex", "standard")

        exclude_list = self.settings.get_settings_specific("standard","environment_blocks_exclude")
        setting_exclude_string_list = []
        word = r"\begin{" # Word to look after
        for setting in exclude_list:
            setting_exclude_string_list.append(word + setting + "}")

        found_exclude_word = False
        index_counter = 0
        with open("./output/Linted_test_enviroment.tex", "r", encoding="utf-8") as linted_test_file:
            for __, line in enumerate(linted_test_file, start=1):
                if  line.strip() in setting_exclude_string_list:
                    found_exclude_word = True
                if found_exclude_word and not line.startswith("\t"):
                    index_counter += 1
                elif found_exclude_word and line.startswith("\t"):
                    found_exclude_word = False
                    if index_counter > 4:
                        index_counter = 0
                    else:
                        self.fail("Rule Environment Blocks With Exclude FAILED | It have tab space")
        self.tearDown()

    def test_rule_comment_space(self):
        """ [Rule] Test rule Comment Space """
        self.setUp("test_comment.tex", "standard")
        value = self.settings.get_settings_specific("standard","comment-space")
        ignore_line = 0
        with open("./output/Linted_test_comment.tex", "r", encoding="utf-8") as linted_file:
            for line_index, line in enumerate(linted_file, start=1):
                if ignore_line > line_index:
                    pass
                elif "%" in line:
                    found_procentage = False
                    counter = 0
                    for char_index, char in enumerate(line, start=1):
                        if "%" in char:
                            found_procentage = True
                        elif found_procentage:
                            if char == " ":
                                counter += 1
                            elif char == "-" or char == "%":
                                ignore_line = line_index + 2
                                break
                            if counter > value:
                                self.fail(
                                        "Comment space rule at line index: " +
                                        str(line_index) +
                                        " Char: " +
                                        str(char_index) +
                                        " has more space then settings value!"
                                    )
                            elif char.isalpha():
                                if counter < value and counter != 0: # != is bcs those who have % and no space with a word is word that is just out commented to use soon so no real comment
                                    self.fail(
                                        "Comment space rule at line index: " +
                                        str(line_index) +
                                        " Char: " +
                                        str(char_index) +
                                        " has less space then settings value!"
                                    )
                                break
        self.tearDown()

    def test_rule_sentence_newline(self):
        """ [Rule] Test rule Sentence Newline """
        self.setUp("test_sentence_newline.tex", "standard")
        with open("./output/Linted_test_sentence_newline.tex", "r", encoding="utf-8") as linted_file:
            for line_index, line in enumerate(linted_file, start=1):
                if re.search("[?!.]", line) and not line.startswith("%"):
                    counter = 0
                    found_dot = False
                    for __, char in enumerate(line, start=1):
                        if re.search("[?!.]", char):
                            counter += 1
                            found_dot = True
                        elif found_dot and re.search("[a-zA-Z1-9]", char):
                            found_dot = False
                        elif found_dot and re.search("[ ]", char):
                            self.fail("Sentence newline rule failed at line: " + str(line_index))
        self.tearDown()
