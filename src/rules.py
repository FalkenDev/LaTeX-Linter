""" Rules Module """
import json
import ast

class Rules():

    def __init__(self, rule = "Standard"):
        self.rule = rule
        self.json_data = self.__read_json() 

    def __read_json(self):
        jsonfile = open("./settings/settings.json")
        data = json.load(jsonfile)
        jsonfile.close()
        return data

    def get_custom_settings(self):
        return self.json_data["customized"]

    def get_standard_settings(self):
        return self.json_data["standard"]

    def get_current_settings(self):
        return self.rule

    def set_settings(self):
        self.rule = "Customized"

    def edit_custom_settings(self, rule, custom_input):
        jsonfile = open("./settings/settings.json", "w")
        self.json_data["customized"][rule] = custom_input
        json.dump(self.json_data, jsonfile)
        jsonfile.close()
        self.json_data = self.__read_json() 