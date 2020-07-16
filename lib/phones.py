import io
import os
import sys
import json
import requests
from clear_screen import clear
from datetime import datetime
from lib.colors import style

def dump_phones():
    while True:
        clear()
        date = datetime.now().strftime("%H:%M:%S")
        time = datetime.now().strftime("%d/%m/%Y")
        print("     --- Dump All Friends Phone Numbers ---")
        print('            --- Author: @Proxy07 ---\n')
        try:
            with open('lib/cache/facebook_token.txt', 'r') as file:
                token = file.read()
        except:
            print(style.RED('\n[!]') + style.RESET(' Error: You must generate an access token first.'))
            sys.exit(0)
        try:
            print_numbers = str(input(style.GREEN('[+]') + style.RESET(' Do you want to print all phone numbers on screen (y/n): ')))
        except KeyboardInterrupt:
            print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
            sys.exit(0)
        try:
            i = 0
            while os.path.exists("Logs/phone_numbers - %s.txt" % i):
                i += 1
            req1 = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
            data1 = json.loads(req1.text)

            with io.open("Logs/phone_numbers - %s.txt" % i, 'w', encoding = 'UTF-8') as f:
                for i in data1['data']:
                    req2 =  requests.get(f'https://graph.facebook.com/{i["id"]}?access_token={token}')
                    data2 = json.loads(req2.text)
                    try:
                        f.write(f'{data2["name"]} : {data2["mobile_phone"]}\n')
                        if print_numbers.lower() == "y":
                            print(style.YELLOW(' [-]') + style.RESET(f'{data2["name"]} : {data2["mobile_phone"]}'))
                        else:
                            None
                    except KeyError:
                        pass
                    except KeyboardInterrupt:
                        print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
                        sys.exit(0)
                print(style.GREEN('\n[+]') + style.RESET(' File saved : Logs/Facebook-Data-Logs/{"Logs/phone_numbers - %s.txt" % i}'))
        except KeyboardInterrupt:
            print(style.RED('\n[!]') + style.RESET(' Error: User exited.'))
            sys.exit(0)
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            print(style.RED('\n[!]') + style.RESET(" Error: Failed to get user's phone numbers due to connection error.."))
            sys.exit(0)
        input(style.CYAN('[*]') + style.RESET(' Press any key to go back to the main menu.'))
        break
