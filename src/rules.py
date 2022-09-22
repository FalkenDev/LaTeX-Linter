""" Rules Module """

from ast import While
from unittest import skip
from src.errors import ErrorDataLoaded
import shutil
import re
import mmap

class Rules():
    """ Rules class """
    def __init__(self, filename = "undefined", file_path = "undefined", json_settings_data = None):
        self.filename = filename    # File name
        self.file_path = file_path  # File path

        self.json_settings_data = json_settings_data

        if self.json_settings_data is None or self.file_path is "undefined":
            raise ErrorDataLoaded

        self.backup_file()
        self.rule_emptylines()
        #self.rule_environment_blocks_exclude()

    def get_specific_settings(self, rule):
        """ Returns the specific setting rule """
        return self.json_settings_data[rule]


    def backup_file(self):
        """ Makes a backup of the file if not the backup exists """
        try:
            dst_dir = "./output/" + "Linted_" + self.filename
            shutil.copy2(self.file_path, dst_dir)
            self.file_path = dst_dir
        except:
            raise ErrorDataLoaded

    def rule_emptylines(self):
        """ Rule Blank lines """
        # WORKS : Needs improvement with the code!

        setting_value = self.get_specific_settings("emptylines")

        rule_include = [
            "\part{",
            "\chapter{",
            "\section{",
            "\subsection{",
            "\subsubsection{",
            "\paragraph{",
            "\subparagraph{"
        ]

        line_number_list = []
        line_number_list_remove = []

        with open(self.file_path, "r") as files:
            for line_number, line in enumerate(files, start=1):
                for word in rule_include:
                    if word in line:
                        file = open(self.file_path)
                        content = file.readlines()
                        mutable_setting_value = setting_value                                       # Reset the mutable to setting value
                        if content[line_number ] != "\n":                                           # If has not "\n" before then apply all \n from settings value
                            for i in range(0, mutable_setting_value):
                                line_number_list.append(line_number)
                        else:                                                                       # If alredy have "\n" before then count how many "\n" it has.
                            counter = 0
                            while True:
                                if content[line_number + counter] == "\n":
                                    mutable_setting_value = mutable_setting_value - 1
                                    counter = counter + 1
                                else:
                                    break                                                           # When no more "\n" is in the line then break it
                            for y in range(0, mutable_setting_value):                               # Apply the rest blank lines
                                line_number_list.append(line_number)
                        file.close()

        append_line = 0
        l1 = []
        with open(self.file_path, 'r') as fp:
            l1 = fp.readlines()

        for line in line_number_list:
            l1.insert(line + append_line, "\n")
            append_line = append_line + 1                                                           # Needs a append line bcs after every "\n" appended then it creates 1 more extra line


        with open(self.file_path, "w") as file:
            l1 = "".join(l1)
            file.write(l1)

        self.replace_line_function(rule_include, setting_value)

    def replace_line_function(self, rule_include, setting_value):
        """ Find the index number and ignores it """
        line_number_list_remove = []
        with open(self.file_path, "r") as files:
            for line_number, line in enumerate(files, start=1):
                for word in rule_include:
                    if word in line:
                        file = open(self.file_path)
                        content = file.readlines()
                        mutable_setting_value = setting_value                                   # Reset the mutable to setting value
                        counter = 0
                        while True:
                            if content[line_number + counter] == "\n":
                                mutable_setting_value = mutable_setting_value - 1
                                counter = counter + 1
                                if counter > setting_value:                                     # If has more lines then setting_value
                                    line_number_list_remove.append(line_number + counter)       # Append the line number
                            else:
                                break                                                           # When no more "\n" is in the line then break it
                        file.close()

        text = []
        with open(self.file_path, "r") as files:
            for line_number, line in enumerate(files, start=1):
                if not line_number in line_number_list_remove:
                     text.append(line)
                else:
                    continue                                                                    # If the line number is in the remove list, it just continues and not append the text line.

        with open(self.file_path, "w") as file:
            text = "".join(text)
            file.write(text)


    def rule_environment_blocks_exclude(self):
        """ Rule environment blocks exclude """

        setting_list = self.get_specific_settings("environment_blocks_exclude")

        word = r'''\begin{'''

        test_list = []

        for setting in setting_list:
            test_list.append(r'''\begin{''' + setting + "}")

        print(test_list)

        end_value = 0

        with open(self.file_path, "r") as FILE:
            for line_number, line in enumerate(FILE, start=1):
                if word in line:
                    file = open(self.file_path)
                    content = file.readlines()
                    if not content[line_number].startswith("\t"):
                        print("Line: " + content[line_number - 1])
                        print(setting)
                        print(content[line_number])
                        print(line_number)
