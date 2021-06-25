import logging

class BaseLogger:
  def getLogger(self):
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('mylog.log')
    formater = logging.Formatter(" %(asctime)s :%(levelname)s :%s(name)s :%s(message)s")
    fileHandler.setFormatter(formater)
    
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    return logger
