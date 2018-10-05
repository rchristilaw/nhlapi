#!/usr/bin/env python
import json

from constants import url_constants


class Api:
    def getTeams(self):
        with open('../data/teams.json') as json_data:
            d = json.load(json_data)
            return d

