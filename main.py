import adbutils

from general_bot import Bot

if __name__ == '__main__':
    adb = adbutils.AdbClient('127.0.0.1', 5037)
    boy_list = []
    for d in adb.device_list():
        bot = Bot(d.serial)
        bot.init_game.start_game()
        login = bot.init_game.login()
        print(login)

