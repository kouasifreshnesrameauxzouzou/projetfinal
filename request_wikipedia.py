# -*- coding: utf-8 -*-

"""

fiu
"""

__auteur__="z.kouassi@cerco.ia"
__coequiriers__="k.kael@cerco.ia"
__date__="2020-02-26"

import sys
import json

import requests
from dewiki import parser

def main():
    
    valid_numbers_of_arguments = False if len(sys.argv) != 2 else True
    if valid_numbers_of_arguments:
        things_to_search = sys.argv[1]
        req = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles={}&format=json".format(things_to_search))
        if req.status_code == 200:
            if not req.text:
                print("This note was not found")
            res = json.dumps(req.json())
            dewiki_parser = parser.Parser()
            result = dewiki_parser.parse_string(res)
            with open("{}.txt".format(things_to_search), "w") as file:
                file.write(result)            
        elif req.status_code == 400:
            print("The syntax of the query is erroneous")
        elif req.status_code == 404:
            print("Not found")
        elif req.status_code == 500:
            print("Server error")
        else:
            print("An error occur")
    else:
        print('Invalid number of argument')

if __name__ == "__main__":
    main()
