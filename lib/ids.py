import io
import os
import sys
import json
import requests
from clear_screen import clear
from datetime import datetime
from lib.colors import style


def dump_ids():
    while True:
        clear()
        date = datetime.now().strftime("%H:%M:%S")
        time = datetime.now().strftime("%d/%m/%Y")
        print("     --- Dump All Friends ID's ---")
        print('        --- Author: @Proxy07 ---\n')
        try:
            with open('lib/cache/facebook_token.txt', 'r') as file:
                token = file.read()
        except:
            print(style.RED('\n[!]') + style.RESET(' Error: You must generate an access token first.'))
            sys.exit(0)

        try:
            print_ids = str(input(style.GREEN('[+]') + style.RESET(' Do you want to print all IDs on screen (y/n): ')))
        except KeyboardInterrupt:
            print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
            sys.exit(0)

        try:
            i = 0
            while os.path.exists("Logs/IDs - %s.txt" % i):
                i += 1

            req = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
            json_data = json.loads(req.text)
            with io.open("Logs/IDs - %s.txt" % i, 'w', encoding = 'UTF-8') as f:
                f.write(f'FacebookHunter IDs Scan\nDate : {date}\nTime : {time}\n\n\n\n')
                for x in json_data['data']:
                    f.write(f'{x["name"]} : {x["id"]}\n')
                    if print_ids.lower() == "y":
                        print(style.YELLOW(' [-]') + style.RESET(f' {x["name"]} : {x["id"]}'))
                    else:
                        None

                print(style.GREEN('\n[+]') + style.RESET(f" Saved ID's successfuly in Logs/{'Logs/IDs - %s.txt' % i}"))

        except Exception as e:
            raise
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            print(style.RED('\n[!]') + style.RESET(" Error: Failed to get user's IDs due to connection error.."))
            sys.exit(0)
        input(style.CYAN('[*]') + style.RESET(' Press any key to go back to the main menu.'))
        break
