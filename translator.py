# -*- coding: utf-8 -*-

import json

class alias(object):
    def command(string):
        string = string.lower()

        f = open('translation/commands.json')
        command_list = json.load(f)
        f.close()

        for key, value in command_list.items():
            if string in value['alias']:
                return key
        
        return

    def mode(string):
        string = string.lower()

        f = open('translation/general.json')
        modes = json.load(f)['mode']
        f.close()

        for key, value in modes.items():
            if string in value:
                return int(key)

        return
    
    def language(string):
        string = string.lower()

        f = open('translation/general.json')
        modes = json.load(f)['language']
        f.close()

        for key, value in modes.items():
            if string in value:
                return key

        return

    def property(string):
        string = string.lower()
        f = open('translation/general.json')
        properties = json.load(f)['property']
        f.close()

        for key, value in properties.items():
            if string in value:
                return key

        return