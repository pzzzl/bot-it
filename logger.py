import logging
import coloredlogs
from datetime import date, datetime
from path import Path, os

path = os.getcwd()

log_path = f"{path}\\log"

if not Path(log_path).exists():
    os.mkdir(log_path)

today_path = f"{log_path}\\{date.today()}"

if not Path(today_path).exists():
    os.mkdir(today_path)

now = datetime.now().strftime("%H_%M_%S_%f")

logging.basicConfig(filename=f"{today_path}\\{now}.log")
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG', logger=logger, fmt="%(asctime)s - %(levelname)s - %(message)s")