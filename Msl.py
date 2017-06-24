import time
import sys
import telepot
import configparser

#apitoken = input("Insira o API Token: ")

cfg = configparser.ConfigParser()
cfg.read('config.ini')

apitoken = cfg.get("Main", "token")
IDT = cfg.getint("Main", "id")
######################################################
#getboolean( ), getfloat( ), ou simplesmente get( ) no caso de strings
#x = cfg.getint('section2', 'confign')
######################################################

from datetime import date
today = date.today()
today2 = today.strftime('%d.%m.%Y')

#bot = telepot.Bot("357230833:AAE6EhFCeNR1SUk8Xup1FjlYXBAKHSIru80")
bot = telepot.Bot(apitoken)
from telepot.loop import MessageLoop

#caminho1 = input("Coloque a data de hoje. EX: 31.12.2017: ")
#caminho2 = ("/Users/reego/Desktop/msl-bot/core/data/logs/")
def monitorar(path):
    with open(path, 'r') as arq:
        while True:
            nova_linha = arq.readline()
            nova_linha = nova_linha.replace('\n', '')
            if nova_linha:
                yield nova_linha
            else:
                time.sleep(1.0)

#caminho_arquivo = 'teste.log'
for idx, linha in enumerate(monitorar(today2)):
    print("{:5d}: {}".format(idx, linha))
    if "Error:" in linha:
        bot.sendMessage(IDT, linha)
    elif "Grade: 6*" in linha:
        bot.sendMessage(IDT, linha)
    elif "Refill gems" in linha:
        bot.sendMessage(IDT, linha)
    elif "Finished" in linha:
        bot.sendMessage(IDT, linha)
    elif "Been stuck for 10 minutes!" in linha:
        bot.sendMessage(IDT, linha)
    elif "Catching astromons..." in linha:
        bot.sendMessage(IDT, linha)
    elif "Caught" in linha:
        bot.sendMessage(IDT, linha)
        
        
