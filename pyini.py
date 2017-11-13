#!/usr/bin/env python
import ConfigParser
import json

try:
    config = ConfigParser.ConfigParser()
    config.read('/home/cregenye/.aws/credentials')
except ConfigParser.MissingSectionHeaderError, e:
    raise WrongIniFormatError(`e`)


dictionary = {}
for section in config.sections():
    dictionary[section] = {}
    for option in config.options(section):
        dictionary[section][option] = config.get(section, option)

print(json.dumps(dictionary, indent=4))
