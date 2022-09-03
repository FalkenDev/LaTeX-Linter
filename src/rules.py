""" Rules Module """
import json
import ast

class Rules():

    def read_json(self):
        jsonfile = open("./settings/settings.json")
        data = json.load(jsonfile)
        return data