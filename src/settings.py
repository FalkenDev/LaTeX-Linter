""" Settings Module """
import json
import ast
from src.errors import AlredyExists, DontExists

green = '\x1b[1;32m'
end_color = '\x1b[0m'

class Settings():

    def __init__(self, rule = "standard"):
        """
        Init 
        Init rule to standrad if nothing is inputed
        Init json_data to save all settings in settings.json
        """
        self.rule = rule
        self.json_data = self.__read_json() 

    def __read_json(self):
        """
        Read settings.json file
        """
        jsonfile = open("./settings/settings.json")
        data = json.load(jsonfile)
        jsonfile.close()
        return data

    def get_settings(self, settings_name):
        """
        Return data from specific settings object
        """
        return self.json_data[settings_name]

    def get_current_settings(self):
        """
        Return what settings is used now
        """
        return self.rule

    def set_settings(self, rule):
        """
        Set 
        """
        self.rule = rule

    def edit_custom_settings(self, rule, custom_input):
        """
        Edit rules on customized settings
        Takes what rule want to be changed and the user input
        """
        jsonfile = open("./settings/settings.json", "w")
        self.json_data["customized"][rule] = custom_input
        json.dump(self.json_data, jsonfile)
        jsonfile.close()
        self.json_data = self.__read_json() 
        print(green + " Setting rule: " + str(rule) + " has updated to have value: " + str(custom_input) + end_color)
        return

    def edit_enviroment_blocks_exclude_add(self, custom_input):
        """
        Adds user input to list in enviroment_blocks_exclude in json file
        Raise exception AlredyExists if user input is alredy in the exclude list
        """
        jsonfile = open("./settings/settings.json", "w")

        for block in self.json_data["customized"]["environment_blocks_exclude"]:
            if block == custom_input:
                raise AlredyExists
        self.json_data["customized"]["environment_blocks_exclude"].append(custom_input)
        json.dump(self.json_data, jsonfile)
        jsonfile.close()
        self.json_data = self.__read_json() 
        print(green + " Setting rule: environment_blocks_exclude has added: " + str(custom_input) + " to the list." + end_color)
        input("\n Press enter to go back to Edit Enviroment Blocks.")
        return

    def edit_enviroment_blocks_exclude_remove(self, custom_input):
        """
        Remove user input from the list in enviroment_blocks_exclude in json file
        Raise exception DontExists if not user input is in the exclude list
        """
        jsonfile = open("./settings/settings.json", "w")

        for block in self.json_data["customized"]["environment_blocks_exclude"]:
            if str(block) == str(custom_input):
                self.json_data["customized"]["environment_blocks_exclude"].remove(custom_input)
                json.dump(self.json_data, jsonfile)
                jsonfile.close()
                self.json_data = self.__read_json() 
                print(green + " Setting rule: environment_blocks_exclude has removed: " + str(custom_input) + " from the list." + end_color)
                input("\n Press enter to go back to Edit Enviroment Blocks.")
                return
        raise DontExists