""" Rules Module """

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
        #self.rule_emptylines()
        self.rule_environment_blocks_exclude()

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

        with open(self.file_path, "r") as files:
            for line_number, line in enumerate(files, start=1):
                for word in rule_include:
                    if word in line:
                        file = open(self.file_path)
                        content = file.readlines()
                        for i in range(1, setting_value):
                            if content[line_number + i] != "\n":
                                line_number_list.append(line_number + 1)
                                for i in range(i + 1, setting_value):
                                    line_number_list.append(line_number + 1)
                                break
                        file.close()
        append_line = 0
        l1 = []
        with open(self.file_path, 'r') as fp:
            l1 = fp.readlines()

        for line in line_number_list:
            l1.insert(line + append_line, "\n")
            append_line = append_line + 1


        with open(self.file_path, "w") as file:
            l1 = "".join(l1)
            file.write(l1)

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
