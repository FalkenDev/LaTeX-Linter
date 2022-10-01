""" Rules Module """

import shutil
from sys import platform
from src.errors import ErrorDataLoaded

# pylint: disable=line-too-long

class Rules():
    """ Rules class """
    def __init__(self, filename = "undefined", file_path = "undefined", json_settings_data = None):
        self.filename = filename    # File name
        self.file_path = file_path  # File path

        if platform in ("linux", "linux2", "darwin"):
            self.newline = "\n"
        elif platform == "win32":
            self.newline = "\r\n"

        self.json_settings_data = json_settings_data # Json Settings

        if self.json_settings_data is None or self.file_path == "undefined": # not loaded correctly
            raise ErrorDataLoaded

        self.backup_file() # Done
        self.rule_sentence_newline() # Almost Done # Needs to be first bcs of \begin can be wrong tabs if apply \n after
        self.rule_emptylines() # Done
        self.rule_environment_blocks_exclude() # Done
        self.rule_comment_space() # Almost Done

    def get_specific_settings(self, rule):
        """ Returns the specific setting rule """
        return self.json_settings_data[rule]


    def backup_file(self):
        """ Makes a backup of the file if not the backup exists """
        dst_dir = "./output/" + "Linted_" + self.filename
        shutil.copy2(self.file_path, dst_dir)
        self.file_path = dst_dir

    def rule_emptylines(self):
        """ Rule Blank lines, print out blank lines before rule_include """
        # WORKS : Needs improvement with the code!

        setting_value = self.get_specific_settings("emptylines")
        newline = self.newline

        rule_include = [
            r"\part{",
            r"\chapter{",
            r"\section{",
            r"\subsection{",
            r"\subsubsection{",
            r"\paragraph{",
            r"\subparagraph{"
        ]

        line_number_list = []
        with open(self.file_path, "r", encoding="utf-8") as file1:
            for line_number, line in enumerate(file1, start=1):
                for word in rule_include:
                    if word in line:
                        file2 = open(self.file_path, encoding="utf-8")
                        content = file2.readlines()
                        mutable_setting_value = setting_value                                       # Reset the mutable to setting value
                        if content[line_number - 2] != newline:                                           # If has not "\n" before then apply all \n from settings value
                            for _ in range(0, mutable_setting_value):
                                line_number_list.append(line_number - 2)
                        else:                                                                       # If alredy have "\n" before then count how many "\n" it has.
                            counter = 2
                            while True:
                                if content[line_number - counter] == newline:
                                    mutable_setting_value = mutable_setting_value - 1
                                    counter = counter + 1
                                else:
                                    break                                                           # When no more "\n" is in the line then break it
                            for _ in range(0, mutable_setting_value):                               # Apply the rest blank lines
                                line_number_list.append(line_number - 2)
                        file2.close()

        append_line = 0
        file_list = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            file_list = file.readlines()

        for line in line_number_list:
            file_list.insert(line + append_line, newline)
            append_line = append_line + 1                                                           # Needs a append line bcs after every "\n" appended then it creates 1 more extra line

        with open(self.file_path, "w", encoding="utf-8") as file:
            file_list = "".join(file_list)
            file.write(file_list)

        self.replace_line_function(rule_include, setting_value)

    def replace_line_function(self, rule_include, setting_value):
        """ Find the index number and ignores it """
        newline = self.newline
        line_number_list_remove = []
        with open(self.file_path, "r", encoding="utf-8") as files:
            for line_number, line in enumerate(files, start=1):
                for word in rule_include:
                    if word in line:
                        file = open(self.file_path, encoding="utf-8")
                        content = file.readlines()
                        mutable_setting_value = setting_value                                   # Reset the mutable to setting value
                        counter = 0
                        line_counter = 2
                        while True:
                            if content[line_number - line_counter] == newline:
                                mutable_setting_value = mutable_setting_value - 1
                                counter = counter + 1
                                line_counter = line_counter + 1
                                if counter > setting_value:                                     # If has more lines then setting_value
                                    line_number_list_remove.append(line_number - line_counter)       # Append the line number
                            else:
                                break                                                           # When no more "\n" is in the line then break it
                        file.close()

        text = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line_number - 2 in line_number_list_remove: #Kolla om denna stämmer utan (line_number - 2)
                    text.append(line)
                else:
                    continue                                                                    # If the line number is in the remove list, it just continues and not append the text line.

        with open(self.file_path, "w", encoding="utf-8") as file:
            text = "".join(text)
            file.write(text)


    def rule_environment_blocks_exclude(self):
        """ Rule environment blocks exclude """

        setting_list = self.get_specific_settings("environment_blocks_exclude") # Get settings

        word = r"\begin{" # Word to look after
        tab = "\t"
        newline = self.newline

        setting_exclude_string_list = []
        tab_index_list = []
        begin_counter = 0
        line_counter = 0
        counter = 0

        for setting in setting_list:
            setting_exclude_string_list.append(word + setting + "}")

        with open(self.file_path, "r", encoding="utf-8") as file1:
            for line_number, line in enumerate(file1, start=1):
                if line_number <= counter - 1:                                                                                                                        # If the program alredy have checked those index position
                    pass                                                                                                                                              # Pass, Just get to next line_number and line
                elif word in line.rstrip() and line.rstrip() not in setting_exclude_string_list:                                                                      # If word is in the line and line is not on exclude list
                    line_counter = 0                                                                                                                                  # Counter to get to next index line
                    begin_counter = 1                                                                                                                               # When get to a \begin{}
                    file2 = open(self.file_path, encoding="utf-8")
                    content = file2.readlines()
                    tab_index_list.append([
                        (line_number + line_counter - 1),
                        ((begin_counter - 1) * tab),
                        (content[line_number + line_counter - 1].strip())
                    ])
                    while True:                                                                                                                                       # Checks trough the whole \begin to the begins \end
                        if begin_counter == 0:                                                                                                                        # If the line in index have got to the last \end for the \begin
                            break
                        if word in content[line_number + line_counter].strip():                                                                                     # If it's a \begin in a \begin
                            begin_counter += 1
                            tab_index_list.append([
                                (line_number + line_counter),
                                ((begin_counter - 1) * tab),
                                (content[line_number + line_counter].strip())
                            ])
                            line_counter += 1
                        elif "\\end" in content[line_number + line_counter].strip():                                                                                  # If it's a \end in a \begin
                            tab_index_list.append([
                                (line_number + line_counter),
                                ((begin_counter - 1) * tab),
                                (content[line_number + line_counter].strip())
                            ])
                            begin_counter -= 1
                            line_counter += 1
                        else:                                                                # If it dosen't have correct \t ( Tab space )
                            tab_index_list.append([
                                (line_number + line_counter),
                                (begin_counter * tab),
                                (content[line_number + line_counter].strip())])
                            line_counter += 1

                    counter = line_number + line_counter                                                                                                              # How many index position the program have checked after the while loop

        file_list = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            file_list = file.readlines()

        for line in tab_index_list:
            file_list[line[0]] = line[1] + line[2] + newline                                                                                                                     # Replace the index position with how many tabs, the line and a \n

        with open(self.file_path, "w", encoding="utf-8") as file:
            file_list = "".join(file_list)
            file.write(file_list)

    def rule_comment_space(self):
        """ Rule Comment Space """

        space_value = self.get_specific_settings("comment-space") # Get settings
        space_index_list = []

        with open(self.file_path, "r", encoding="utf-8") as FILE:
            for line_number, line in enumerate(FILE, start=1):
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
        """ Rule sentence newline for better git suppourt"""
        sentence_newline = self.get_specific_settings("sentence-newline") # Get settings
        dot_index_list = []
        newline = self.newline

        if sentence_newline is True:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if ". " in line:
                        same_line_number = 0
                        line_length = len(line)
                        for char_index, char in enumerate(line, start=1):
                            if line_length <= (char_index + 1):
                                break
                            if char == "." and line[char_index] is " ":
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
            return
