import logging
import datetime
from selenium.webdriver.support.events import AbstractEventListener

log_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    # log file will be created in "tests" directory. Feel free to change the path or filename
    filename=f"{log_filename}.log",
    format="%(asctime)s: %(levelname)s: %(message)s",
    level=logging.INFO
)


class WebDriverListener(AbstractEventListener):
    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.logger.info(exception)
