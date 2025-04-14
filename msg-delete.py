##################################################################################
#                                                                                #
#   ce script a ete entierement developper par zxk                               #
#   merci de respecter le travail fourni et de ne pas le modifier                #
#   dans le but de vous l’approprier ou de le republier sous un autre nom        #
#                                                                                #
#   ce tool a demande du temps, de l’energie et de la passion                    #
#   chaque ligne de code a ete pensee pour fonctionner proprement                #
#   et vous proposer une experience fluide et fonctionnelle                      #
#                                                                                #
#   toute modification sans autorisation est deconseillee par respect            #
#   pour moi zxk                                                                 #
#                                                                                #
#   si vous avez besoin d’une version personnalisee, contactez moi directement   #
#   sur discord : zxk_no_ban                                                     #
#                                                                                #
#   encore merci de ne pas voler le travail                                      #
#                                                                                #
##################################################################################

import requests
import time
import sys
import os
from colorama import Fore, init
from pystyle import Colors, Colorate

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################

ascii = Colorate.Diagonal(Colors.blue_to_purple, '''
                                             ______     __  __     __  __    
                                            /\___  \   /\_\_\_\   /\ \/ /    
                                            \/_/  /__  \/_/\_\/_  \ \  _"-.  
                                              /\_____\   /\_\/\_\  \ \_\ \_\ 
                                              \/_____/   \/_/\/_/   \/_/\/_/ 
                                                    _           
                                            | |    | |    | |           | |          
                                          __| | ___| | ___| |_ ___    __| |_ __ ___  
                                         / _ |/ _ \ |/ _ \ __/ _ \  / _ | '_  _ \ 
                                        | (_| |  __/ |  __/ ||  __/ | (_| | | | | | |
                                         \__,_|\___|_|\___|\__\___|  \__,_|_| |_| |_| 
                          
''')

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#   pour le partager a votre nom par respect#
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################

os.system('cls' if os.name == 'nt' else 'clear')
print(ascii)
print(Fore.RED + """                              Dev by zxk // supprime tous tes messages d\'une conv ou d'un serv\n""")

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#   pour le partager a votre nom par respect#
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################

token = input(Fore.LIGHTGREEN_EX+ '[+] ton token : ')
chan = input(Fore.LIGHTGREEN_EX + '[+] id du salon ou dm : ')

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#   pour le partager a votre nom par respect#
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################

headers = {
    'authorization': token,
    'user-agent': 'Mozilla/5.0'
}

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#   pour le partager a votre nom par respect#
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################

me = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if me.status_code != 200:
    print(Fore.RED + '[!] token invalide')
    sys.exit()
uid = me.json()['id']
print(Fore.GREEN + f'[i] connecté en tant que {me.json()["username"]}#{me.json()["discriminator"]}\n')

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#   pour le partager a votre nom par respect#
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################

while True:
    while True:
        r = requests.get(f'https://discord.com/api/v9/channels/{chan}/messages?limit=100', headers=headers)
        if r.status_code != 200:
            print(Fore.RED + "[!] erreur d'accès au salon")
            break
        msgs = r.json()
        if not msgs:
            print(Fore.GREEN + "[✓] tous tes messages sont supprimés")
            break

        found_msg = False
        for m in msgs:
            if m['author']['id'] == uid:
                found_msg = True
                try:
                    delurl = f'https://discord.com/api/v9/channels/{chan}/messages/{m["id"]}'
                    res = requests.delete(delurl, headers=headers)
                    if res.status_code == 204:
                        print(Fore.GREEN + '[✓] supprimé :', m['id'])
                    elif res.status_code == 429:
                        retry = res.json()['retry_after']
                        print(Fore.RED + f'[!] rate limit, attente {max(20, retry):.2f}s')
                        time.sleep(max(20, retry))  
                    else:
                        print(Fore.RED + f'[x] erreur {res.status_code}')
                    time.sleep(0.3) 
                except Exception as e:
                    print(Fore.RED + f'[x] erreur pendant suppression: {str(e)}')
            else:
                print(Fore.BLUE + '[+] ignoré (pas ton msg)')
        
        if not found_msg:
            print(Fore.GREEN + "[✓] tous tes messages sont supprimés (les autres sont ignorés)")
            break

    choix = input(Fore.YELLOW + "\n[i] veux-tu supprimer tes messages dans une autre conversation ? (y/n) : ").lower()
    if choix == 'y':
        chan = input(Fore.LIGHTGREEN_EX + '[+] id du nouveau salon ou dm : ')
    else:
        print(Fore.CYAN + "[i] ok.")
        break

#############################################
#                                           #
#   ce code a ete developper par zxk        #
#   merci de pas modifier le code           #
#   pour le partager a votre nom par respect#
#                                           #
#   discord : zxk_no_ban                    #
#                                           #
#############################################
