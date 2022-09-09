""" Settings Module """
import json
import ast

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