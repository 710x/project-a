import os
import adbutils
from dotenv import load_dotenv
from general_bot import Bot

load_dotenv()
WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH"))
WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT"))
CONTINUE_AUTO = int(os.getenv("CONTINUE_AUTO"))
DEFAULT_PASS = os.getenv("DEFAULT_PASS")
ACCOUNT_MIN = int(os.getenv("ACCOUNT_MIN"))
ACCOUNT_MAX = int(os.getenv("ACCOUNT_MAX"))
EMAIL_PREFIX = os.getenv("EMAIL_PREFIX")
EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER")
ACCOUNT_MIN_1 = int(os.getenv("ACCOUNT_MIN_1"))
ACCOUNT_MAX_1 = int(os.getenv("ACCOUNT_MAX_1"))
ACC_REVERSE = int(os.getenv("ACC_REVERSE"))
MAX_USERNAME_LENGTH = int(os.getenv("MAX_USERNAME_LENGTH"))
APP_PACKAGE = os.getenv("APP_PACKAGE")

if __name__ == '__main__':
    adb = adbutils.AdbClient('127.0.0.1', 5037)
    boy_list = []
    for d in adb.device_list():
        bot = Bot(serial=d.serial, app_package=APP_PACKAGE)
        bot.init_game.start_game()
        login = bot.init_game.login()
        print(login)
