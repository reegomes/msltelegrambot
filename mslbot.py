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
                
pvpwin = 0
pvplost = 0
gem6 = 0
gem5 = 0
energy = 0
astrogem = 0

for idx, linha in enumerate(monitorar(today2)):
    print("{:5d}: {}".format(idx, linha))
    if "No tickets remaining." in linha:
        bot.sendMessage(IDT, "No PvP tickets remaining")
    elif "Kept: 6*" in linha:
        bot.sendMessage(IDT, "Kept 6* Gem")
        gem6 += 1
        bot.sendMessage(IDT, "Gems: " + str(gem6))
    elif "Kept: 5*" in linha:
        bot.sendMessage(IDT, "Kept 5* Gem")
        gem5 += 1
        bot.sendMessage(IDT, "Gems: " + str(gem5))
    elif "Farm Forever has ended." in linha:
        bot.sendMessage(IDT, "Farm Forever has Ended")
    elif "doDailies  6" in linha:
        bot.sendMessage(IDT, "Daily quest completed")
    elif "Catching astromons..." in linha:
        bot.sendMessage(IDT, linha)
    elif "Lost a PvP Battle." in linha:
        bot.sendMessage(IDT, "Lost a PvP Battle.")
        pvplost += 1
        bot.sendMessage(IDT, "Total Defeats " + str(pvplost))
    elif "Won a PvP battle!" in linha:
        bot.sendMessage(IDT, "Won a PvP battle!")
        pvpwin += 1
        bot.sendMessage(IDT, "Total Victories " + str(pvpwin))
    elif "Refilled energy" in linha:
        energy += 80
        astrogem += 30
        bot.sendMessage(IDT, "Refilled Energy: " + str(energy))
        bot.sendMessage(IDT, "Spent Astrogem: " + str(astrogem))
