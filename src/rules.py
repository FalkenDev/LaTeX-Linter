""" Rules Module """

from itertools import count
from unittest import skip
from src.errors import ErrorDataLoaded
import shutil

class Rules():
    """ Rules class """
    def __init__(self, filename = "undefined", file_path = "undefined", json_settings_data = None):
        self.filename = filename    # File name
        self.file_path = file_path  # File path

        self.json_settings_data = json_settings_data # Json Settings

        if self.json_settings_data is None or self.file_path == "undefined": # If not loaded correctly
            raise ErrorDataLoaded

        self.backup_file() # Done
        #self.rule_emptylines() # Done
        #self.rule_environment_blocks_exclude() # Done
        self.rule_comment_space() # Doing

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
        """ Rule Blank lines, print out blank lines before rule_include """
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
                        mutable_setting_value = setting_value                                       # Reset the mutable to setting value
                        if content[line_number - 2] != "\n":                                           # If has not "\n" before then apply all \n from settings value
                            for i in range(0, mutable_setting_value):
                                line_number_list.append(line_number - 2)
                        else:                                                                       # If alredy have "\n" before then count how many "\n" it has.
                            counter = 2
                            while True:
                                if content[line_number - counter] == "\n":
                                    mutable_setting_value = mutable_setting_value - 1
                                    counter = counter + 1
                                else:
                                    break                                                           # When no more "\n" is in the line then break it
                            for y in range(0, mutable_setting_value):                               # Apply the rest blank lines
                                line_number_list.append(line_number - 2)
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
                        line_counter = 2
                        while True:
                            if content[line_number - line_counter] == "\n":
                                mutable_setting_value = mutable_setting_value - 1
                                counter = counter + 1
                                line_counter = line_counter + 1
                                if counter > setting_value:                                     # If has more lines then setting_value
                                    line_number_list_remove.append(line_number - line_counter)       # Append the line number
                            else:
                                break                                                           # When no more "\n" is in the line then break it
                        file.close()

        text = []
        with open(self.file_path, "r") as files:
            for line_number, line in enumerate(files, start=1):
                if not (line_number - 2) in line_number_list_remove:
                     text.append(line)
                else:
                    continue                                                                    # If the line number is in the remove list, it just continues and not append the text line.

        with open(self.file_path, "w") as file:
            text = "".join(text)
            file.write(text)


    def rule_environment_blocks_exclude(self):
        """ Rule environment blocks exclude """

        setting_list = self.get_specific_settings("environment_blocks_exclude") # Get settings

        word = r"\begin{" # Word to look after

        setting_exclude_string_list = []
        tab_index_list = []
        begin_counter = 0
        line_counter = 0
        counter = 0

        for setting in setting_list:
            setting_exclude_string_list.append(word + setting + "}")

        with open(self.file_path, "r") as FILE:
            for line_number, line in enumerate(FILE, start=1):
                if line_number <= counter - 1:                                                                                                                        # If the program alredy have checked those index position
                    pass                                                                                                                                              # Pass, Just get to next line_number and line
                elif word in line.rstrip() and line.rstrip() not in setting_exclude_string_list:                                                                      # If word is in the line and line is not on exclude list
                    line_counter = 0                                                                                                                                  # Counter to get to next index line
                    begin_counter = 1                                                                                                                               # When get to a \begin{}
                    file = open(self.file_path)
                    content = file.readlines()
                    tab_index_list.append([(line_number + line_counter - 1), ((begin_counter - 1) * "\t"), (content[line_number + line_counter - 1].strip())])
                    while True:                                                                                                                                       # Checks trough the whole \begin to the begins \end
                        if begin_counter == 0:                                                                                                                        # If the line in index have got to the last \end for the \begin
                            break
                        elif word in content[line_number + line_counter].strip():                                                                                     # If it's a \begin in a \begin
                            begin_counter += 1
                            tab_index_list.append([(line_number + line_counter), ((begin_counter - 1) * "\t"), (content[line_number + line_counter].strip())])
                            line_counter += 1
                        elif "\\end" in content[line_number + line_counter].strip():                                                                                  # If it's a \end in a \begin
                            tab_index_list.append([(line_number + line_counter), ((begin_counter - 1) * "\t"), (content[line_number + line_counter].strip())])
                            begin_counter -= 1
                            line_counter += 1
                        else:                                                                # If it dosen't have correct \t ( Tab space )
                            tab_index_list.append([(line_number + line_counter), (begin_counter * "\t"), (content[line_number + line_counter].strip())])
                            line_counter += 1

                    counter = line_number + line_counter                                                                                                              # How many index position the program have checked after the while loop

        l1 = []
        with open(self.file_path, 'r') as fp:
            l1 = fp.readlines()

        for line in tab_index_list:
            l1[line[0]] = line[1] + line[2] + "\n"                                                                                                                     # Replace the index position with how many tabs, the line and a \n

        with open(self.file_path, "w") as file:
            l1 = "".join(l1)
            file.write(l1)

    def rule_comment_space(self):
        """ Rule Comment Space """

        space_value = self.get_specific_settings("comment-space") # Get settings
