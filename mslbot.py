import time
import sys
import telepot
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

apitoken = cfg.get("Main", "token")
IDT = cfg.getint("Main", "id")

from datetime import date
today = date.today()
today2 = today.strftime('%d.%m.%Y.txt')

bot = telepot.Bot(apitoken)
from telepot.loop import MessageLoop

def monitorar(path):
    with open(path, 'r') as arq:
        while True:
            nova_linha = arq.readline()
            nova_linha = nova_linha.replace('\n', '')
            if nova_linha:
                yield nova_linha
            else:
                time.sleep(1.0)
                
for idx, linha in enumerate(monitorar(today2)):
    print("{:5d}: {}".format(idx, linha))
    if "No tickets remaining." in linha:
        bot.sendMessage(IDT, linha)
    elif "Kept: 6*" in linha:
        bot.sendMessage(IDT, linha)
    elif "|400" in linha:
        bot.sendMessage(IDT, linha)
    elif "Farm Forever has ended." in linha:
        bot.sendMessage(IDT, linha)
    elif "doDailies  6" in linha:
        bot.sendMessage(IDT, linha)
    elif "Catching astromons..." in linha:
        bot.sendMessage(IDT, linha)
    elif "Lost a PvP Battle." in linha:
        bot.sendMessage(IDT, linha)
    elif "Won a PvP battle!" in linha:
        bot.sendMessage(IDT, linha)
