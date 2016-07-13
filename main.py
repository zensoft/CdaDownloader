from core.logic import *
from utils.proccess_helper import *
from settings.settings import *
from utils.custom_logger import *

custom_logger = CustomLogger()

#"http://www.cda.pl/video/49867892" // nie dziala
#"http://www.cda.pl/video/573845cc" dziala

if __name__ == "__main__":
    """
    When app is locked another instance can not start
    """
    get_lock(APP_NAME)
    custom_logger.log("Start logic")
    run_logic(sys.argv)
    custom_logger.log("End logic")
