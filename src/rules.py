""" Rules Module """
# pylint: disable=line-too-long

import shutil
import re
from sys import platform
from src.errors import ErrorDataLoaded


class Rules():
    """ Rules class """
    def __init__(self, filename = "undefined", file_path = "undefined", json_settings_data = None):
        """ Init the variables, check operating system and run the linter. """

        self.filename = filename    # File name
        self.file_path = file_path  # File path
        self.json_settings_data = json_settings_data # Json Settings

         # --- Check what operating system user are using --- #
        if platform in ("linux", "linux2", "darwin"):
            self.newline = "\n"
        elif platform == "win32":
            self.newline = "\r\n"

        # --- If soemthing has not passed into the Rules class --- #
        if (self.json_settings_data is None or
            self.file_path == "undefined" or
            self.filename == "undefined"):
            raise ErrorDataLoaded

        # --- Running the Backup + the Linter rules --- #
        self.backup_file()
        self.rule_sentence_newline()
        self.rule_emptylines()
        self.rule_environment_blocks_exclude()
        self.rule_comment_space()

    def get_specific_settings(self, rule):
        """ Returns the specific setting rule value """
        return self.json_settings_data[rule]


    def backup_file(self):
        """
        Makes a backup of the file.
        Using the backup file for the linter
        """
        dst_dir = "./output/" + "Linted_" + self.filename
        shutil.copy2(self.file_path, dst_dir)
        self.file_path = dst_dir

    def rule_emptylines(self):
        """
        Rule Blank lines, print out blank lines before section, chapter, etc.

        Check if line is in the rule_include list then checks if it alredy has some newlines.
        If it have: Find how many alredy is there and then append the rest of the newlines.
        else: Append all newlines.
        """
        # WORKS : Needs improvement with the code!

        setting_value = self.get_specific_settings("emptylines")
        newline = self.newline
        line_number_list = []

        rule_include = [
            r"\part{",
            r"\chapter{",
            r"\section{",
            r"\subsection{",
            r"\subsubsection{",
            r"\paragraph{",
            r"\subparagraph{"
        ]

        with open(self.file_path, "r", encoding="utf-8") as file1:
            for line_number, line in enumerate(file1, start=1):
                for word in rule_include:
                    if word in line:
                        with open(self.file_path, "r", encoding="utf-8") as file2:
                            content = file2.readlines()
                            mutable_setting_value = setting_value # Reset the mutable to setting value
                            if content[line_number - 2] != newline: # If not \n before then apply all \n
                                for _ in range(0, mutable_setting_value):
                                    line_number_list.append(line_number - 2)
                            else: # If alredy have "\n" before then count how many "\n" it has.
                                counter = 2 # Need to get to the upper index
                                while True:
                                    if content[line_number - counter] == newline:
                                        mutable_setting_value = mutable_setting_value - 1
                                        counter = counter + 1
                                    else:
                                        break # When no more "\n" is in the line then break it
                                for _ in range(0, mutable_setting_value): # Apply the rest blank lines
                                    line_number_list.append(line_number - 2)

        append_line = 0
        file_list = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            file_list = file.readlines()

        for line in line_number_list:
            file_list.insert(line + append_line + 1, newline)
            append_line = append_line + 1 # append_line is for every "\n" applied so it still apply correct index

        with open(self.file_path, "w", encoding="utf-8") as file:
            file_list = "".join(file_list)
            file.write(file_list)

        self.replace_line_function(rule_include, setting_value) # Look if text have to many "\n"

    def replace_line_function(self, rule_include, setting_value):
        """
        Function for the Rule Blank lines.
        Find the index number that has to many blank lines and ignores it.
        """
        newline = self.newline
        line_number_list_remove = []

        with open(self.file_path, "r", encoding="utf-8") as file1:
            for line_number, line in enumerate(file1, start=1):
                for word in rule_include:
                    if word in line:
                        with open(self.file_path, "r", encoding="utf-8") as file2:
                            content = file2.readlines()
                            mutable_setting_value = setting_value
                            counter = 0
                            line_counter = 2
                            while True:
                                if content[line_number - line_counter] == newline:
                                    mutable_setting_value = mutable_setting_value - 1
                                    counter = counter + 1
                                    line_counter = line_counter + 1
                                    if counter > setting_value: # If more blanklines the settings value
                                        line_number_list_remove.append( # Append the line number
                                            line_number - line_counter
                                        )
                                else:
                                    break
        text = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line_number - 2 in line_number_list_remove:
                    text.append(line)
                else:
                    continue # Ignore the append

        with open(self.file_path, "w", encoding="utf-8") as file:
            text = "".join(text)
            file.write(text)


    def rule_environment_blocks_exclude(self):
        """ Rule environment blocks exclude """

        setting_list = self.get_specific_settings("environment_blocks_exclude") # Get settings

        word = r"\begin{" # Word to look after
        tab = "\t" # The tab space to use
        newline = self.newline # Newline to use

        setting_exclude_string_list = []
        tab_index_list = []
        begin_counter = 0 # Counts how many \begin{ in \begin{
        counter = 0 # How many index positions it alredy have been looked at

        for setting in setting_list:
            setting_exclude_string_list.append(word + setting + "}")

        print(setting_exclude_string_list)

        with open(self.file_path, "r", encoding="utf-8") as file1:
            for line_number, line in enumerate(file1, start=1):
                if line_number <= counter - 1: # If the program alredy have checked those index position
                    pass
                elif word in line.rstrip() and any(exclude in line for exclude in setting_exclude_string_list) is False and not line.startswith("%"): # If word is in the line and line is not on exclude list and it's not a comment block
                    line_counter = 0 # Counter to get to next index line
                    begin_counter = 1 # When get to a \begin{}
                    with open(self.file_path, "r", encoding="utf-8") as file2:
                        content = file2.readlines()
                        tab_index_list.append([
                            (line_number + line_counter - 1),
                            ((begin_counter - 1) * tab),
                            (content[line_number + line_counter - 1].strip())
                        ])
                        while True: # Checks trough the whole \begin to the begins \end
                            if begin_counter == 0: # If the line in index have got to the last \end for the \begin
                                break
                            if word in content[line_number + line_counter].strip():
                                begin_counter += 1
                                tab_index_list.append([
                                    (line_number + line_counter),
                                    ((begin_counter - 1) * tab),
                                    (content[line_number + line_counter].strip())
                                ])
                                line_counter += 1
                            elif "\\end" in content[line_number + line_counter].strip():
                                tab_index_list.append([
                                    (line_number + line_counter),
                                    ((begin_counter - 1) * tab),
                                    (content[line_number + line_counter].strip())
                                ])
                                begin_counter -= 1
                                line_counter += 1
                            else:
                                tab_index_list.append([
                                    (line_number + line_counter),
                                    (begin_counter * tab),
                                    (content[line_number + line_counter].strip())])
                                line_counter += 1

                        counter = line_number + line_counter # How many index position the program have checked after the while loop

        file_list = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            file_list = file.readlines()

        for line in tab_index_list:
            file_list[line[0]] = line[1] + line[2] + newline # Replace the index position with how many tabs, the line and a \n

        with open(self.file_path, "w", encoding="utf-8") as file:
            file_list = "".join(file_list)
            file.write(file_list)

    def rule_comment_space(self):
        """ Rule Comment Space """

        space_value = self.get_specific_settings("comment-space") # Get settings
        space_index_list = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if "%" in line:
                    found_percent = False
                    precent_index = 0
                    for char_index, char in enumerate(line, start=1):
                        if (
                            char_index == 2 and
                            char.startswith("-") or
                            char_index == 2 and
                            char.startswith("%")
                        ):
                            found_percent = False
                            break

                        if char == "%":
                            found_percent = True
                            precent_index = char_index

                    if found_percent:
                        space_index_list.append([line_number, line, precent_index])

        file_list = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            file_list = file.readlines()

        for line in space_index_list:
            file_list[line[0] - 1] = line[1][:line[2]] + (" " * (space_value - 1)) + line[1][line[2]:]

        with open(self.file_path, "w", encoding="utf-8") as file:
            file_list = "".join(file_list)
            file.write(file_list)

    def rule_sentence_newline(self):
        """ Rule sentence newline for better git support """
        sentence_newline = self.get_specific_settings("sentence-newline") # Get settings
        dot_index_list = []
        newline = self.newline

        if sentence_newline is True:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if re.search("[?!.][ ]", line) and not line.startswith("%"):
                        same_line_number = 0
                        line_length = len(line)
                        for char_index, char in enumerate(line, start=1):
                            if line_length <= (char_index + 1):
                                break
                            if re.search("[?!.]", char) and line[char_index] is " ":
                                if same_line_number is line_number:
                                    line1 = ""
                                else:
                                    line1 = line
                                same_line_number = line_number
                                dot_index_list.append([line_number, line1, char_index])
            file_list = []

            with open(self.file_path, 'r', encoding="utf-8") as file:
                file_list = file.readlines()

            for line in dot_index_list:
                if line[1] == "": # If it same line as before then take the line which was used before and insert is as new line bcs else the \n won't apear when same text is there all the way
                    line[1] = file_list[line[0] - 1]
                file_list[line[0] - 1] = line[1][:line[2]] + (newline) + line[1][line[2] + 1:]

            with open(self.file_path, "w", encoding="utf-8") as file:
                file_list = "".join(file_list)
                file.write(file_list)
        else:
            return #  If false then just return
